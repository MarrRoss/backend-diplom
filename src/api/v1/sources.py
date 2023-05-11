from fastapi import APIRouter, Depends, Query
from pyfa_converter import PyFaDepends
from controllers.sources import SourceController
from di.markers import SourceControllerMarker
from dto.filters.paginate import BasePaginateDTO
from dto.sources import GetSourceDTO

source_router = APIRouter()


@source_router.get("/sources/{id_}", response_model=GetSourceDTO)
async def get_one_city(
    id_: int,
    controller: SourceController = Depends(SourceControllerMarker),
):
    return await controller.get_one_from_id(id_=id_)


@source_router.get("/sources", response_model=list[GetSourceDTO])
async def get_cities(
    paginate: BasePaginateDTO = PyFaDepends(BasePaginateDTO, _type=Query),
    controller: SourceController = Depends(SourceControllerMarker),
):
    return await controller.get_all(paginate=paginate)
