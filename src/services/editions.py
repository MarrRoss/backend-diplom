from typing import Sequence

from db.repositories.base import BaseSession
from db.repositories.editions import ProductEditionRepository
from db.tables import Edition
from db.utils.decorators.error_handler import orm_error_handler
from dto.editions import CreateEditionDTO


class ProductEditionService:
    def __init__(
        self,
        session: BaseSession,
        edition_repo: ProductEditionRepository,
    ):
        self.session = session
        self.edition_repo = edition_repo

    @orm_error_handler
    async def create_one(
        self,
        data: CreateEditionDTO,
    ) -> Edition:
        async with self.session.transaction():
            edition = await self.edition_repo.add_one(
                name=data.name,
            )
            return edition

    @orm_error_handler
    async def get_one(self, id_: int) -> Edition:
        async with self.session.transaction():
            edition = await self.edition_repo.get_one(
                id_=id_,
            )
            return edition

    @orm_error_handler
    async def get_all(
        self,
    ) -> Sequence[Edition]:
        async with self.session.transaction():
            return await self.edition_repo.get_all()
