import json
from http import HTTPStatus
from operator import itemgetter
from typing import Any

from flask_restful import Resource, reqparse

from grpc_config.configuration_pb2 import addressData, address
from src.abstract_classes.grpc_translator import GrpcTranslator
from src.abstract_classes.repository import Repository
from src.domain.models.user_address import UserAddress
from src.infrastructure.translators.models.user_address_translator import UserAddressTranslator


class UserController(Resource):
    def __init__(self, stub: Any, grpc_translator: GrpcTranslator, model_translator: UserAddressTranslator,
                 repository: Repository):
        self.__grpc_stub: Any = stub
        self.__grpc_translator: GrpcTranslator = grpc_translator
        self.__model_translator: UserAddressTranslator = model_translator
        self.__repository: Repository = repository

    def post(self):
        body: dict = validate_post()
        cep = itemgetter('zipCode')(body)

        print("=== Body received ===")
        print(json.dumps(body, indent=4))

        print("\n=== Requesting to gRPC Server ===")
        request: address = self.__grpc_translator.translate(**{"cep": cep})
        print(request)

        response: addressData = self.__grpc_stub.get_data(request)
        print("\n=== Response from gRPC Server ===")
        print(response)

        inserted_item: UserAddress = self.__repository.save(
            self.__model_translator.translate_request(
                document=body.get("document"),
                name=body.get("name"),
                cep=cep,
                city=response.city,
                neighborhood=response.neighborhood,
                street=response.street,
                number=body.get("number")
            )
        )

        return {
            "message": "User successfully saved",
            **inserted_item.to_json()
        }, HTTPStatus.CREATED


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
