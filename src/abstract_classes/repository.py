from abc import ABC, abstractmethod
from typing import Any


class Repository(ABC):

    @staticmethod
    @abstractmethod
    def save(item: Any) -> Any:
        pass
