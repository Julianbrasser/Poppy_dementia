import pyttsx


class Speaker:
    def __init__(self):
        self.engine = pyttsx.init()
        self.rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', self.rate + 10)


    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


