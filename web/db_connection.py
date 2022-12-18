"""Database Connection."""
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

db_host = os.getenv("db_host")
db_port = os.getenv("db_port")
db_user = os.getenv("db_user")
db_pass = os.getenv("db_pass")
db_name = os.getenv("db_name")


def get_connection():
    """get_connection

    Returns:
        _type_: _description_
    """

    conn = psycopg2.connect(
        host=db_host, port=db_port, user=db_user, password=db_pass, dbname=db_name
    )
    cursor = conn.cursor()

    return conn, cursor


def get_data(query):
    """_summary_

    Args:
        query (_type_): _description_
        cursor (_type_): _description_

    Returns:
        _type_: _description_
    """

    conn, cursor = get_connection()

    cursor.execute(query)

    columns = [col.name for col in cursor.description]
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return columns, data
