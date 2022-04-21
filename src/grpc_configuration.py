from concurrent import futures
from typing import Any

import grpc

from grpc_config import configuration_pb2_grpc as pb2_grpc

MAX_WORKERS: int = 10


def configure_client() -> Any:
    channel: grpc.Channel = grpc.insecure_channel("localhost:50061")
    return pb2_grpc.GetAddressDataStub(channel)


def configure_server(exchange: Any) -> Any:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_WORKERS))
    pb2_grpc.add_GetAddressDataServicer_to_server(exchange(), server)

    server.add_insecure_port("[::]:50061")
    return server
