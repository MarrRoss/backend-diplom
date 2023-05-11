from typing import Sequence

from db.repositories.base import BaseSession
from db.repositories.countries import CountryRepository
from db.tables import Country
from db.utils.decorators.error_handler import orm_error_handler


class CountryService:
    def __init__(
        self,
        session: BaseSession,
        country_repo: CountryRepository,
    ):
        self.session = session
        self.country_repo = country_repo

    @orm_error_handler
    async def get_one(self, id_: int) -> Country:
        async with self.session.transaction():
            street = await self.country_repo.get_one(
                id_=id_,
            )
            return street

    @orm_error_handler
    async def get_all(
        self,
    ) -> Sequence[Country]:
        async with self.session.transaction():
            streets = await self.country_repo.get_all()
            return streets
