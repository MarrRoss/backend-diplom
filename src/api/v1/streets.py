from fastapi import APIRouter
from fastapi import Depends

from controllers.streets import StreetController
from di.markers import StreetControllerMarker
from dto.streets import GetStreetDTO

street_router = APIRouter()


@street_router.get("/streets/{id_}", response_model=GetStreetDTO)
async def get_one_city(
    id_: int,
    controller: StreetController = Depends(StreetControllerMarker),
):
    return await controller.get_one_from_id(id_=id_)


@street_router.get("/streets", response_model=list[GetStreetDTO])
async def get_cities(
    controller: StreetController = Depends(StreetControllerMarker),
):
    return await controller.get_all()
