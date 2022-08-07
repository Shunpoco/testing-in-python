import util

class FakeResponse:
    def __init__(self, status=200, body=""):
        self.status = status
        self.body = body


def test_build_message_success(monkeypatch):
    def fake_request():
        return FakeResponse()
    monkeypatch.setattr("util.make_request", fake_request)

    result = util.build_message()

    assert result["success"] is True
