from typing import Any

from grpc_config import configuration_pb2_grpc as pb2_grpc
from grpc_config.configuration_pb2 import addressData, address
from src.domain.services.viacep_service import ViacepService
from src.grpc_configuration import configure_server
from src.infrastructure.translators.grpc.response import GrpcResponseTranslator
from src.infrastructure.viacep.client import ViacepClient
from src.infrastructure.viacep.gateway import ViacepGateway


class Exchange(pb2_grpc.GetAddressDataServicer):
    def __init__(self, service):
        self.__viacep_service = service

    def get_data(self, request: address, context: Any) -> addressData:
        print("\n=== Request from gRPC Client received ===")
        print(request)

        address_data: addressData = self.__viacep_service.get_address(request.zip_code)
        print("=== Returning response to gRPC Client ===")

        print(address_data)
        return address_data


def create_exchange() -> Exchange:
    return Exchange(
        service=ViacepService(
            gateway=ViacepGateway(
                client=ViacepClient(
                    url="https://viacep.com.br/ws",
                    timeout=20
                )
            ),
            translator=GrpcResponseTranslator
        )
    )


def main():
    server = configure_server(create_exchange)
    print("Starting server...")

    server.start()
    print("Server started...")

    server.wait_for_termination()


if __name__ == '__main__':
    main()
