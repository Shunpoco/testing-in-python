from collections import namedtuple
import json

class Book(namedtuple("Book", ["id", "title"])):
    def as_json(self):
        return json.dumps(dict(id=self.id, title=self.title))

def _read_books():
    return [Book(id=1, title="hogehog")]

def create_json_lines():
    return [b.as_json() for b in _read_books()]

