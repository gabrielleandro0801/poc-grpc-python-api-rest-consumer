from typing import Any

from flask import Flask
from flask_restful import Api

from src import grpc_configuration
from src.routes import user_routes

app: Flask = Flask(__name__)
api: Api = Api(app)

stub: Any = grpc_configuration.configure_client()

api = user_routes.add(api, stub)

if __name__ == '__main__':
    app.run()
