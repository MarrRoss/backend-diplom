from fastapi import APIRouter
from fastapi import Depends

from controllers.companies import CompanyController
from di.markers import CompanyControllerMarker
from dto.companies import GetCompanyDTO

company_router = APIRouter()


@company_router.get("/companies/{id_}", response_model=GetCompanyDTO)
async def get_one_city(
    id_: int,
    controller: CompanyController = Depends(CompanyControllerMarker),
):
    return await controller.get_one_from_id(id_=id_)


@company_router.get("/companies", response_model=list[GetCompanyDTO])
async def get_cities(
    controller: CompanyController = Depends(CompanyControllerMarker),
):
    return await controller.get_all()
