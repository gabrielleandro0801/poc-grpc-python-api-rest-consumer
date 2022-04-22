from grpc_config.configuration_pb2 import addressData
from src.abstract_classes.grpc_translator import GrpcTranslator


class ViacepService:
    def __init__(self, gateway, translator):
        self.__gateway = gateway
        self.__translator: GrpcTranslator = translator

    def get_address(self, cep: str) -> addressData:
        response: dict = self.__gateway.get_address(cep)
        return self.__translator.translate(**response)
