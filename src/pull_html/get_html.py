from requests import get
from src.pull_html.constants import HTML_KEYS
from os import path, remove


class GetHTML:
    _url: str
    _html_key: str

    def __init__(self, url: str, html_key: str):
        """Acceptable html_keys in HTML_KEYS."""
        self._url = url
        self._html_key = html_key

    def check_if_file_exists(self):
        """Checks for existing locally stored data. Otherwise, creates the data. Intended for use with stored HTML."""
        if path.isfile(self._html_key):
            self.prompt_overwrite()
        else:
            self.save_html()

    def get_html(self):
        return get(self._url).content

    def save_html(self):
        with open(self._html_key, 'wb') as file:
            file.write(self.get_html())

    def delete_html(self):
        remove(self._html_key)

    def prompt_overwrite(self):
        """Prompts if existing data found. User can request new data or use existing .txt file."""
        while True:
            user_response = input(f"File {self._html_key} found. Overwrite? (Y/N)").lower()
            if user_response == 'y':
                print("Overwriting...")
                self.delete_html()
                self.save_html()
                break
            elif user_response == 'n':
                print("Using existing data...")
                break
            else:
                print("Invalid response.")
