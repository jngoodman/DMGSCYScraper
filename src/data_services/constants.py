class HTMLStrings:
    COLLECTIONS = {'tag': 'a', 'class': 'instant-brand-text-link', 'url': 'href'}
    PRODUCT_URL = {'tag': 'a', 'class': 'card__link', 'url': 'href'}
    PRODUCT_NAME = {'tag': 'h3', 'class': 'card__title'}
    PRODUCT_IMAGE = {'tag': 'div', 'class': 'card__image', 'image_data': 'noscript',
                     'image': 'img', 'image_source': 'src'}
    PRODUCT_PRICE = {'tag': 'div', 'class': 'product-price'}


class Dirs:
    HTML_FILES = r"src/pull_html/html_files/"
    SQL_FILES = r"src/handle_sql/sql_database/"
