from __future__ import print_function
import httplib2
import os

import os, sys, pygame
from datetime import datetime
from pygame.locals import *
from math import pi

from PopupWindow import *
from GUIcommands import *

from googleapiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


from PoppyWindow import PoppyWindow
from Singletons import *
from AbstractClasses import *
from ListenInBackground import *


#initialization of the containing screen
Bag().screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Vandaag")
pygame.init()

window =  PoppyWindow();







