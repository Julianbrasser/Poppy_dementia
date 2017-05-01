import os, sys, pygame
from datetime import datetime
from pygame.locals import *
from math import pi
from AbstractClasses import *
from Singletons import *
from GUIcommands import *

class PoppyWindow(SwitchableWindow):
    def __init__(self):
        eventTable = CreateEventTable()
        self.commands.append(eventTable)
        self.view()


        #checks for events with a delay
        while 1:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    sys.exit(0)
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.display.quit()
                    sys.exit(0)

            pygame.display.update()


            pygame.time.delay(DELAYTIME)



