from src.pull_html import ReadHTML, BASE_URL, BAND_COLLECTIONS_URL, BAND_COLLECTIONS_FILENAME, \
    GetHTML
from src.data_services.constants import BandCollectionsStrings, BandMerchStrings


def gen_html_filename(band: str):
    return f"{band.lower()}.txt"


class HTMLService:
    _html_reader: ReadHTML

    def __init__(self, file_name: str, url: str):
        self._html_reader = ReadHTML(file_name)
        self.html_getter = GetHTML(url=url, file_name=file_name)

    @staticmethod
    def get_text_from_element_list(element_list):
        text_list = []
        for html in element_list:
            text_list.append(html.text.strip())
        return text_list

    @staticmethod
    def get_urls_from_element_list(element_list: list, **kwargs):
        """kwargs: partial: bool, tag: str, base_url: str"""
        url_list = []
        if 'partial' not in kwargs or kwargs['partial'] == False:
            for html in element_list:
                url_list.append(html[kwargs['tag']])
            return url_list
        for html in element_list:
            partial_url = html[kwargs['tag']]
            full_url = f"{kwargs['base_url']}{partial_url}"
            url_list.append(full_url)
        return url_list


class CollectionsHTMLService(HTMLService):

    def __init__(self, file_name: str = BAND_COLLECTIONS_FILENAME, url: str = BAND_COLLECTIONS_URL):
        super().__init__(file_name, url)

    def return_band_names(self):
        html_reader = self._html_reader
        element_list = html_reader.retrieve_html_list_by_class(tag=BandCollectionsStrings.ELEMENT_TAG,
                                                               class_=BandCollectionsStrings.ELEMENT_CLASS)
        return self.get_text_from_element_list(element_list)

    def return_band_urls(self):
        html_reader = self._html_reader
        element_list = html_reader.retrieve_html_list_by_class(tag=BandCollectionsStrings.ELEMENT_TAG,
                                                               class_=BandCollectionsStrings.ELEMENT_CLASS)
        return self.get_urls_from_element_list(element_list, tag=BandCollectionsStrings.URL_TAG,
                                               partial=True, base_url=BASE_URL)

    def return_names_urls_dict(self):
        names = self.return_band_names()
        urls = self.return_band_urls()
        return dict(zip(names, urls))

    def return_names_urls_list(self):
        sequence = []
        for name, url in self.return_names_urls_dict().items():
            sequence.append([name, url])
        return sequence


class MerchHTMLService(HTMLService):

    def __init__(self, band_name: str, band_url: str):
        super().__init__(file_name=gen_html_filename(band_name),
                         url=band_url)
        self.html_getter = GetHTML(url=band_url, file_name=gen_html_filename(band_name))

    def _return_product_names(self):
        html_reader = self._html_reader
        element_list = html_reader.retrieve_html_list_by_class(tag=BandMerchStrings.NAME_TAG,
                                                               class_=BandMerchStrings.NAME_CLASS)
        return self.get_text_from_element_list(element_list)

    def _return_product_prices(self):
        html_reader = self._html_reader
        element_list = html_reader.retrieve_html_list_by_class(tag=BandMerchStrings.IMAGE_PRICE_TAG,
                                                               class_=BandMerchStrings.PRICE_CLASS)
        return self.get_text_from_element_list(element_list)

    def _return_product_images(self):
        html_reader = self._html_reader
        element_list = html_reader.retrieve_html_list_by_class(tag=BandMerchStrings.IMAGE_PRICE_TAG,
                                                               class_=BandMerchStrings.IMAGE_CLASS)
        image_list = []
        for element in element_list:
            image_data = element.find('noscript')
            image_src = image_data.find('img')['src']
            image_list.append(image_src)
        return image_list

    def return_names_images_prices_list(self):
        names_images_prices_list = []
        for item in self._return_product_names():
            index = self._return_product_names().index(item)
            names_images_prices_list.append([
                item,
                self._return_product_images()[index],
                self._return_product_prices()[index]
            ])
        return names_images_prices_list
