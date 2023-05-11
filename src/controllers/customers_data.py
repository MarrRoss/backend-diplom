from dto.customers_data import UpdateCustomerDataDTO
from dto.filters.paginate import BasePaginateDTO
from services.customers_data import CustomerDataService


class CustomerDataController:
    def __init__(self, service: CustomerDataService):
        self.service = service

    async def get_one_from_id(self, id_: int):
        return await self.service.get_one(id_=id_)

    async def get_all(
        self,
        account_id: int,
    ):
        return await self.service.get_all(
            account_id=account_id,
        )

    async def update_one(
        self,
        customer_id: int,
        data: UpdateCustomerDataDTO,
    ):
        print(f"{data=}")
        data_without_none = data.dict(exclude_none=True)
        print(f"{data_without_none=}")
        return await self.service.update_one(
            customer_id=customer_id,
            data=data_without_none,
        )
