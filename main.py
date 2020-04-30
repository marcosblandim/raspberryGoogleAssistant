from os import path
import json
import google.oauth2.credentials
from google.assistant.library import Assistant

from event_handlers import HANDLERS

debug=True

def start_assist():
    credentials = path.join(
        path.expanduser('/home/pi/.config'),
        'google-oauthlib-tool',
        'credentials.json'
    )
    with open(credentials, 'r') as f:
        credentials = google.oauth2.credentials.Credentials(token=None,
                                                            **json.load(f))

    with Assistant(credentials) as assistant:
        for event in assistant.start():
            for handler in HANDLERS:
                if debug:
                    print("[DEBUG] event triggered.")
                    print(event)
                handler(event, debug=debug)

if __name__ == '__main__':
    try:
        if debug:
            print("[DEBUG] program started.")
        start_assist()
    finally:
        if debug:
            print("[DEBUG] program ended.")