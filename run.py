import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_google_sheets_api():
    key_file_path = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
    creds = service_account.Credentials.from_service_account_file(key_file_path)
    service = build('sheets', 'v4', credentials=creds, cache_discovery=False)
    return service

def get_row(row_number):
    try:
        service = get_google_sheets_api()
        sheet_id = '1y1gpQaX6n1Pix4pcw7K_MTS8X1hg_703FGEO3Y4Ll3w'
        range_name = f'Sheet1!A{row_number}:B{row_number}'
        result = (
            service.spreadsheets().values().get(
                spreadsheetId=sheet_id, range=range_name).execute()
        )
        return result['values'][0]
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

def display_visuals(current_row):
    if current_row in range(2, 5):
        print("===== Forest =====")
        print("  .  /\\")
        print(" *- /  \\")
        print("    /\\  \\")
        print("   /  \\  \\")
        print("  /    \\  \\")
        print("===================")
    elif current_row in range(5, 9):
        print("======= Tavern =======")
        print("  __[___]__")
        print("  |       |")
        print("  |  |L|  |")
        print("  |__|_|__|")
        print("=======================")
    elif current_row in range(9, 13):
        print("===== Goblin King =====")
        print("  (\\_/)")
        print(" (*)_(*_)")
        print("  (/   \\)")
        print("========================")

def display_dialogue(character, dialogue, options, current_row):
    os.system('cls' if os.name == 'nt' else 'clear')
    display_visuals(current_row)
    print(f"{character}: {dialogue}")
    for i, option in enumerate(options, 1):
        print(f"({i}) {option}")

def play_game():
    current_row = 2
    while True:
        row_data = get_row(current_row)
        (
            character, dialogue, option_a, option_b, option_c,
            next_a, next_b, next_c
        ) = row_data

        options = [option for option in [option_a, option_b, option_c] if option]
        next_rows = [int(next_row) for next_row in [next_a, next_b, next_c] if next_row]

        display_dialogue(character, dialogue, options, current_row)

        if current_row in [10, 11, 12]:
            print("You finished the game!")
            break

        while True:
            user_choice = input("Choose an option (1, 2, or 3): ")
            if (
                user_choice.isdigit() and
                1 <= int(user_choice) <= len(options)
            ):
                current_row = next_rows[int(user_choice) - 1]
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    play_game()