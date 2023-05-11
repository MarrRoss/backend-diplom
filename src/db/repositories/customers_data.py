from typing import Any
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from db.repositories.base import BaseCRUD
from db.tables import AccountCustomerRelation
from db.tables import CustomerData


class CustomerDataRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.model = CustomerData
        self.base = BaseCRUD(db_session=db_session, model=self.model)

    async def get_one(self, id_: int) -> CustomerData:
        stmt = (
            select(CustomerData)
            .options(
                joinedload(CustomerData.company),
                joinedload(CustomerData.country),
                joinedload(CustomerData.street),
                joinedload(CustomerData.city),
                joinedload(CustomerData.zip),
                joinedload(CustomerData.state),
                joinedload(CustomerData.phone),
            )
            .filter(CustomerData.id == id_)
        )
        curr = await self.db_session.execute(statement=stmt)
        return curr.scalar_one()

    async def get_all(
        self,
        account_id: int,
    ) -> Sequence[CustomerData]:
        stmt_customers_id = (
            select(AccountCustomerRelation.customer_id)
            .filter(AccountCustomerRelation.account_id == account_id)
        ).scalar_subquery()

        stmt = (
            select(CustomerData)
            .options(
                joinedload(CustomerData.company),
                joinedload(CustomerData.country),
                joinedload(CustomerData.street),
                joinedload(CustomerData.city),
                joinedload(CustomerData.zip),
                joinedload(CustomerData.state),
                joinedload(CustomerData.phone),
            )
            .filter(CustomerData.id.in_(stmt_customers_id))
        )
        curr = await self.db_session.execute(statement=stmt)
        return curr.scalars().all()

    async def add_one(
        self,
        first_name: str,
        last_name: str,
        register_name: str,
        description: str,
        company_id: int,
        country_id: int,
        street_id: int,
        city_id: int,
        zip_id: int,
        state_id: int,
        phone_id: int,
    ) -> CustomerData:
        model = CustomerData(
            first_name=first_name,
            last_name=last_name,
            register_name=register_name,
            description=description,
            company_id=company_id,
            country_id=country_id,
            street_id=street_id,
            city_id=city_id,
            zip_id=zip_id,
            state_id=state_id,
            phone_id=phone_id,
        )
        self.db_session.add(model)
        await self.db_session.flush(objects=[model])
        return model

    async def exists(
        self,
        first_name: str,
        last_name: str,
        register_name: str,
        company_id: int,
        country_id: int,
        street_id: int,
        city_id: int,
        zip_id: int,
        state_id: int,
        phone_id: int,
    ):
        return await self.base.exists(
            CustomerData.first_name == first_name,
            CustomerData.last_name == last_name,
            CustomerData.register_name == register_name,
            CustomerData.company_id == company_id,
            CustomerData.country_id == country_id,
            CustomerData.street_id == street_id,
            CustomerData.city_id == city_id,
            CustomerData.zip_id == zip_id,
            CustomerData.state_id == state_id,
            CustomerData.phone_id == phone_id,
        )

    async def get_one_from_params(
        self,
        first_name: str,
        last_name: str,
        register_name: str,
        company_id: int,
        country_id: int,
        street_id: int,
        city_id: int,
        zip_id: int,
        state_id: int,
        phone_id: int,
    ) -> CustomerData:
        stmt = select(CustomerData).filter(
            CustomerData.first_name == first_name,
            CustomerData.last_name == last_name,
            CustomerData.register_name == register_name,
            CustomerData.company_id == company_id,
            CustomerData.country_id == country_id,
            CustomerData.street_id == street_id,
            CustomerData.city_id == city_id,
            CustomerData.zip_id == zip_id,
            CustomerData.state_id == state_id,
            CustomerData.phone_id == phone_id,
        )
        curr = await self.db_session.execute(statement=stmt)
        return curr.scalar_one()

    async def update_one(
        self,
        customer_id: int,
        data: dict[str, Any],
    ):
        return await self.base.update(
            CustomerData.id == customer_id,
            **data,
        )
