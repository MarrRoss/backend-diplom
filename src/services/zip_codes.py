from typing import Sequence

from db.repositories.base import BaseSession
from db.repositories.zip_codes import ZipCodeRepository
from db.tables import ZipCode
from db.utils.decorators.error_handler import orm_error_handler


class ZipCodeService:
    def __init__(
        self,
        session: BaseSession,
        zip_code_repo: ZipCodeRepository,
    ):
        self.session = session
        self.zip_code_repo = zip_code_repo

    @orm_error_handler
    async def get_one(self, id_: int) -> ZipCode:
        async with self.session.transaction():
            zip_codes = await self.zip_code_repo.get_one(
                id_=id_,
            )
            return zip_codes

    @orm_error_handler
    async def get_all(
        self,
    ) -> Sequence[ZipCode]:
        async with self.session.transaction():
            zip_codes = await self.zip_code_repo.get_all()
            return zip_codes
