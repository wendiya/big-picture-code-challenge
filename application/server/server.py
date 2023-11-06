"""Contains class to manage requests to web server and requests to database"""
import os

from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from loguru import logger
import requests

from application.server.exceptions import BookNotFound
from application.database.database import create_system_model
from application.database.database import insert_to_database


class Server:
    """Keeps everything related to server and database in one place"""
    def __init__(self, path_to_database, table_name):
        self._app = Flask(__name__)
        self._system_model = None
        self._database = None
        self._table_name = table_name
        self._path_to_database = path_to_database

    @property
    def app(self):
        """Returns app variable to main.py where we can start web server"""
        return self._app

    def define_database_configurations(self):
        """Defines path to database and secret key for it"""
        self._app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{self._path_to_database}'
        self._app.config['SECRET_KEY'] = os.urandom(32)

    def connect_to_database(self):
        """Creates instance of SQLAlchemy extension, which allows to work with db in Flask app"""
        self._database = SQLAlchemy()
        self._database.init_app(self._app)


        self._system_model = create_system_model(database=self._database, # Creates custom SQLAlchemy model for db
                                                 table_name=self._table_name)
        with self._app.app_context():
            self._database.create_all()

    def define_server_routers(self):
        """Defines routes fro web server which will be used for making requests to web server"""
        @self._app.route('/books', methods=['GET'])
        def get_all_books():
            """Returns all books stored in db"""
            books = self._system_model.query.all()
            book_list = []
            for book in books:
                book_list.append(book.isbn)
            return jsonify({'books': book_list}), 200

        @self._app.route('/isbn/<isbn>', methods=['GET'])
        def get_book_by_isbn(isbn):
            """Returns book information from db by it's isbn number"""
            # there should be validator for isbn
            book = self._system_model.query.filter_by(isbn=isbn).first()
            if book is None:
                raise BookNotFound()
            else:
                response = {"isbn": book.isbn,
                                     "author": book.author,
                                     "title": book.title,
                                     "summary": book.summary,
                                     "cover_url": book.cover_url}
                return jsonify(response), 200

        @self._app.route('/books', methods=['POST'])
        def add_book_by_isbn():
            """Adds book to db from openlibrary website by it's isbn number"""
            # there should be validator for isbn
            request_data = request.get_json()
            if 'isbn' not in request_data:
                return jsonify({"error": f"isbn is missing in body of request"}), 400

            isbn = request_data['isbn']
            book_info = get_book_info_by_isbn(isbn)
            insert_to_database(path_to_database=self._path_to_database,
                               table_name=self._table_name,
                               content=book_info)
            if book_info is None:
                raise BookNotFound()

            response = {"success": f"book with isbn={isbn} is added to library"}
            return jsonify(response), 200


def get_book_info_by_isbn(isbn):
    """Makes get request to openlibrary website to get book info by it's isbn number"""
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&jscmd=data&format=json"
    response = requests.get(url)
    book_info = response.json()[f"ISBN:{isbn}"]
    return {"isbn": isbn,
            "author": book_info["authors"][0]["name"],
            "title": book_info["title"],
            "summary": "summary", # this one confused me
            "cover_url": book_info["cover"]["small"]}




