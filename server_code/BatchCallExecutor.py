import anvil.server
from anvil import _server
@anvil.server.callable
def batch_call_executor(server_call_data):
    return_datas = []
    registrations = _server.registrations
    for server_call in server_call_data:
        callable = registrations.get(server_call['name'])
        
        if not callable:
            print(f"Warning: No Server Function \"{server_call['name']}\" exists")
            return_datas.append(None)
            continue
            
        return_datas.append(callable(*server_call['args'], **server_call['kwargs']))

    return return_datas
