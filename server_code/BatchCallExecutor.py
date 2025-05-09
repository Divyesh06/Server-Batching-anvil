import anvil.server
from anvil import _server
@anvil.server.callable("Server_Batching.batch_call_executor")
def batch_call_executor(server_call_data):
    return_datas = []
    registrations = _server.registrations
    for server_call in server_call_data:
        callable = registrations.get(server_call['name'])
        
        if not callable:
            print(f"Warning: No Server Function \"{server_call['name']}\" exists")
            return_datas.append(None)
            continue

        try:
            return_datas.append(callable(*server_call['args'], **server_call['kwargs']))
        except Exception as e:
            print(f"Warning: Error calling Server Function \"{server_call['name']}\". The following exception was raised: {e}")
            return_datas.append(None)

    return return_datas
