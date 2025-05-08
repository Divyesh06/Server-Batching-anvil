from ._anvil_designer import Form2Template
import anvil.server

class Form2(Form2Template):
    def __init__(self, **properties):
        self.init_components(**properties)

    def form_show(self, **event_args):
        anvil.server.call("test1")

    