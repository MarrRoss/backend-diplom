from fastapi import APIRouter

from api.v1.cities import city_router
from api.v1.companies import company_router
from api.v1.countries import country_router
from api.v1.customers_accounts import customer_account
from api.v1.customers_data import customer_data_router
from api.v1.editions import product_edition
from api.v1.phones import phone_router
from api.v1.products import product_router
from api.v1.products_types import product_type
from api.v1.products_vendors import product_vendor
from api.v1.sources import source_router
from api.v1.states import state_router
from api.v1.streets import street_router
from api.v1.zip_codes import zip_code_router

own_router_v1 = APIRouter()
own_router_v1.include_router(city_router, tags=["City"])
own_router_v1.include_router(source_router, tags=["Source"])
own_router_v1.include_router(product_type, tags=["ProductType"])
own_router_v1.include_router(product_vendor, tags=["ProductVendor"])
own_router_v1.include_router(product_edition, tags=["ProductEdition"])
own_router_v1.include_router(customer_account, tags=["CustomerAccount"])
own_router_v1.include_router(product_router, tags=["Product"])
own_router_v1.include_router(customer_data_router, tags=["CustomerData"])
own_router_v1.include_router(company_router, tags=["Companies"])
own_router_v1.include_router(country_router, tags=["Countries"])
own_router_v1.include_router(street_router, tags=["Streets"])
own_router_v1.include_router(zip_code_router, tags=["ZipCode"])
own_router_v1.include_router(state_router, tags=["State"])
own_router_v1.include_router(phone_router, tags=["Phones"])
