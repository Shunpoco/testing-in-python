import pytest

from utils import build_message

class FakeResponse:
    def __init__(self, status=200, body=""):
        self.status = status
        self.body = body

@pytest.fixture
def response():
    def apply(status=200, body=""):
        return FakeResponse(status=status, body=body)
    return apply

def test_build_message_success(response):
    result = build_message(response())

    assert result["success"] is True

def test_build_message_failure(response):
    result = build_message(response(400, "not allowed here!"))
    
    assert result["success"] is False
    assert result["error"] == "not allowed here!"
