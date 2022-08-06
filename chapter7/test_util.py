import pytest

import util

class FakeResponse:
    def __init__(self, status=200):
        self.status = status

@pytest.fixture
def response():
    def apply(status=200):
        return FakeResponse(status=status)

    return apply

def test_build_message_success(response):
    result = util.build_message(response())
    assert result["success"] is True
