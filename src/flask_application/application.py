from flask import Flask, render_template
from src.data_services import SQLService, create_storage_directories
from src.handle_sql.constants import DMGSCY_PATH


def instantiate_mainpage():
    service = SQLService(database_file=DMGSCY_PATH, return_=True)
    service.create_table()
    service.fill_table()
    return service.select_table()


def instantiate_collection(name: str):
    service = SQLService(database_file=DMGSCY_PATH, return_=True, band_name=name)
    service.create_table()
    service.fill_table()
    return service.select_table()


def store_merch_instantiation(name: str) -> str:
    return f'instantiate_collection("{name}")'


def create_app():
    create_storage_directories()
    app = Flask(__name__)

    @app.route("/")
    def main_page():
        data = instantiate_mainpage()
        return render_template('mainpage.html', data=data)

    @app.route("/collection/<name>")
    def merch_page(name):
        data = eval(store_merch_instantiation(name))
        return render_template('collection.html', data=data)

    return app
