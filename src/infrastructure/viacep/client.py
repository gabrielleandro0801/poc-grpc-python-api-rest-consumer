from http import HTTPStatus
from typing import Tuple

import requests

from src.abstract_classes.http_client import HttpClient


class ViacepClient(HttpClient):
    def __init__(self, url: str, timeout: float = 10):
        self.__base_url: str = url
        self.__timeout: float = timeout

    def get(self, **kwargs) -> Tuple[dict, int]:
        url: str = f"{self.__base_url}/{kwargs.get('cep')}/json"

        try:
            response = requests.get(url, timeout=self.__timeout)
            return response.json(), response.status_code
        except requests.Timeout:
            return {}, HTTPStatus.GATEWAY_TIMEOUT
