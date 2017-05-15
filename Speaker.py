import pyttsx
from gtts import gTTS
import os


class GoogleSpeaker:

     def speak(self, text):
        tts = gTTS(text=text, lang='nl')
        tts.save("tospeak.mp3")
        # this is for linux
        #make sure you have entered the command "sudo apt-get install mpg321"
        os.system("mpg321 tospeak.mp3")

class Speaker:
    def __init__(self):
        self.engine = pyttsx.init()
        self.rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', self.rate + 10)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()




