import os
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_google_sheets_api():
    creds, _ = google.auth.default()
    service = build('sheets', 'v4', credentials=creds, cache_discovery=False)
    return service

def get_row(row_number):
    try:
        service = get_google_sheets_api()
        sheet_id = '1y1gpQaX6n1Pix4pcw7K_MTS8X1hg_703FGEO3Y4Ll3w'
        range_name = f'Sheet1!A{row_number}:H{row_number}'
        result = (
            service.spreadsheets().values().get(
                spreadsheetId=sheet_id, range=range_name).execute()
        )
        return result['values'][0]
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None


def display_dialogue(character, dialogue, options):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{character}: {dialogue}")
    for i, option in enumerate(options, 1):
        print(f"({i}) {option}")

def play_game():
    current_row = 1
    while True:
        row_data = get_row(current_row)
        (
            character, dialogue, option_a, option_b, option_c,
            next_a, next_b, next_c
        ) = row_data

        options = [option for option in [option_a, option_b, option_c] if option]
        next_rows = [int(next_row) for next_row in [next_a, next_b, next_c] if next_row]

        display_dialogue(character, dialogue, options)
