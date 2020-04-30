from os import path
import json
import google.oauth2.credentials
from google.assistant.library import Assistant

if __name__ == '__main__':
    try:
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
                print(event)
    finally:
        print("[INFO] program ended.")