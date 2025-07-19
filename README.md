# Server Batching for Anvil

Created a simple package that allows batching of Server Calls. If you want to avoid multiple server calls in your app but also avoid writing a single complicated server function, this package will do the job for you.

## Clone Link

https://anvil.works/build#clone:VKSHYAFNFY34XEBI=XDUVUJZKC33A54YGDRMOHULL

## Usage
There are three ways of using it

### 1 - ‘with’ block with .value

```python
import anvil.server
from Server_Batching import Server_Batching

with Server_Batching.BatchServerCall(): 
    call_1 = anvil.server.call('test1') #Use server calls normally
    call_2 = anvil.server.call('test2') 

print(call_1.value) #The return value of the server call is accessible from .value
print(call_2.value)
```
In this example, a single call will execute both `test_1` and `test_2`. The value for test1 and test2 can be accessed at .value after the with block. If you try to access .value inside the with block itself, it will return None

## 2. ‘with’ block with callback

```python
import anvil.server
from Server_Batching import Server_Batching

def handle_test_1(value):
   print(value)

def handle_test_2(value):
   print(value)

with Server_Batching.BatchServerCall():  
    
    anvil.server.call('test1').on_complete(handle_test_1)
    anvil.server.call('test2').on_complete(handle_test_2)
```

### 3. Global Batching with on_complete

For more complex app structures, you can use a global batching system. This gives you complete control over when to start batching and when to execute those batch. Useful if you are embedding multiple forms that may have calls of their own.

For example (Assuming that SubForm1 and SubForm2 have their own server calls in form_show)

```python

from ._anvil_designer import Form1Template
from Server_Batching import Server_Batching

class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)
        Server_Batching.start_global_batching()

        self.add_component(SubForm1())
        self.add_component(SubForm2())

    def form_show(self, **event_args):
        Server_Batching.execute_global_batch()
```
Unless you call the execute_global_batch, any server calls happening anywhere on the app (after start_global_batch) will be queued. With global batching, it is usually best to use the on_complete callback.
