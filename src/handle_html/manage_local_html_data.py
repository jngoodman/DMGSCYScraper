from src.handle_html.constants import HTML_KEYS
from src.handle_html.get_web_html_data import GetHTML
from os import path, remove


def check_for_local_data(path_=HTML_KEYS['band_collections']):
    """Checks for existing locally stored data. Otherwise, creates the data. Intended for use with stored HTML."""
    if path.isfile(path_):
        prompt_for_new_data()
    else:
        create_local_data()


def create_local_data():
    get_html = GetHTML()
    get_html.retrieve_html()
    get_html.save_html()


def remove_local_data(path_=HTML_KEYS['band_collections']):
    remove(path_)


def prompt_for_new_data():
    """Prompts if existing data found. User can request new data or use existing .txt file."""
    user_response = input("Local DMG SCY html found. Would you like to request new html? (Y/N): ").lower()
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
            continue
