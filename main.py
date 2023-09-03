from src.handle_http_data import HandleLocalHTTP, check_for_local_data


def main():
    check_for_local_data()
    http_handle_instance = HandleLocalHTTP()
    http_handle_instance.run()
    print(http_handle_instance.bands_dictionary)


if __name__ == "__main__":
    main()
