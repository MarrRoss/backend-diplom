from datetime import datetime
from typing import Optional
from dto.base import BaseSchema
from dto.cities import GetCityDTO
from dto.companies import GetCompanyDTO
from dto.countries import GetCountryDTO
from dto.phones import GetPhoneDTO
from dto.states import GetStateDTO
from dto.streets import GetStreetDTO
from dto.zip_codes import GetZipCodeDTO


class SmallGetCustomerDataDTO(BaseSchema):
    id: int
    first_name: str
    last_name: str
    register_name: str
    creating_date: datetime
    description: Optional[str] = None
    last_modified_date: datetime
    company_id: Optional[int] = None
    country_id: Optional[int] = None
    street_id: Optional[int] = None
    city_id: Optional[int] = None
    zip_id: Optional[int] = None
    state_id: Optional[int] = None
    phone_id: Optional[int] = None


class GetCustomerDataDTO(BaseSchema):
    id: int
    first_name: str
    last_name: str
    register_name: str
    creating_date: datetime
    description: Optional[str] = None
    last_modified_date: datetime
    company: Optional[GetCompanyDTO] = None
    country: GetCountryDTO
    street: GetStreetDTO
    city: GetCityDTO
    zip: GetZipCodeDTO
    state: Optional[GetStateDTO] = None
    phone: Optional[GetPhoneDTO] = None


class CreateCustomerDataDTO(BaseSchema):
    first_name: str
    last_name: str
    register_name: str
    description: Optional[str] = None
    company: str
    country: str
    street: str
    city: str
    zip: str
    state: str
    phone: str
    email: str


class UpdateCustomerDataDTO(BaseSchema):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    register_name: Optional[str] = None
    description: Optional[str] = None
    company_id: Optional[int] = None
    country_id: Optional[int] = None
    street_id: Optional[int] = None
    city_id: Optional[int] = None
    zip_id: Optional[int] = None
    state_id: Optional[int] = None
    phone_id: Optional[int] = None
