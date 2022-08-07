import pytest

import util

class FakeResponse:
    def __init__(self, status=200, body=""):
        self.status = status
        self.body = body

@pytest.fixture(autouse=True)
def monkey_response(monkeypatch):
    def fake_request():
        return FakeResponse()
    monkeypatch.setattr(util, "make_request", fake_request)

def test_build_message_success():
    result = util.build_message()

    assert result["success"] is True
