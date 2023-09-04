from bs4 import BeautifulSoup
from src.handle_html.constants import LOCAL_HTML_PATH, COLLECTION_BASE_URL


class HandleLocalHTML:

    def __init__(self):
        self.html_binary = None
        self.bs_object = None
        self.band_html_list: list = []
        self.bands_dictionary: dict = {}

    def get_html_binary(self):
        """Reads http .txt file stored in LOCAL_HTTP_PATH as binary."""
        with open(LOCAL_HTML_PATH, 'rb') as file:
            self.html_binary = file.read()

    def parse_html_binary(self):
        """Parses http binary into BeautifulSoup object."""
        self.bs_object = BeautifulSoup(self.html_binary, "html.parser")

    def retrieve_band_html_list(self):
        """Constructs iterable of http elements containing band names and links."""
        self.band_html_list = self.bs_object.find_all("a", class_="instant-brand-text-link")

    def _retrieve_band_names_from_list(self):
        """Retrieves names of bands from iterable of http elements by recovering strings."""
        band_name_list = []
        for http in self.band_html_list:
            band_name_list.append(http.text.strip())
        return band_name_list

    def _retrieve_band_urls_from_list(self):
        """Retrieves urls of bands from iterable of http elements by recovering href."""
        collection_url_list = []
        for http in self.band_html_list:
            partial_url = http["href"]
            full_url = f"{COLLECTION_BASE_URL}{partial_url}"
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
        self.retrieve_band_html_list()
        self.construct_bands_dictionary()

