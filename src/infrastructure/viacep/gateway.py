from http import HTTPStatus

from src.abstract_classes.http_client import HttpClient


class ViacepGateway:
    def __init__(self, client: HttpClient):
        self.__client: HttpClient = client

    def get_address(self, cep: str) -> dict:
        body, status_code = self.__client.get(cep=cep)

        if status_code != HTTPStatus.OK:
            raise Exception("Viacep unavailable at the moment")

        return body
