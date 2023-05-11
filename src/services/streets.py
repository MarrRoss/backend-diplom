from typing import Sequence

from db.repositories.base import BaseSession
from db.repositories.streets import StreetRepository
from db.tables import Street
from db.utils.decorators.error_handler import orm_error_handler


class StreetService:
    def __init__(
        self,
        session: BaseSession,
        street_repo: StreetRepository,
    ):
        self.session = session
        self.street_repo = street_repo

    @orm_error_handler
    async def get_one(self, id_: int) -> Street:
        async with self.session.transaction():
            street = await self.street_repo.get_one(
                id_=id_,
            )
            return street

    @orm_error_handler
    async def get_all(
        self,
    ) -> Sequence[Street]:
        async with self.session.transaction():
            streets = await self.street_repo.get_all()
            return streets
