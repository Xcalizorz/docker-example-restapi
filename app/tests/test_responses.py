import pytest

from app.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


class TestResponse:
    @pytest.mark.parametrize("test_string", [
        "hi", "bye", "xxx", "123!", "-12312",
    ])
    def test_simple_response__simple_message(self, client, test_string):
        response = client.get(f"/respond/{test_string}")

        assert response.status_code == 200
        assert response.json == {'response': test_string}

    @pytest.mark.parametrize("test_string", [
        "../", "\\//..", "cd ..//",
    ])
    def test_simple_response__wrong_url(self, client, test_string):
        response = client.get(f"/respond/{test_string}")

        assert response.status_code == 404
