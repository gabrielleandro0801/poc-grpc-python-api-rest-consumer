from typing import Any

from flask_restful import Api

from src.controllers.user import UserController
from src.infrastructure.translators.grpc.request import GrpcRequestTranslator


def add(api: Api, stub: Any) -> Api:
    api.add_resource(
        UserController,
        '/v1/users',
        resource_class_kwargs={
            'stub': stub,
            'translator': GrpcRequestTranslator
        }
    )

    return api
