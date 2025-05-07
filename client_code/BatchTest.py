from . import Server_Batching
import anvil.server

def on_test1_complete(data):
    print(data)

with Server_Batching.BatchServerCall():
    test1 = anvil.server.call("test1").on_complete(on_test1_complete)
    test2 = anvil.server.call("test4")
    test3 = anvil.server.call('test3')


print(test2.value)
print(test3.value)