from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.repositories.base import BaseCRUD
from db.tables import CustomerAccount


class CustomerAccountRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.model = CustomerAccount
        self.base = BaseCRUD(db_session=db_session, model=self.model)

    async def get_one(self, id_: int) -> CustomerAccount:
        stmt = select(CustomerAccount).filter(CustomerAccount.id == id_)
        curr = await self.db_session.execute(statement=stmt)
        return curr.scalar_one()

    async def add_one(
        self, first_name: str, last_name: str, register_name: str, comment: str
    ) -> CustomerAccount:
        account = CustomerAccount(
            first_name=first_name,
            last_name=last_name,
            register_name=register_name,
            comment=comment,
        )
        self.db_session.add(account)
        await self.db_session.flush()
        return account

    async def get_all(
        self,
        limit: int = 10,
        offset: int = 0,
    ) -> Sequence[CustomerAccount]:
        stmt = select(CustomerAccount).limit(limit).offset(offset)
        curr = await self.db_session.execute(statement=stmt)
        return curr.scalars().all()
