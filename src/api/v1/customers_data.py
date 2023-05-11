from fastapi import APIRouter, Depends, Query
from pyfa_converter import PyFaDepends

from controllers.customers_data import CustomerDataController
from di.markers import CustomerDataControllerMarker
from dto.customers_data import GetCustomerDataDTO
from dto.customers_data import SmallGetCustomerDataDTO
from dto.customers_data import UpdateCustomerDataDTO
from dto.filters.paginate import BasePaginateDTO

customer_data_router = APIRouter()


@customer_data_router.get("/customers/{id_}", response_model=GetCustomerDataDTO)
async def get_one_city(
    id_: int,
    controller: CustomerDataController = Depends(CustomerDataControllerMarker),
):
    return await controller.get_one_from_id(id_=id_)


@customer_data_router.patch("/customers/{id_}", response_model=SmallGetCustomerDataDTO)
async def get_one_city(
    id_: int,
    data: UpdateCustomerDataDTO,
    controller: CustomerDataController = Depends(CustomerDataControllerMarker),
):
    return await controller.update_one(customer_id=id_, data=data)
