class BookNotFound(Exception):
    """Raises exception when isbn of the book is not found in db or in openlibrary website
    I knooow it's better to have different exceptions here :)"""
    status_code = 400

    def __init__(self, payload=None):
        Exception.__init__(self)
        self.message = "Book is not found"
        self.status_code = 404
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

