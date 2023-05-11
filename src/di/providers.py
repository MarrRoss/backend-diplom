from fastapi import Depends

from controllers.cities import CityController
from controllers.companies import CompanyController
from controllers.countries import CountryController
from controllers.customers_accounts import CustomerAccountController
from controllers.customers_data import CustomerDataController
from controllers.editions import ProductEditionController
from controllers.orders import OrderController
from controllers.phones import PhoneController
from controllers.products import ProductController
from controllers.products_types import ProductTypeController
from controllers.products_vendors import ProductVendorController
from controllers.sources import SourceController
from controllers.states import StateController
from controllers.streets import StreetController
from controllers.zip_codes import ZipCodeController
from db.repositories.base import BaseSession
from db.repositories.cities import CityRepository
from db.repositories.companies import CompanyRepository
from db.repositories.countries import CountryRepository
from db.repositories.customers_accounts import CustomerAccountRepository
from db.repositories.customers_accounts_relations import (
    AccountCustomerRelationRepository,
)
from db.repositories.customers_data import CustomerDataRepository
from db.repositories.editions import ProductEditionRepository
from db.repositories.orders import OrderRepository
from db.repositories.phones import PhoneRepository
from db.repositories.products import ProductRepository
from db.repositories.products_types import ProductTypeRepository
from db.repositories.products_vendors import ProductVendorRepository
from db.repositories.sources import SourceRepository
from db.repositories.states import StateRepository
from db.repositories.streets import StreetRepository
from db.repositories.zip_codes import ZipCodeRepository
from di.factory import ConfigFactory, EngineFactory, SessionFactory
from di.markers import *
from services.cities import CityService
from services.companies import CompanyService
from services.countries import CountryService
from services.customers_accounts import CustomerAccountService
from services.customers_data import CustomerDataService
from services.editions import ProductEditionService
from services.orders import OrderService
from services.phones import PhoneService
from services.products import ProductService
from services.products_types import ProductTypeService
from services.products_vendors import ProductVendorService
from services.products_vendors import ProductVendorService
from services.sources import SourceService
from services.states import StateService
from services.streets import StreetService
from services.zip_codes import ZipCodeService
from settings.postgres import SettingsPostgres


class FastAPIDependenciesProvider:
    def __init__(self, config: ConfigFactory):
        self.config = config

        self.async_engine_factory = EngineFactory(config=config.postgres, mode="async")
        self.async_session_factory = SessionFactory(
            engine=self.async_engine_factory.engine
        )

    def get_async_engine_factory(self) -> EngineFactory:
        return self.async_engine_factory

    def get_session_factory(self) -> SessionFactory:
        return self.async_session_factory

    def get_settings_postgres(self) -> SettingsPostgres:
        return self.config.postgres

    @staticmethod
    def get_db_session(
        session: SessionFactory = Depends(SessionFactoryMarker),
    ):
        return BaseSession(db_session=session.session_factory)

    @staticmethod
    def get_city_service(
        session: BaseSession = Depends(BaseSessionMarker),
    ) -> CityService:
        return CityService(
            session=session,
            city_repo=CityRepository(db_session=session.session),
        )

    @staticmethod
    def get_city_controller(
        service: CityService = Depends(CityServiceMarker),
    ):
        return CityController(
            service=service,
        )

    @staticmethod
    def get_source_service(
        session: BaseSession = Depends(BaseSessionMarker),
    ) -> SourceService:
        return SourceService(
            session=session,
            source_repo=SourceRepository(db_session=session.session),
        )

    @staticmethod
    def get_source_controller(
        service: SourceService = Depends(SourceServiceMarker),
    ):
        return SourceController(
            service=service,
        )

    @staticmethod
    def get_customer_data_service(
        session: BaseSession = Depends(BaseSessionMarker),
    ) -> CustomerDataService:
        return CustomerDataService(
            session=session,
            customer_data_repo=CustomerDataRepository(db_session=session.session),
            company_repo=CompanyRepository(db_session=session.session),
            city_repo=CityRepository(db_session=session.session),
            phone_repo=PhoneRepository(db_session=session.session),
            zip_code_repo=ZipCodeRepository(db_session=session.session),
            country_repo=CountryRepository(db_session=session.session),
            street_repo=StreetRepository(db_session=session.session),
            state_repo=StateRepository(db_session=session.session),
            a_c_relation_repo=AccountCustomerRelationRepository(
                db_session=session.session
            ),
        )

    @staticmethod
    def get_customer_data_controller(
        service: CustomerDataService = Depends(CustomerDataServiceMarker),
    ):
        return CustomerDataController(
            service=service,
        )

    @staticmethod
    def get_product_type_service(
        session: BaseSession = Depends(BaseSessionMarker),
    ) -> ProductTypeService:
        return ProductTypeService(
            session=session,
            source_repo=ProductTypeRepository(db_session=session.session),
        )

    @staticmethod
    def get_product_type_controller(
        service: ProductTypeService = Depends(ProductTypeServiceMarker),
    ):
        return ProductTypeController(
            service=service,
        )

    @staticmethod
    def get_product_vendor_service(
        session: BaseSession = Depends(BaseSessionMarker),
    ) -> ProductVendorService:
        return ProductVendorService(
            session=session,
            vendor_repo=ProductVendorRepository(db_session=session.session),
        )

    @staticmethod
    def get_product_vendor_controller(
        service: ProductVendorService = Depends(ProductVendorServiceMarker),
    ):
        return ProductVendorController(
            service=service,
        )

    @staticmethod
    def get_product_edition_service(
        session: BaseSession = Depends(BaseSessionMarker),
    ) -> ProductEditionService:
        return ProductEditionService(
            session=session,
            edition_repo=ProductEditionRepository(db_session=session.session),
        )

    @staticmethod
    def get_product_edition_controller(
        service: ProductEditionService = Depends(ProductEditionServiceMarker),
    ):
        return ProductEditionController(
            service=service,
        )

    @staticmethod
    def get_customer_account_service(
        session: BaseSession = Depends(BaseSessionMarker),
    ) -> CustomerAccountService:
        return CustomerAccountService(
            session=session,
            account_repo=CustomerAccountRepository(db_session=session.session),
        )

    @staticmethod
    def get_customer_account_controller(
        service: CustomerAccountService = Depends(CustomerAccountServiceMarker),
    ):
        return CustomerAccountController(
            service=service,
        )

    @staticmethod
    def get_product_service(
        session: BaseSession = Depends(BaseSessionMarker),
    ) -> ProductService:
        return ProductService(
            session=session,
            product_repo=ProductRepository(db_session=session.session),
        )

    @staticmethod
    def get_product_controller(
        service: ProductService = Depends(ProductServiceMarker),
    ):
        return ProductController(
            service=service,
        )

    @staticmethod
    def get_order_service(
        session: BaseSession = Depends(BaseSessionMarker),
    ) -> OrderService:
        return OrderService(
            session=session,
            order_repo=OrderRepository(db_session=session.session),
        )

    @staticmethod
    def get_order_controller(
        order_service: OrderService = Depends(OrderServiceMarker),
        customer_service: CustomerDataService = Depends(CustomerDataServiceMarker),
        account_service: CustomerAccountService = Depends(CustomerAccountServiceMarker),
    ):
        return OrderController(
            order_service=order_service,
            customer_service=customer_service,
            account_service=account_service,
        )

    @staticmethod
    def get_company_service(
        session: BaseSession = Depends(BaseSessionMarker),
    ) -> CompanyService:
        return CompanyService(
            session=session,
            company_repo=CompanyRepository(db_session=session.session),
        )

    @staticmethod
    def get_company_controller(
        service: CompanyService = Depends(CompanyServiceMarker),
    ):
        return CompanyController(
            service=service,
        )

    @staticmethod
    def get_country_service(
        session: BaseSession = Depends(BaseSessionMarker),
    ) -> CountryService:
        return CountryService(
            session=session,
            country_repo=CountryRepository(db_session=session.session),
        )

    @staticmethod
    def get_country_controller(
        service: CountryService = Depends(CountryServiceMarker),
    ):
        return CountryController(
            service=service,
        )

    @staticmethod
    def get_street_service(
        session: BaseSession = Depends(BaseSessionMarker),
    ) -> StreetService:
        return StreetService(
            session=session,
            street_repo=StreetRepository(db_session=session.session),
        )

    @staticmethod
    def get_street_controller(
        service: StreetService = Depends(StreetServiceMarker),
    ):
        return StreetController(
            service=service,
        )

    @staticmethod
    def get_zip_code_service(
        session: BaseSession = Depends(BaseSessionMarker),
    ) -> ZipCodeService:
        return ZipCodeService(
            session=session,
            zip_code_repo=ZipCodeRepository(db_session=session.session),
        )

    @staticmethod
    def get_zip_code_controller(
        service: ZipCodeService = Depends(ZipCodeServiceMarker),
    ):
        return ZipCodeController(
            service=service,
        )

    @staticmethod
    def get_state_service(
        session: BaseSession = Depends(BaseSessionMarker),
    ) -> StateService:
        return StateService(
            session=session,
            state_repo=StateRepository(db_session=session.session),
        )

    @staticmethod
    def get_state_controller(
        service: StateService = Depends(StateServiceMarker),
    ):
        return StateController(
            service=service,
        )

    @staticmethod
    def get_phone_service(
        session: BaseSession = Depends(BaseSessionMarker),
    ) -> PhoneService:
        return PhoneService(
            session=session,
            phone_repo=PhoneRepository(db_session=session.session),
        )

    @staticmethod
    def get_phone_controller(
        service: PhoneService = Depends(PhoneServiceMarker),
    ):
        return PhoneController(
            service=service,
        )
