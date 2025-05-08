from ._anvil_designer import Form3Template
import anvil.server


class Form3(Form3Template):
    def __init__(self, **properties):
        self.init_components(**properties)

    def form_show(self, **event_args):
        anvil.server.call("test2")
