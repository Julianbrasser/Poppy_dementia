import pyttsx

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+10)
engine.say('Komt een vrouw bij de dokter')
engine.runAndWait()