from dto.customers_accounts import CreateCustomerAccountDTO
from dto.filters.paginate import BasePaginateDTO
from services.customers_accounts import CustomerAccountService


class CustomerAccountController:
    def __init__(self, service: CustomerAccountService):
        self.service = service

    async def get_one_from_id(self, id_: int):
        return await self.service.get_one(id_=id_)

    async def get_all(
        self,
        paginate: BasePaginateDTO,
    ):
        return await self.service.get_all(paginate=paginate)

    async def create_one(
        self,
        data: CreateCustomerAccountDTO,
    ):
        return await self.service.create_one(data=data)
