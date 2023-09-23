from src import application

app = application.create_app()


def main():
    app.run()


if __name__ == "__main__":
    main()
