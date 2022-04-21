from grpc_config import configuration_pb2_grpc as pb2_grpc, configuration_pb2 as pb2
from src.grpc_configuration import configure_server


class Exchange(pb2_grpc.GetAddressDataServicer):
    def get_data(self, request, context):
        return pb2.addressData(**{"city": "Os", "zip_code": "", "street": "", "neighborhood": ""})


def main():
    server = configure_server(Exchange)
    print("Starting server...")

    server.start()
    print("Server started...")

    server.wait_for_termination()


if __name__ == '__main__':
    main()
