from abc import ABC, abstractmethod
from typing import Tuple, Any


class GrpcTranslator(ABC):

    @staticmethod
    @abstractmethod
    def translate(**kwargs) -> Any:
        pass
