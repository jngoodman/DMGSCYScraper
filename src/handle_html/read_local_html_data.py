from bs4 import BeautifulSoup
from src.handle_html.constants import BAND_COLLECTIONS_PATH, BASE_URL


class HandleLocalHTML:
    """Handles a locally stored HTML file. Default is band_collections_path."""

    def __init__(self, path=BAND_COLLECTIONS_PATH):
        self.path = path
        self.html_binary = None
        self.bs_object = None
        self.html_element_list: list = []

    def get_html_binary(self):
        """Reads http .txt file stored in path as binary."""
        with open(self.path, 'rb') as file:
            self.html_binary = file.read()

    def parse_html_binary(self):
        """Parses http binary into BeautifulSoup object."""
        self.bs_object = BeautifulSoup(self.html_binary, "html.parser")

    def retrieve_html_list_by_class(self, tag: str, class_: str):
        """Constructs iterable of http elements by tag and class_."""
        self.html_element_list = self.bs_object.find_all(tag, class_=class_)

    def retrieve_html_list_by_id(self, tag: str, id_: str):
        """Constructs iterable of http elements by tag and class_."""
        self.html_element_list = self.bs_object.find_all(tag, id=id_)


class HandleBandHTML(HandleLocalHTML):
    """Child class of HandleLocalHTML specifically for handling the band page HTML."""

    def __init__(self):
        super().__init__()
        self.bands_dictionary: dict = {}

    def _retrieve_band_names_from_list(self):
        """Retrieves names of bands from iterable of http elements by recovering strings."""
        band_name_list = []
        for http in self.html_element_list:
            band_name_list.append(http.text.strip())
        return band_name_list

    def _retrieve_band_urls_from_list(self):
        """Retrieves urls of bands from iterable of http elements by recovering href."""
        collection_url_list = []
        for http in self.html_element_list:
            partial_url = http["href"]
            full_url = f"{BASE_URL}{partial_url}"
            collection_url_list.append(full_url)
        return collection_url_list

    def construct_bands_dictionary(self):
        """Zips names and urls into dictionary."""
        self.bands_dictionary = dict(zip(self._retrieve_band_names_from_list(),
                                         self._retrieve_band_urls_from_list()))

    def run(self):
        """Runs functions in order to recover bands dictionary."""
        self.get_html_binary()
        self.parse_html_binary()
        self.retrieve_html_list_by_class(tag='a', class_="instant-brand-text-link")
        self.construct_bands_dictionary()
