from operator import itemgetter

from grpc_config import configuration_pb2 as pb2
from src.abstract_classes.grpc_translator import GrpcTranslator


class GrpcResponseTranslator(GrpcTranslator):

    @staticmethod
    def translate(**kwargs):
        city, zip_code, street, neighborhood = itemgetter('localidade', 'cep', 'logradouro', 'bairro')(kwargs)
        return pb2.addressData(
            city=city,
            zip_code=zip_code,
            street=street,
            neighborhood=neighborhood
        )
