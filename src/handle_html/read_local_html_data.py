from bs4 import BeautifulSoup
from src.handle_html.constants import HTML_KEYS


class ReadHTML:
    _html_file: str
    _options: dict

    def __init__(self, html_key: str):
        self._html_file = HTML_KEYS[html_key]
        self.html_element_list = []

    def get_html_binary(self):
        """Reads http .txt file stored in path as binary."""
        with open(self._html_file, 'rb') as file:
            return file.read()

    def parse_html_binary(self):
        """Parses http binary into BeautifulSoup object."""
        return BeautifulSoup(self.get_html_binary(), "html.parser")

    def retrieve_html_list_by_class(self, tag: str, class_: str):
        """Constructs iterable of http elements by tag and class_."""
        return self.parse_html_binary().find_all(tag, class_=class_)

    def retrieve_html_list_by_id(self, tag: str, id_: str):
        """Constructs iterable of http elements by tag and class_."""
        return self.parse_html_binary().find_all(tag, id=id_)
