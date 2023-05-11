from di.factory import ConfigFactory
from di.markers import *
from di.providers import FastAPIDependenciesProvider


def fastapi_dependency_overrides(config: ConfigFactory):
    dependencies_provider = FastAPIDependenciesProvider(config)
    return {
        SettingsPostgresMarker: dependencies_provider.get_settings_postgres,
        AsyncEngineFactoryMarker: dependencies_provider.get_async_engine_factory,
        SessionFactoryMarker: dependencies_provider.get_session_factory,
        BaseSessionMarker: dependencies_provider.get_db_session,
        CityServiceMarker: dependencies_provider.get_city_service,
        CityControllerMarker: dependencies_provider.get_city_controller,
        SourceServiceMarker: dependencies_provider.get_source_service,
        SourceControllerMarker: dependencies_provider.get_source_controller,
        CustomerDataServiceMarker: dependencies_provider.get_customer_data_service,
        CustomerDataControllerMarker: dependencies_provider.get_customer_data_controller,
        ProductTypeServiceMarker: dependencies_provider.get_product_type_service,
        ProductTypeControllerMarker: dependencies_provider.get_product_type_controller,
        ProductVendorServiceMarker: dependencies_provider.get_product_vendor_service,
        ProductVendorControllerMarker: dependencies_provider.get_product_vendor_controller,
        ProductEditionServiceMarker: dependencies_provider.get_product_edition_service,
        ProductEditionControllerMarker: dependencies_provider.get_product_edition_controller,
        CustomerAccountServiceMarker: dependencies_provider.get_customer_account_service,
        CustomerAccountControllerMarker: dependencies_provider.get_customer_account_controller,
        ProductServiceMarker: dependencies_provider.get_product_service,
        ProductControllerMarker: dependencies_provider.get_product_controller,
        OrderServiceMarker: dependencies_provider.get_order_service,
        OrderControllerMarker: dependencies_provider.get_order_controller,
        CompanyServiceMarker: dependencies_provider.get_company_service,
        CompanyControllerMarker: dependencies_provider.get_company_controller,
        CountryServiceMarker: dependencies_provider.get_country_service,
        CountryControllerMarker: dependencies_provider.get_country_controller,
        StreetServiceMarker: dependencies_provider.get_street_service,
        StreetControllerMarker: dependencies_provider.get_street_controller,
        ZipCodeServiceMarker: dependencies_provider.get_zip_code_service,
        ZipCodeControllerMarker: dependencies_provider.get_zip_code_controller,
        StateServiceMarker: dependencies_provider.get_state_service,
        StateControllerMarker: dependencies_provider.get_state_controller,
        PhoneServiceMarker: dependencies_provider.get_phone_service,
        PhoneControllerMarker: dependencies_provider.get_phone_controller,
    }
