from typing import Any

from flask import Flask
from flask_restful import Api

import src.infrastructure.database.connection.db_connection as database
from src import grpc_configuration
from src.routes import user_routes

app: Flask = Flask(__name__)
api: Api = Api(app)

stub: Any = grpc_configuration.configure_client()
database.start_connection(app)

api = user_routes.add(api, stub)

if __name__ == '__main__':
    app.run()
