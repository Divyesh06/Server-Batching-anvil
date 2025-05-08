from ._anvil_designer import Form1Template
from ..Form2 import Form2
from ..Form3 import Form3
import anvil.server
from .. import Server_Batching
class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)
        Server_Batching.start_global_batching()
        
    def form_show(self, **event_args):
        anvil.server.call('test1')
        self.add_component(Form2())
        self.add_component(Form3())
        
        Server_Batching.execute_global_batch()
        