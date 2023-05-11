import datetime
import io
import os

from docxtpl import DocxTemplate

from dto.orders import CreateOrderDTO
from services.customers_accounts import CustomerAccountService
from services.customers_data import CustomerDataService
from services.orders import OrderService
from utils.folders_path import get_parent_path
from utils.temp_files import GenerateTempFileDepends


class OrderController:
    def __init__(
        self,
        order_service: OrderService,
        customer_service: CustomerDataService,
        account_service: CustomerAccountService,
    ):
        self.order_service = order_service
        self.customer_service = customer_service
        self.account_service = account_service

    async def get_one_from_id(self, id_: int):
        return await self.order_service.get_one(id_=id_)

    async def get_all(
        self,
        account_id: int,
        only_basic: bool = True,
    ):
        customers = await self.customer_service.get_customers_from_account_id(
            account_id=account_id,
        )
        customers_ids = [i.customer_id for i in customers]
        return await self.order_service.get_all(
            customers_ids=customers_ids,
            only_basic=only_basic,
        )

    async def get_upgrades(
        self,
        order_id: int,
    ):
        return await self.order_service.get_upgrades(order_id=order_id)

    async def create_one(
        self,
        account_id: int,
        data: CreateOrderDTO,
    ):
        customer = await self.customer_service.add_one(
            account_id=account_id,
            data=data.customer,
        )
        order = await self.order_service.add_one(
            customer_id=customer.id,
            data=data,
        )
        return order

    async def export_by_id(self, account_id: int, order_id: int):
        account = await self.account_service.get_one(
            id_=account_id,
        )
        order = await self.order_service.get_one(id_=order_id)

        temp_file = GenerateTempFileDepends(cleanup=True)()
        source_folder = os.path.abspath(os.path.join(__file__, "../../.."))

        document = DocxTemplate(f"{source_folder}/static/templates/order.docx")
        document.render(
            {
                "OrderId": order.id,
                "Date": order.date.strftime("%d-%M-%Y %H:%M:%S"),
                "AccountFirstName": account.first_name,
                "AccountLastName": account.last_name,
                "AccountRegisterName": account.register_name,
                "CustomerFirstName": order.customer.first_name,
                "CustomerLastName": order.customer.last_name,
                "CustomerRegisterName": order.customer.register_name,
                "StreetName": order.customer.street.name,
                "CountryName": order.customer.country.name,
                "StateName": order.customer.state.name,
                "ZipCodeName": order.customer.zip.name,
                "CustomerPhone": order.customer.phone.name,
                "PaymentTypeName": order.payment_type.name,
                "PreviousOrderId": order.previous_order_id,
                "ProductName": order.product.name,
                "ProductVersion": order.product.version,
                "ProductPreviousVersion": order.product.previous_version,
                "ProductPlatformId": order.product.platform_id,
                "ProductGroupName": order.product.product_group.name,
                "ProductTypeName": order.product.product_type.name,
                "ProductEditionName": order.product.edition.name,
                "ProductVendorName": order.product.vendor.name,
                "KeyName": order.key.key,
                "LicenseCount": order.num_license,
                "KeyCreatingDate": order.key.creating_date.strftime("%d-%M-%Y %H:%M:%S"),
                "KeyExpirationDate": order.key.expiration_date.strftime("%d-%M-%Y %H:%M:%S") if
                order.key.expiration_date else '-',
                "KeyIsActive": "Да" if order.key.is_active else "Нет"
            }
        )

        file_stream = io.BytesIO()
        document.save(file_stream)
        file_stream.seek(0)

        temp_file.write(file_stream.read())
        return temp_file
