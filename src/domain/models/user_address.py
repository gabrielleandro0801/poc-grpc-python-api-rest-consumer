from src.infrastructure.database.connection.db_connection import db


class UserAddress(db.Model):
    __tablename__ = "user_address"

    document = db.Column('document', db.String(20), primary_key=True)
    name = db.Column('name', db.String(50), nullable=False)
    cep = db.Column('cep', db.String(9), nullable=False)
    city = db.Column('city', db.String(35), nullable=False)
    neighborhood = db.Column('neighborhood', db.String(35), nullable=False)
    street = db.Column('street', db.String(75), nullable=False)
    number = db.Column('number', db.String(7), nullable=False)

    def __init__(self, **kwargs) -> None:
        self.document = kwargs.get('document')
        self.name = kwargs.get('name')
        self.cep = kwargs.get('cep')
        self.city = kwargs.get('city')
        self.neighborhood = kwargs.get('neighborhood')
        self.street = kwargs.get('street')
        self.number = kwargs.get('number')

    def to_json(self) -> dict:
        return {
            "document": self.document,
            "name": self.name,
            "cep": self.cep,
            "city": self.city,
            "neighborhood": self.neighborhood,
            "street": self.street,
            "number": self.number
        }
