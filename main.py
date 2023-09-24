from src import application


def main():
    app = application.create_app()
    app.run()


if __name__ == "__main__":
    main()
