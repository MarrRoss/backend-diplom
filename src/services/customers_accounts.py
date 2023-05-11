from typing import Sequence
from db.repositories.base import BaseSession
from db.repositories.customers_accounts import CustomerAccountRepository
from db.tables import CustomerAccount
from db.utils.decorators.error_handler import orm_error_handler
from dto.customers_accounts import CreateCustomerAccountDTO
from dto.filters.paginate import BasePaginateDTO


class CustomerAccountService:
    def __init__(
        self,
        session: BaseSession,
        account_repo: CustomerAccountRepository,
    ):
        self.session = session
        self.account_repo = account_repo

    @orm_error_handler
    async def get_one(self, id_: int) -> CustomerAccount:
        async with self.session.transaction():
            account = await self.account_repo.get_one(
                id_=id_,
            )
            return account

    @orm_error_handler
    async def get_all(
        self,
        paginate: BasePaginateDTO,
    ) -> Sequence[CustomerAccount]:
        async with self.session.transaction():
            accounts = await self.account_repo.get_all(
                limit=paginate.limit,
                offset=paginate.offset,
            )
            return accounts

    @orm_error_handler
    async def create_one(
        self,
        data: CreateCustomerAccountDTO,
    ):
        async with self.session.transaction() as t:
            product_vendor = await self.account_repo.add_one(
                first_name=data.first_name,
                last_name=data.last_name,
                register_name=data.register_name,
                comment=data.comment,
            )
            await t.commit()
            return product_vendor
