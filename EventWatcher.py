from __future__ import print_function
import httplib2
import os
from datetime import datetime

from googleapiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from Singletons import *
from AbstractClasses import *
from PopupWindow import *
from Speaker import *

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'

class RetrieveCommand(Command):
    receiver = object
    intervalSeconds = 5

    callsPerHit = int
    callsUntilHit = int

    def __init__(self, receiver):
        self.receiver = receiver
        self.callsPerHit = int(self.intervalSeconds * 1000 / DELAYTIME)
        self.callsUntilHit = self.callsPerHit

    def execute(self):
        self.callsUntilHit = self.callsUntilHit - 1

        if (self.callsUntilHit == 0):
            self.receiver.retrieve()
            self.callsUntilHit = self.callsPerHit

class EventWatcher:
    __metaclass__ = Singleton

    events = {}
    eventsToday = {}

    firstEvent ={}

    def __init__(self):
        self.retrieve()
        CallRegularly.commands.append(RetrieveCommand(self))

    def retrieve(self):
        try:
            import argparse
            flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
        except ImportError:
            flags = None

            """Shows basic usage of the Google Calendar API.

                   Creates a Google Calendar API service object and outputs a list of the next
                   10 events on the user's calendar.
                   """

        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('calendar', 'v3', http=http)

        now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events for today')
        eventsResult = service.events().list(
            calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
            orderBy='startTime').execute()
        self.events = eventsResult.get('items', [])

        #let popup appear when a new event is starting
        self.firstEvent = self.events[0]
        timestamp = str(self.firstEvent['start'].get('dateTime'))




    def get_credentials(self):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'calendar-python-quickstart.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else:  # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials