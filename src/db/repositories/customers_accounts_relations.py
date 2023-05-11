from typing import Optional
from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from db.repositories.base import BaseCRUD
from db.tables import AccountCustomerRelation


class AccountCustomerRelationRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.model = AccountCustomerRelation
        self.base = BaseCRUD(db_session=db_session, model=self.model)

    async def add_one(
        self,
        account_id: int,
        customer_id: int,
    ) -> AccountCustomerRelation:
        account = AccountCustomerRelation(
            account_id=account_id,
            customer_id=customer_id,
        )
        self.db_session.add(account)
        await self.db_session.flush()
        return account

    async def exists(self, account_id: int, customer_id: int):
        return await self.base.exists(
            AccountCustomerRelation.account_id == account_id,
            AccountCustomerRelation.customer_id == customer_id,
        )

    async def get_all(
        self,
        account_id: Optional[int] = None,
        customer_id: Optional[int] = None,
    ) -> Sequence[AccountCustomerRelation]:
        if account_id:
            return await self.base.get_many(
                AccountCustomerRelation.account_id == account_id,
            )
        if customer_id:
            return await self.base.get_many(
                AccountCustomerRelation.customer_id == customer_id,
            )
