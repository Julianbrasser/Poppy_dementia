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
        if len(self.popups) >= 1:
            self.normalWindows.append(window)
        else:
            window.showMaximized()
            self.normalWindows.append(window)


    def closeLast(self):
        if len(self.popups) == 1:
            self.normalWindows[-1].showMaximized()
            self.popups = []
        elif len(self.popups) >= 2:
            self.popups[-2].showMaximized()
            self.popups.pop()
        elif len(self.popups) == 0 and len(self.normalWindows) >= 1:
            self.normalWindows[-2].showMaximized()
            self.normalWindows.pop()




