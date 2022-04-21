import json
from http import HTTPStatus
from operator import itemgetter
from typing import Any

from flask_restful import Resource, reqparse

from grpc_config.configuration_pb2 import addressData, address
from src.abstract_classes.grpc_translator import GrpcTranslator


class UserController(Resource):
    def __init__(self, stub: Any, translator: GrpcTranslator):
        self.__grpc_stub: Any = stub
        self.__translator: GrpcTranslator = translator

    def post(self):
        body: dict = validate_post()
        cep = itemgetter('zipCode')(body)

        print("=== Body received ===")
        print(json.dumps(body, indent=4))

        print("\n=== Requesting to gRPC Server ===")
        request: address = self.__translator.translate(**{"cep": cep})
        print(request)

        response: addressData = self.__grpc_stub.get_data(request)
        print("\n=== Response from gRPC Server ===")
        print(response)

        return {
            "message": "User successfully saved",
            "document": body.get("document")
        }, HTTPStatus.OK


def validate_post() -> dict:
    body = reqparse.RequestParser()

    body.add_argument(
        'name',
        required=True,
        type=str,
        help='Param is required and must be a valid string'
    )
    body.add_argument(
        'document',
        required=True,
        type=str,
        help='Param is required and must be a valid string'
    )
    body.add_argument(
        'number',
        required=True,
        type=str,
        help='Param is required and must be a valid string'
    )
    body.add_argument(
        'zipCode',
        required=True,
        type=str,
        help='Param is required and must be a valid string'
    )
    return body.parse_args()
