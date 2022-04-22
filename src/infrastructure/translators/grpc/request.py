from grpc_config import configuration_pb2 as pb2
from src.abstract_classes.grpc_translator import GrpcTranslator


class GrpcRequestTranslator(GrpcTranslator):

    @staticmethod
    def translate(**kwargs):
        return pb2.address(zip_code=kwargs.get("cep"))
