from fastapi import APIRouter
from fastapi import Depends

from controllers.countries import CountryController
from di.markers import CountryControllerMarker
from dto.countries import GetCountryDTO

country_router = APIRouter()


@country_router.get("/countries/{id_}", response_model=GetCountryDTO)
async def get_one_city(
    id_: int,
    controller: CountryController = Depends(CountryControllerMarker),
):
    return await controller.get_one_from_id(id_=id_)


@country_router.get("/countries", response_model=list[GetCountryDTO])
async def get_cities(
    controller: CountryController = Depends(CountryControllerMarker),
):
    return await controller.get_all()
