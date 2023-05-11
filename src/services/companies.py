from typing import Sequence

from db.repositories.base import BaseSession
from db.repositories.companies import CompanyRepository
from db.tables import Company
from db.utils.decorators.error_handler import orm_error_handler


class CompanyService:
    def __init__(
        self,
        session: BaseSession,
        company_repo: CompanyRepository,
    ):
        self.session = session
        self.company_repo = company_repo

    @orm_error_handler
    async def get_one(self, id_: int) -> Company:
        async with self.session.transaction():
            company = await self.company_repo.get_one(
                id_=id_,
            )
            return company

    @orm_error_handler
    async def get_all(
        self,
    ) -> Sequence[Company]:
        async with self.session.transaction():
            companies = await self.company_repo.get_all()
            return companies
