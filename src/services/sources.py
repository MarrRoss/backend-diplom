from db.repositories.base import BaseSession
from db.repositories.sources import SourceRepository
from db.tables import Source
from db.utils.decorators.error_handler import orm_error_handler
from dto.filters.paginate import BasePaginateDTO


class SourceService:
    def __init__(
        self,
        session: BaseSession,
        source_repo: SourceRepository,
    ):
        self.session = session
        self.source_repo = source_repo

    @orm_error_handler
    async def get_one(self, id_: int) -> Source:
        async with self.session.transaction():
            city = await self.source_repo.get_one(
                id_=id_,
            )
            return city

    @orm_error_handler
    async def get_all(
        self,
        paginate: BasePaginateDTO,
    ):
        async with self.session.transaction():
            cities = await self.source_repo.get_all(
                limit=paginate.limit,
                offset=paginate.offset,
            )
            return cities
