from requests import get
from src.handle_html.constants import BAND_COLLECTIONS_URL, BAND_COLLECTIONS_PATH


class GetHTML:

    def __init__(self):
        self.url: str = BAND_COLLECTIONS_URL
        self.url_content = None

    def retrieve_html(self):
        self.url_content = get(self.url).content

    def save_html(self):
        with open(BAND_COLLECTIONS_PATH, 'wb') as file:
            file.write(self.url_content)
