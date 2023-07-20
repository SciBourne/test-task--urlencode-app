import pytest
from httpx import Response

from fastapi import status
from fastapi.testclient import TestClient

from test_task_urlencode.app import build_app
from core.encode_types import EnumEncodeType


@pytest.mark.api
@pytest.mark.urlencode
class TestURLEncode:

    API_PREFIX = "/api/v1"
    ENDPOINT_ROUTE = f"{API_PREFIX}/urlencode"
    QUERY_SOURCE = "https://yandex.ru"

    @pytest.fixture
    def test_client(self):
        return TestClient(app=build_app())

    def test_query_source(self, test_client):
        url_request = f"{self.ENDPOINT_ROUTE}?source={self.QUERY_SOURCE}"
        response: Response = test_client.get(url_request)

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            "encoded_url": "https%3A%2F%2Fyandex.ru",
            "encode_type": EnumEncodeType.percent
        }

    def test_query_source_query_percent_type(self, test_client):
        url_request = (
            f"{self.ENDPOINT_ROUTE}?source={self.QUERY_SOURCE}"
            "&encode_type=percent"
        )

        response: Response = test_client.get(url_request)

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            "encoded_url": "https%3A%2F%2Fyandex.ru",
            "encode_type": EnumEncodeType.percent
        }

    def test_query_source_query_base64_type(self, test_client):
        url_request = (
            f"{self.ENDPOINT_ROUTE}?source={self.QUERY_SOURCE}"
            "&encode_type=base64"
        )

        response: Response = test_client.get(url_request)

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            "encoded_url": "aHR0cHM6Ly95YW5kZXgucnU=",
            "encode_type": EnumEncodeType.base64
        }
