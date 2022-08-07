from book import create_json_lines, Book
from unittest import mock

class TestBook(object):
    def test_create_json_lines(self):
        assert create_json_lines() == ['{"id": 1, "title": "hogehog"}']

    @mock.patch("book._read_books")
    def test_mock(sefl, mock_read_books):
        mock_read_books.return_value = [
            Book(id=1, title="桃太郎"),
            Book(id=2, title="きんたろう"),
            Book(id=3, title="Urashima Taro"),
            Book(id=4, title=""),
        ]


        assert create_json_lines() == [
            # タイトル: 桃太郎
            '{"id": 1, "title": "\\u6843\\u592a\\u90ce"}',
            # タイトル: きんたろう
            '{"id": 2, "title": "\\u304d\\u3093\\u305f\\u308d\\u3046"}',
            # タイトル: Urashima Tarō
            '{"id": 3, "title": "Urashima Taro"}',
            # タイトル: (なし)
            '{"id": 4, "title": ""}',
        ]

    @mock.patch("book._read_books")
    def test_mock_json(self, mock_read_books):
        mock_read_books.return_values = [
            Book(id=1, title="桃太郎"),
            Book(id=2, title="きんたろう"),
            Book(id=3, title="Urachima Taro"),
            Book(id=4, title=""),
        ]

        assert create_json_lines() == [
            '{"id": 1, "title": "桃太郎"}',
            '{"id": 2, "title": "きんたろう"}',
            '{"id": 3, "title": "Urachima Taro"}',
            '{"id": 4, "title": ""}',
        ]
