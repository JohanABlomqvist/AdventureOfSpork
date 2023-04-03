import os
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_google_sheets_api():
    creds, _ = google.auth.default()
    service = build('sheets', 'v4', credentials=creds, cache_discovery=False)
    return service