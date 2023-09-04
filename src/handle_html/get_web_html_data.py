from requests import get
from src.handle_html.constants import BAND_MERCH_URL, LOCAL_HTML_PATH


class GetHTML:

    def __init__(self):
        self.url: str = BAND_MERCH_URL
        self.url_content = None

    def retrieve_html(self):
        self.url_content = get(self.url).content

    def save_html(self):
        with open(LOCAL_HTML_PATH, 'wb') as file:
            file.write(self.url_content)
