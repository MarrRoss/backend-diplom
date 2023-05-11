from dto.editions import CreateEditionDTO
from services.editions import ProductEditionService


class ProductEditionController:
    def __init__(self, service: ProductEditionService):
        self.service = service

    async def get_one_from_id(self, id_: int):
        return await self.service.get_one(id_=id_)

    async def get_all(
        self,
    ):
        return await self.service.get_all()

    async def create_one(
        self,
        data: CreateEditionDTO,
    ):
        return await self.service.create_one(data=data)
