from requests import get
from os import path, remove
from src.pull_html.constants import BASE_PATH


class GetHTML:
    _url: str
    _html_path: str

    def __init__(self, url: str, file_name: str):
        """Acceptable html_keys in HTML_KEYS."""
        self._url = url
        self._html_path = f"{BASE_PATH}{file_name}"

    def check_if_file_exists(self):
        """Checks for existing locally stored data. Otherwise, creates the data. Intended for use with stored HTML."""
        if path.isfile(self._html_path):
            self.prompt_overwrite()
        else:
            self.save_html()

    def get_html(self):
        return get(self._url).content

    def save_html(self):
        with open(self._html_path, 'wb') as file:
            file.write(self.get_html())

    def delete_html(self):
        remove(self._html_path)

    def prompt_overwrite(self):
        """Prompts if existing data found. User can request new data or use existing .txt file."""
        while True:
            user_response = input(f"File {self._html_path} found. Overwrite? (Y/N)").lower()
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
