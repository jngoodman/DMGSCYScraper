DMGSCY_PATH = r'src/handle_sql/sql_database/dmgscy.db'
CUSTOM_COMMANDS_PATH = r'src/handle_sql/sql_commands/custom_commands/'


class Queries:
    ROOT = r"src/handle_sql/sql_commands/"
    CREATE_BAND_TABLE = r"src/handle_sql/sql_commands/create_band_table.sql"
    ADD_TO_BAND_TABLE = r"src/handle_sql/sql_commands/add_to_band_table.sql"
    SELECT_BAND_TABLE = r"src/handle_sql/sql_commands/select_band_table.sql"
    DROP_BAND_TABLE = r"src/handle_sql/sql_commands/drop_band_table.sql"
    SELECT_NAME_BAND_TABLE = r"src/handle_sql/sql_commands/select_name_band_table.sql"
    CREATE_FAVOURITES_TABLE = r"src/handle_sql/sql_commands/create_favourites_table.sql"
    ADD_TO_FAVOURITES_TABLE = r"src/handle_sql/sql_commands/add_to_favourites_table.sql"
    SELECT_FAVOURITES_TABLE = r"src/handle_sql/sql_commands/select_favourites_table.sql"
    REMOVE_FROM_FAVOURITES_TABLE = r"src/handle_sql/sql_commands/remove_from_favourites_table.sql"
    DROP_FAVOURITES_TABLE = r"src/handle_sql/sql_commands/drop_favourites_table.sql"

    class Partial:
        GET_ROW_FROM_BAND = r"src/handle_sql/sql_commands/merch_table_partials/get_row_from_band.sql"
        CREATE_MERCH_TABLE = r"src/handle_sql/sql_commands/merch_table_partials/create_merch_table.sql"
        SELECT_MERCH_TABLE = r"src/handle_sql/sql_commands/merch_table_partials/select_merch_table.sql"
        DROP_MERCH_TABLE = r"src/handle_sql/sql_commands/merch_table_partials/drop_merch_table.sql"
        ADD_TO_MERCH_TABLE = r"src/handle_sql/sql_commands/merch_table_partials/add_to_merch_table.sql"
