import pytest

from learn_docker_app.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


class TestResponse:
    def copy_cat_response(self, test_string: str):
        return f"/respond/{test_string}"

    @pytest.mark.parametrize("test_string", [
        "hi", "bye", "xxx", "123!", "-12312",
    ])
    def test_simple_response__simple_message(self, client, test_string):
        response = client.get(self.copy_cat_response(test_string))

        assert response.status_code == 200
        assert response.json == {'response': test_string}

    @pytest.mark.parametrize("test_string", [
        "../", "\\//..", "cd ..//",
    ])
    def test_simple_response__wrong_url(self, client, test_string):
        response = client.get(self.copy_cat_response(test_string))

        assert response.status_code == 404

    def test_server_hostname(self, client):
        response = client.get(f"/respond/hostname")

        assert response.status_code == 200
        assert response.json == {
            'hostname': 'TEST-HOSTNAME',
            'requester': 'TEST-REQUESTER',
        }