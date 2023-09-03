from requests import get
from src.handle_http_data.constants import BAND_MERCH_URL, LOCAL_HTTP_PATH


class GetHTTP:

    def __init__(self):
        self.url: str = BAND_MERCH_URL
        self.url_content = None

    def retrieve_http(self):
        self.url_content = get(self.url).content

    def save_http(self):
        with open(LOCAL_HTTP_PATH, 'wb') as file:
            file.write(self.url_content)
