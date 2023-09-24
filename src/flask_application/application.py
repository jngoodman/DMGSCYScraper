from flask import Flask, render_template, redirect, url_for
from src.data_services import SQLService, create_storage_directories
from src.handle_sql import DMGSCY_PATH


def instantiate_mainpage():
    service = SQLService(database_file=DMGSCY_PATH, return_=True)
    service.create_table()
    service.add_to_table()
    return service.select_table()


def instantiate_collection(name: str):
    service = SQLService(database_file=DMGSCY_PATH, return_=True, band_name=name)
    service.create_table()
    service.add_to_table()
    return service.select_table()


def instantiate_favourites():
    service = SQLService(database_file=DMGSCY_PATH, return_=True, favourites=True)
    service.create_table()
    return service.select_table()


def store_merch_instantiation(name: str) -> str:
    return f'instantiate_collection("{name}")'


def create_app():
    create_storage_directories()
    app = Flask(__name__)

    @app.route("/")
    def main_page():
        all_bands = instantiate_mainpage()
        favourites = instantiate_favourites()
        return render_template('mainpage.html', data=all_bands, favourites=favourites)

    @app.route("/collection/<name>")
    def merch_page(name: str):
        data = eval(store_merch_instantiation(name))
        return render_template('collection.html', data=data)

    @app.route("/favourites/<name>")
    def add_to_favourites(name: str):
        service = SQLService(database_file=DMGSCY_PATH, return_=True, favourites=True)
        service.add_to_table([name])
        return redirect(url_for('main_page'))

    @app.route("/favourites_remove/<name>")
    def remove_from_favourites(name: str):
        service = SQLService(database_file=DMGSCY_PATH, return_=True, favourites=True)
        service.remove_from_table(name)
        return redirect(url_for('main_page'))

    return app
