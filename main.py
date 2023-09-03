from src import ManageDatabase, check_for_local_data


def main():
    check_for_local_data()
    manage_database = ManageDatabase()
    manage_database.create_database()
    manage_database.create_band_table()
    manage_database.add_to_band_table()


if __name__ == "__main__":
    main()
