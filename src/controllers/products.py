from dto.products import CreateProductDTO
from services.products import ProductService


class ProductController:
    def __init__(self, service: ProductService):
        self.service = service

    async def get_one_from_id(self, id_: int):
        return await self.service.get_one(id_=id_)

    async def get_all(
        self,
    ):
        return await self.service.get_all()

    async def add_one(
        self,
        data: CreateProductDTO,
    ):
        return await self.service.add_one(data=data)
