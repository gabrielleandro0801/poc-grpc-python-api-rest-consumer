from abc import ABC, abstractmethod
from typing import Tuple


class HttpClient(ABC):

    @abstractmethod
    def get(self, **kwargs) -> Tuple[dict, int]:
        pass
