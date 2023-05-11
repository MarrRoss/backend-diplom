from typing import Any
from typing import Sequence

from db.repositories.base import BaseSession
from db.repositories.cities import CityRepository
from db.repositories.companies import CompanyRepository
from db.repositories.countries import CountryRepository
from db.repositories.customers_accounts_relations import (
    AccountCustomerRelationRepository,
)
from db.repositories.customers_data import CustomerDataRepository
from db.repositories.phones import PhoneRepository
from db.repositories.states import StateRepository
from db.repositories.streets import StreetRepository
from db.repositories.zip_codes import ZipCodeRepository
from db.tables import CustomerData
from db.utils.decorators.error_handler import orm_error_handler
from dto.customers_data import CreateCustomerDataDTO
from dto.filters.paginate import BasePaginateDTO


class CustomerDataService:
    def __init__(
        self,
        session: BaseSession,
        customer_data_repo: CustomerDataRepository,
        company_repo: CompanyRepository,
        city_repo: CityRepository,
        phone_repo: PhoneRepository,
        zip_code_repo: ZipCodeRepository,
        country_repo: CountryRepository,
        street_repo: StreetRepository,
        state_repo: StateRepository,
        a_c_relation_repo: AccountCustomerRelationRepository,
    ):
        self.session = session
        self.customer_data_repo = customer_data_repo
        self.company_repo = company_repo
        self.city_repo = city_repo
        self.phone_repo = phone_repo
        self.zip_code_repo = zip_code_repo
        self.country_repo = country_repo
        self.street_repo = street_repo
        self.state_repo = state_repo
        self.a_c_relation_repo = a_c_relation_repo

    @orm_error_handler
    async def get_customers_from_account_id(self, account_id: int):
        async with self.session.transaction():
            return await self.a_c_relation_repo.get_all(
                account_id=account_id,
            )

    @orm_error_handler
    async def get_one(self, id_: int) -> CustomerData:
        async with self.session.transaction():
            city = await self.customer_data_repo.get_one(
                id_=id_,
            )
            return city

    @orm_error_handler
    async def get_all(
        self,
        account_id: int,
    ) -> Sequence[CustomerData]:
        async with self.session.transaction():
            cities = await self.customer_data_repo.get_all(
                account_id=account_id,
            )
            return cities

    # noinspection Duplicates
    @orm_error_handler
    async def add_one(
        self, account_id: int, data: CreateCustomerDataDTO
    ) -> CustomerData:
        async with self.session.transaction() as t:
            if await self.company_repo.exists(name=data.company):
                company = await self.company_repo.get_one_from_name(name=data.company)
            else:
                company = await self.company_repo.add_one(name=data.company)

            if await self.city_repo.exists(name=data.city):
                city = await self.city_repo.get_one_from_name(name=data.city)
            else:
                city = await self.city_repo.add_one(name=data.city)

            if await self.phone_repo.exists(name=data.phone):
                phone = await self.phone_repo.get_one_from_name(name=data.phone)
            else:
                phone = await self.phone_repo.add_one(name=data.phone)

            if await self.zip_code_repo.exists(name=data.zip):
                zip_code = await self.zip_code_repo.get_one_from_name(name=data.zip)
            else:
                zip_code = await self.zip_code_repo.add_one(name=data.zip)

            if await self.country_repo.exists(name=data.country):
                country = await self.country_repo.get_one_from_name(name=data.country)
            else:
                country = await self.country_repo.add_one(name=data.country)

            if await self.street_repo.exists(name=data.street):
                street = await self.street_repo.get_one_from_name(name=data.street)
            else:
                street = await self.street_repo.add_one(name=data.street)

            if await self.state_repo.exists(name=data.state):
                state = await self.state_repo.get_one_from_name(name=data.state)
            else:
                state = await self.state_repo.add_one(name=data.state)

            if await self.customer_data_repo.exists(
                first_name=data.first_name,
                last_name=data.last_name,
                register_name=data.register_name,
                company_id=company.id,
                country_id=country.id,
                street_id=street.id,
                city_id=city.id,
                zip_id=zip_code.id,
                state_id=state.id,
                phone_id=phone.id,
            ):
                customer_data = await self.customer_data_repo.get_one_from_params(
                    first_name=data.first_name,
                    last_name=data.last_name,
                    register_name=data.register_name,
                    company_id=company.id,
                    country_id=country.id,
                    street_id=street.id,
                    city_id=city.id,
                    zip_id=zip_code.id,
                    state_id=state.id,
                    phone_id=phone.id,
                )
            else:
                customer_data = await self.customer_data_repo.add_one(
                    first_name=data.first_name,
                    last_name=data.last_name,
                    description=data.description,
                    register_name=data.register_name,
                    company_id=company.id,
                    country_id=country.id,
                    street_id=street.id,
                    city_id=city.id,
                    zip_id=zip_code.id,
                    state_id=state.id,
                    phone_id=phone.id,
                )
            if not await self.a_c_relation_repo.exists(
                customer_id=customer_data.id,
                account_id=account_id,
            ):
                await self.a_c_relation_repo.add_one(
                    customer_id=customer_data.id,
                    account_id=account_id,
                )
            await t.commit()
            return customer_data

    @orm_error_handler
    async def update_one(
        self,
        customer_id: int,
        data: dict[str, Any]
    ):
        async with self.session.transaction() as t:
            result = await self.customer_data_repo.update_one(
                customer_id=customer_id,
                data=data,
            )
            await t.commit()
            return result

