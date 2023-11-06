"""Contains SQL queries to database"""

CREATE_TABLE = '''CREATE TABLE {}(
                isbn TEXT PRIMARY KEY,
                author TEXT NOT NULL,
                title TEXT NOT NULL,
                summary TEXT NOT NULL,
                cover_url TEXT NOT NULL);
                '''

INSERT_RECORDS = "INSERT INTO {} (isbn, author, title, summary, cover_url) " \
                     "VALUES (:isbn, :author, :title, :summary, :cover_url)"


