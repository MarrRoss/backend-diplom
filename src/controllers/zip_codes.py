from services.zip_codes import ZipCodeService


class ZipCodeController:
    def __init__(self, service: ZipCodeService):
        self.service = service

    async def get_one_from_id(self, id_: int):
        return await self.service.get_one(id_=id_)

    async def get_all(
        self,
    ):
        return await self.service.get_all()
