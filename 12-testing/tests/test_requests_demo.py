# contents of test_app.py, a simple test for our API retrieval
# import requests for the purposes of monkeypatching
import pytest
import requests

# custom class to be the mock return value
# will override the requests.Response returned from requests.get
from simple import requests_demo


class MockResponse:

    # mock json() method always returns a specific testing dictionary
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


# monkeypatched requests.get moved to a fixture
@pytest.fixture
def mock_response(monkeypatch):
    """Requests.get() mocked to return {'mock_key':'mock_response'}."""

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)


# notice our test uses the custom fixture instead of monkeypatch directly
@pytest.mark.usefixtures("mock_response")
def test_get_json(mock_response):
    result = requests_demo.get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"

def test_get_json2(monkeypatch):

    # Any arguments may be passed and mock_get() will always return our
    # mocked object, which only has the .json() method.
    def mock_get(*args, **kwargs):
        return MockResponse()

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    # app.get_json, which contains requests.get, uses the monkeypatch
    result = requests_demo.get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"