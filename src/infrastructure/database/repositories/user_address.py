from typing import Any

from src.abstract_classes.repository import Repository
from src.infrastructure.database.connection.db_connection import db


class UserAddressRepository(Repository):

    @staticmethod
    def save(item: Any) -> Any:
        db.session.add(item)
        db.session.commit()
        return item
