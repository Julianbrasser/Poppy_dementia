import os, sys, pygame
from datetime import datetime
from pygame.locals import *
from math import pi
from AbstractClasses import *
from Singletons import *


class CreateEventTable(Command):

    events = {}

    def __init__(self, events):
        self.events = events


    def execute(self):
        # draw a table for showing the upcoming 10 events
        # draw header-text
        font = pygame.font.Font(None, 24)
        fontimg1 = font.render("Tijd", 1, WHITE)
        fontimg2 = font.render("Wat te doen", 1, WHITE)
        Bag.screen.blit(fontimg1, (10, 20))
        Bag.screen.blit(fontimg2, (50, 20))
        # draw double line
        pygame.draw.aaline(Bag.screen, WHITE, (20, 40), (300, 40))
        pygame.draw.aaline(Bag.screen, WHITE, (20, 50), (300, 50))

        # draw vertical line
        pygame.draw.aaline(Bag.screen, WHITE, (40, 50), (40, 500))

        # draw text
        rows = 0;
        if not self.events:
            print('No upcoming events found.')
        for event in self.events:
            timestamp = str(event['start'].get('dateTime'))

            date = timestamp[:-15]
            i = datetime.now()
            currentdate = i.strftime('%Y-%m-%d')

            if date == currentdate:
                time = timestamp[11:-9];
                summary = event['summary']

                timeRender = font.render(time, 1, WHITE)
                summaryRender = font.render(summary, 1, WHITE)
                Bag.screen.blit(timeRender, (0, 60 + (20 * rows)))
                Bag.screen.blit(summaryRender, (50, 60 + (20 * rows)))
                rows = rows + 1





