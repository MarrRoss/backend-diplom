from dto.filters.paginate import BasePaginateDTO
from services.cities import CityService


class CityController:
    def __init__(self, service: CityService):
        self.service = service

    async def get_one_from_id(self, id_: int):
        return await self.service.get_one(id_=id_)

    async def get_all(
        self,
    ):
        return await self.service.get_all()
