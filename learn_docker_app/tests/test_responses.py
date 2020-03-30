import pytest
from dataclasses import dataclass
from types import SimpleNamespace

from learn_docker_app.app import create_app
from learn_docker_app.api.respond import platform
from learn_docker_app.api.respond import request


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

    def test_hostname(self, client, monkeypatch):
        monkeypatch.setattr('learn_docker_app.api.respond.platform', MockPlatform)
        monkeypatch.setattr('learn_docker_app.api.respond.request', MockRequest)

        response = client.get(f"/respond/hostname")

        assert response.status_code == 200
        assert response.json == {
            'host': {
                'hostname_or_ip': 'TEST-HOSTNAME',
                'system': 'TEST-SYSTEM',
            },
            'client': {
                'hostname_or_ip': 'TEST-HOSTNAME-CLIENT',
                'system': 'TEST-SYSTEM-CLIENT',
            },
        }


class MockPlatform:
    """Will override the builtin platform module"""
    @staticmethod
    def node():
        return 'TEST-HOSTNAME'
    
    @staticmethod
    def system():
        return 'TEST-SYSTEM'


@dataclass
class MockRequest:
    """Will override the flask.request object"""
    user_agent = SimpleNamespace(platform='TEST-SYSTEM-CLIENT')
    remote_addr = 'TEST-HOSTNAME-CLIENT'
