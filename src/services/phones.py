from typing import Sequence

from db.repositories.base import BaseSession
from db.repositories.phones import PhoneRepository
from db.tables import Phone
from db.utils.decorators.error_handler import orm_error_handler


class PhoneService:
    def __init__(
        self,
        session: BaseSession,
        phone_repo: PhoneRepository,
    ):
        self.session = session
        self.phone_repo = phone_repo

    @orm_error_handler
    async def get_one(self, id_: int) -> Phone:
        async with self.session.transaction():
            phone = await self.phone_repo.get_one(
                id_=id_,
            )
            return phone

    @orm_error_handler
    async def get_all(
        self,
    ) -> Sequence[Phone]:
        async with self.session.transaction():
            phones = await self.phone_repo.get_all()
            return phones
