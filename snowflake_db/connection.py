import snowflake.connector


def get_connection():
    conn = snowflake.connector.connect(
        user="PURVAJA510",
        password="Purvajadodke@1234",
        account="ALHXHWY-BD79190",
        warehouse="COMPUTE_WH",
        database="ATMOSYNC_DB",
        schema="RAW",
        role="ACCOUNTADMIN"
    )

    return conn