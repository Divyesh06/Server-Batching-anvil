import anvil.server

global_batch = None

class QueuedServerCall:
    def __init__(self):
        self.value = None
        self.callback = None

    def on_complete(self, callback):
        self.callback = callback

    def raise_completed_callback(self):
        if self.callback:
            self.callback(self.value)

class BatchServerCall:
    def __init__(self):
        self.queued_server_calls_ref = []
        self.queued_server_calls_data = []
        
    def server_call_patch(self, name, *args, **kwargs):
        queued_call = QueuedServerCall()
        server_call_data = {'args': args, "kwargs": kwargs, "name": name}
        self.queued_server_calls_ref.append(queued_call)
        self.queued_server_calls_data.append(server_call_data)
        return queued_call
        
    def __enter__(self):
        self._original_server_call = anvil.server.call
        anvil.server.call = self.server_call_patch

    def __exit__(self, *args, **kwargs):
        
        return_datas = self._original_server_call('Server_Batching.batch_call_executor', self.queued_server_calls_data)

        for index, queued_call in enumerate(self.queued_server_calls_ref):
            return_data = return_datas[index]
            queued_call.value = return_data
            queued_call.raise_completed_callback()

        anvil.server.call = self._original_server_call

def start_global_batching():
    global global_batch
    global_batch = BatchServerCall()
    global_batch.__enter__()

def execute_global_batch():
    global_batch.__exit__()