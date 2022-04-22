from typing import Any

from flask_restful import Api

from src.controllers.user import UserController
from src.infrastructure.database.repositories.user_address import UserAddressRepository
from src.infrastructure.translators.grpc.request import GrpcRequestTranslator
from src.infrastructure.translators.models.user_address_translator import UserAddressTranslator


def add(api: Api, stub: Any) -> Api:
    api.add_resource(
        UserController,
        '/v1/users',
        resource_class_kwargs={
            'stub': stub,
            'grpc_translator': GrpcRequestTranslator,
            'model_translator': UserAddressTranslator,
            'repository': UserAddressRepository
        }
    )

    return api
