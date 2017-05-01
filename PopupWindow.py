from AbstractClasses import *
from Singletons import *
from Speaker import *

class PopupWindow(SwitchableWindow):
    backgroundColor = GREEN
    event = {}
    speaker = {}

    def __init__(self, event):
        self.event = event
        self.speaker = Speaker()

    def view(self):
        ViewProxy().viewPopup(self)
        








