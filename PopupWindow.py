from AbstractClasses import *
from Singletons import *
from Speaker import *
from GUIcommands import *

class PopupWindow(SwitchableWindow):
    backgroundColor = GREEN
    speaker = {}

    def __init__(self, event):
        eventStamp = StampPopup(event)
        self.commands.append(eventStamp)
        self.view()


    def view(self):
        ViewProxy().viewPopup(self)









