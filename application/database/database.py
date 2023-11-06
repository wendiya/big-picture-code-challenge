from pathlib import Path

from loguru import logger
import sqlite3

from application.database.queries import CREATE_TABLE
from application.database.queries import INSERT_RECORDS


def create_database(path_to_database, table_name):
    """Establishes connection to SQLite database using sqlite3 module and creates table in it"""
    Path(path_to_database).touch()

    connection = sqlite3.connect(path_to_database)
    cursor = connection.cursor()

    try:
        cursor.execute(CREATE_TABLE.format(table_name))

    except:
        logger.warning(f'Table in database already exists')

    connection.commit()
    connection.close()


def insert_to_database(path_to_database, table_name,  content):
    """Establishes connection to SQLite database using sqlite3 module
    and inserts values to table with table_name"""
    Path(path_to_database).touch()

    connection = sqlite3.connect(path_to_database)
    cursor = connection.cursor()
    cursor.execute(INSERT_RECORDS.format(table_name), content)

    connection.commit()
    connection.close()


def create_system_model(database, table_name):
    """Creates database model and returns instance of it"""
    class SystemFormModel(database.Model):
        __tablename__ = table_name
        isbn = database.Column(database.String, primary_key=True)
        author = database.Column(database.String)
        title = database.Column(database.String)
        summary = database.Column(database.String)
        cover_url = database.Column(database.String)
    return SystemFormModel


