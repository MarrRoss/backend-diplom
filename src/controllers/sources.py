from dto.filters.paginate import BasePaginateDTO
from services.sources import SourceService


class SourceController:
    def __init__(self, service: SourceService):
        self.service = service

    async def get_one_from_id(self, id_: int):
        return await self.service.get_one(id_=id_)

    async def get_all(
        self,
        paginate: BasePaginateDTO,
    ):
        return await self.service.get_all(
            paginate=paginate,
        )
