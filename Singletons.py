class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

#Singleton to put things in, like: the containing screen
class Bag(object):
    __metaclass__ = Singleton

class CallRegularly(object):
    __metaclass__ = Singleton
    commands = []

class ViewProxy(object):
    __metaclass__ = Singleton
    popups = []
    normalWindows = []

    def viewPopup(self, window):
        window.showMaximized()
        self.popups.append(window)

    def viewNormal(self, window):
        self.normalWindows.append(window)
        if self.popups == []:
            self.normalWindows.pop().showMaximized()

    def closeLast(self):
        if self.popups == [] and self.normalWindows != []:
            self.normalWindows.pop().showMaximized()
        elif self.popups != []:
            self.popups.pop().showMaximized()



