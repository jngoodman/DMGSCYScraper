DMGSCY_PATH = r'src/handle_sql/sql_database/dmgscy.db'
CUSTOM_COMMANDS_PATH = r'src/handle_sql/sql_commands/custom_commands/'


class Queries:
    CREATE_BAND_TABLE = r"src/handle_sql/sql_commands/create_band_table.sql"
    ADD_TO_BAND_TABLE = r"src/handle_sql/sql_commands/add_to_band_table.sql"
    SELECT_BAND_TABLE = r"src/handle_sql/sql_commands/select_band_table.sql"
    DROP_BAND_TABLE = r"src/handle_sql/sql_commands/drop_band_table.sql"
    SELECT_NAME_BAND_TABLE = r"src/handle_sql/sql_commands/select_name_band_table.sql"


QueryBases = {"get_row_from_band": r"src/handle_sql/sql_commands/merch_table_partials/get_row_from_band.sql",
              "create_merch_table": r"src/handle_sql/sql_commands/merch_table_partials/create_merch_table.sql",
              "select_merch_table": r"src/handle_sql/sql_commands/merch_table_partials/select_merch_table.sql",
              "drop_merch_table": r"src/handle_sql/sql_commands/merch_table_partials/drop_merch_table.sql"}
