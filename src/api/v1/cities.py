from fastapi import APIRouter
from fastapi import Depends

from controllers.cities import CityController
from di.markers import CityControllerMarker
from dto.cities import GetCityDTO

city_router = APIRouter()


@city_router.get("/cities/{id_}", response_model=GetCityDTO)
async def get_one_city(
    id_: int,
    controller: CityController = Depends(CityControllerMarker),
):
    return await controller.get_one_from_id(id_=id_)


@city_router.get("/cities", response_model=list[GetCityDTO])
async def get_cities(
    controller: CityController = Depends(CityControllerMarker),
):
    return await controller.get_all()
