import uuid

from fastapi import APIRouter, Depends
from fastapi import Query
from pyfa_converter import PyFaDepends
from starlette.responses import FileResponse
from starlette.responses import JSONResponse

from controllers.customers_accounts import CustomerAccountController
from controllers.customers_data import CustomerDataController
from controllers.orders import OrderController
from di.markers import CustomerAccountControllerMarker
from di.markers import CustomerDataControllerMarker
from di.markers import OrderControllerMarker
from dto.customers_accounts import CreateCustomerAccountDTO
from dto.customers_accounts import GetCustomerAccountDTO
from dto.customers_data import GetCustomerDataDTO
from dto.filters.paginate import BasePaginateDTO
from dto.orders import CreateOrderDTO
from dto.orders import GetOrderDTO
from dto.orders import GetSmallOrderDTO

customer_account = APIRouter()


@customer_account.get("/accounts/{id_}", response_model=GetCustomerAccountDTO)
async def get_one_edition(
    id_: int,
    controller: CustomerAccountController = Depends(CustomerAccountControllerMarker),
):
    return await controller.get_one_from_id(id_=id_)


@customer_account.get(
    "/accounts/{account_id}/customers",
    response_model=list[GetCustomerDataDTO]
)
async def get_customers_data(
    account_id: int,
    controller: CustomerDataController = Depends(CustomerDataControllerMarker),
):
    return await controller.get_all(account_id=account_id)


@customer_account.get("/accounts", response_model=list[GetCustomerAccountDTO])
async def get_all_editions(
    paginate: BasePaginateDTO = PyFaDepends(BasePaginateDTO, _type=Query),
    controller: CustomerAccountController = Depends(CustomerAccountControllerMarker),
):
    return await controller.get_all(paginate=paginate)


@customer_account.post("/accounts", response_model=GetCustomerAccountDTO)
async def create_one_edition(
    data: CreateCustomerAccountDTO,
    controller: CustomerAccountController = Depends(CustomerAccountControllerMarker),
):
    return await controller.create_one(data=data)


@customer_account.get("/accounts/{account_id}/orders", response_model=list[GetOrderDTO])
async def get_all_editions(
    account_id: int,
    only_basic: bool = Query(True),
    controller: OrderController = Depends(OrderControllerMarker),
):
    return await controller.get_all(
        account_id=account_id,
        only_basic=only_basic,
    )


@customer_account.get("/accounts/{account_id}/orders/{order_id}", response_model=GetOrderDTO)
async def get_one_order(
    account_id: int,
    order_id: int,
    controller: OrderController = Depends(OrderControllerMarker),
):
    return await controller.get_one_from_id(
        id_=order_id,
    )


@customer_account.get("/accounts/{account_id}/orders/{order_id}/export")
async def get_one_order(
    account_id: int,
    order_id: int,
    controller: OrderController = Depends(OrderControllerMarker),
):
    result = await controller.export_by_id(
        account_id=account_id,
        order_id=order_id,
    )
    return FileResponse(
        result.name,
        filename=f"{uuid.uuid4()}.docx",
        status_code=200,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )


@customer_account.get(
    "/accounts/{account_id}/orders/{order_id}/upgrades", response_model=list[GetOrderDTO]
)
async def get_all_editions(
    account_id: int,
    order_id: int,
    controller: OrderController = Depends(OrderControllerMarker),
):
    return await controller.get_upgrades(order_id=order_id)


@customer_account.post("/accounts/{account_id}/orders", response_model=GetSmallOrderDTO)
async def create_order(
    account_id: int,
    data: CreateOrderDTO,
    controller: OrderController = Depends(OrderControllerMarker),
):
    return await controller.create_one(
        account_id=account_id,
        data=data,
    )
