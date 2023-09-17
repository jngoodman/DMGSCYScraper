from src.pull_html import ReadHTML, BASE_URL, COLLECTIONS_URL, COLLECTIONS_FILENAME, GetHTML
from src.data_services.constants import HTMLStrings


def gen_html_filename(band: str):
    return f"{band.lower()}.txt"


class HTMLService:
    _html_reader: ReadHTML
    _html_getter: GetHTML

    def __init__(self, file_name: str, file_url: str):
        self._html_reader = ReadHTML(file_name)
        self._html_getter = GetHTML(file_name, file_url)

    def get_html_elements(self, tag: str, class_: str):
        html_reader = self._html_reader
        html_elements = html_reader.retrieve_html_list_by_class(tag, class_)
        return html_elements

    def return_text(self, tag: str, class_: str):
        html_elements = self.get_html_elements(tag, class_)
        text_list = [element.text.strip() for element in html_elements]
        return text_list


class HTMLCollServ(HTMLService):
    html_strings = HTMLStrings.COLLECTIONS

    def __init__(self):
        super().__init__(COLLECTIONS_FILENAME, COLLECTIONS_URL)

    def return_urls(self, tag=html_strings['tag'], class_=html_strings['class'], url=html_strings['url']):
        html_elements = self.get_html_elements(tag, class_)
        url_list = [f"{BASE_URL}{element[url]}" for element in html_elements]
        return url_list

    def return_names_urls_list(self, tag=html_strings['tag'], class_=html_strings['class'], url=html_strings['url']):
        url_list = self.return_urls(tag, class_, url)
        name_list = self.return_text(tag, class_)
        return zip(name_list, url_list)


class HTMLMerchServ(HTMLService):
    name_strings = HTMLStrings.PRODUCT_NAME
    image_strings = HTMLStrings.PRODUCT_IMAGE
    price_strings = HTMLStrings.PRODUCT_PRICE

    def __init__(self, band_name: str, band_url: str):
        super().__init__(file_name=gen_html_filename(band_name), file_url=band_url)

    def _parse_image_source(self, tag=image_strings['tag'], class_=image_strings['class']):
        [data_tag, image_tag, src_tag] = [self.image_strings['image_data'], self.image_strings['image'],
                                          self.image_strings['image_source']]
        image_element_list = self.get_html_elements(tag, class_)
        image_data_list = [element.find(data_tag) for element in image_element_list]
        image_source_list = [element.find(image_tag)[src_tag] for element in image_data_list]
        return image_source_list

    def return_names_images_prices_list(self):
        name_list = self.return_text(self.name_strings['tag'], self.name_strings['class'])
        price_list = self.return_text(self.price_strings['tag'], self.price_strings['class'])
        image_list = self._parse_image_source()
        return zip(name_list, image_list, price_list)
