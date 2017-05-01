import os, sys, pygame
from datetime import datetime
from pygame.locals import *
from math import pi
from Singletons import *

#Constants
WHITE = 255, 255, 255
GREEN = 0, 255, 0
BLACK = 0, 0, 0
BLUE = 0, 0, 255
RED = 255, 0, 0
SCREENSIZE = width, height = 410, 300

DELAYTIME = 500

#function to object. You may call it 'delegate-item'
class Command:


    def execute(self):
        raise NotImplementedError


#allows windows to switch back and forth as the active window
class SwitchableWindow:
    commands = []
    backgroundColor = BLACK

    def showMaximized(self):
        pygame.draw.rect(Bag.screen, self.backgroundColor, (0, 0, SCREENSIZE[0], SCREENSIZE[1]), 0)  # Fills the whole containing screen

        for c in self.commands:
            c.execute()

    def view(self):
        ViewProxy().viewNormal(self)

#observer pattern





