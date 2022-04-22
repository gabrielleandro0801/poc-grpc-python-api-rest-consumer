from src.domain.models.user_address import UserAddress


class UserAddressTranslator:

    @staticmethod
    def translate_request(**kwargs) -> UserAddress:
        return UserAddress(
            document=kwargs.get("document"),
            name=kwargs.get("name"),
            cep=kwargs.get("cep"),
            city=kwargs.get("city"),
            neighborhood=kwargs.get("neighborhood"),
            street=kwargs.get("street"),
            number=kwargs.get("number")
        )
