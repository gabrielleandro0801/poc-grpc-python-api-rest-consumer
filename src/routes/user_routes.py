from typing import Any

from flask_restful import Api

from src.controllers.user import UserController


def add(api: Api, stub: Any) -> Api:
    api.add_resource(
        UserController,
        '/v1/users',
        resource_class_kwargs={
            'stub': stub
        }
    )

    return api
