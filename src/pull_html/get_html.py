from requests import get, exceptions
from os import path, remove
from src.pull_html.constants import HTML_FILES


class GetHTML:
    _url: str
    _html_path: str

    def __init__(self, file_name: str, url: str):
        """Acceptable html_keys in HTML_KEYS."""
        self._url = url
        self._html_path = f"{HTML_FILES}{file_name}"

    def overwrite_html(self):
        """Checks for existing locally stored data. Otherwise, creates the data. Intended for use with stored HTML."""
        if path.isfile(self._html_path):
            self.delete_html()
        self._save_html()

    def _get_html(self):
        try:
            return get(self._url).content
        except exceptions.RequestException:
            print("Connection error. Locally stored HTML will be used if available. Otherwise, data not available.")

    def _save_html(self):
        with open(self._html_path, 'wb') as file:
            file.write(self._get_html())

    def delete_html(self):
        remove(self._html_path)
