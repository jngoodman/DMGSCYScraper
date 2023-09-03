from src.handle_http.constants import LOCAL_HTTP_PATH
from src.handle_http.get_web_http_data import GetHTTP
from os import path, remove


def check_for_local_data():
    if path.isfile(LOCAL_HTTP_PATH):
        prompt_for_new_data()
    else:
        create_local_data()


def create_local_data():
    get_http = GetHTTP()
    get_http.retrieve_http()
    get_http.save_http()


def remove_local_data():
    remove(LOCAL_HTTP_PATH)


def prompt_for_new_data():
    """Prompts if existing data found. User can request new data or use existing .txt file."""
    user_response = input("Local DMG SCY data found. Would you like to request new data? (Y/N): ").lower()
    awaiting_response = True
    while awaiting_response:
        if user_response == 'y':
            print("Requesting new data...")
            remove_local_data()
            create_local_data()
            awaiting_response = False
        elif user_response == 'n':
            print("Using existing data...")
            awaiting_response = False
        else:
            print("Invalid response. Please try again.")
