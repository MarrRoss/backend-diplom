from fastapi import APIRouter
from fastapi import Depends

from controllers.states import StateController
from di.markers import StateControllerMarker
from dto.states import GetStateDTO

state_router = APIRouter()


@state_router.get("/states/{id_}", response_model=GetStateDTO)
async def get_one_city(
    id_: int,
    controller: StateController = Depends(StateControllerMarker),
):
    return await controller.get_one_from_id(id_=id_)


@state_router.get("/states", response_model=list[GetStateDTO])
async def get_cities(
    controller: StateController = Depends(StateControllerMarker),
):
    return await controller.get_all()
