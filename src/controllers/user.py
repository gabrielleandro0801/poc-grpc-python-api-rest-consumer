from typing import Any

from flask_restful import Resource, reqparse
from grpc_config import configuration_pb2 as pb2


class UserController(Resource):
    def __init__(self, stub: Any):
        self.__grpc_stub: Any = stub

    def post(self):
        body: dict = validate_post()

        cep: str = body.get("zipCode")
        request = pb2.address(zip_code=cep)

        response = self.__grpc_stub.get_data(request)
        return {}


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
        'zipCode',
        required=True,
        type=str,
        help='Param is required and must be a valid string'
    )
    return body.parse_args()
