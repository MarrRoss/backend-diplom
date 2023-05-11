from fastapi import APIRouter
from fastapi import Depends

from controllers.zip_codes import ZipCodeController
from di.markers import ZipCodeControllerMarker
from dto.zip_codes import GetZipCodeDTO

zip_code_router = APIRouter()


@zip_code_router.get("/zip_codes/{id_}", response_model=GetZipCodeDTO)
async def get_one_city(
    id_: int,
    controller: ZipCodeController = Depends(ZipCodeControllerMarker),
):
    return await controller.get_one_from_id(id_=id_)


@zip_code_router.get("/zip_codes", response_model=list[GetZipCodeDTO])
async def get_cities(
    controller: ZipCodeController = Depends(ZipCodeControllerMarker),
):
    return await controller.get_all()
