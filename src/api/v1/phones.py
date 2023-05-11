from fastapi import APIRouter
from fastapi import Depends

from controllers.phones import PhoneController
from di.markers import PhoneControllerMarker
from dto.phones import GetPhoneDTO

phone_router = APIRouter()


@phone_router.get("/phones/{id_}", response_model=GetPhoneDTO)
async def get_one_city(
    id_: int,
    controller: PhoneController = Depends(PhoneControllerMarker),
):
    return await controller.get_one_from_id(id_=id_)


@phone_router.get("/phones", response_model=list[GetPhoneDTO])
async def get_cities(
    controller: PhoneController = Depends(PhoneControllerMarker),
):
    return await controller.get_all()
