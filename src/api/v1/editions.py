from fastapi import APIRouter, Depends

from controllers.editions import ProductEditionController
from di.markers import ProductEditionControllerMarker
from dto.editions import CreateEditionDTO
from dto.editions import GetEditionDTO

product_edition = APIRouter()


@product_edition.get("/editions/{id_}", response_model=GetEditionDTO)
async def get_one_edition(
    id_: int,
    controller: ProductEditionController = Depends(ProductEditionControllerMarker),
):
    return await controller.get_one_from_id(id_=id_)


@product_edition.get("/editions", response_model=list[GetEditionDTO])
async def get_all_editions(
    controller: ProductEditionController = Depends(ProductEditionControllerMarker),
):
    return await controller.get_all()


@product_edition.post("/editions", response_model=GetEditionDTO)
async def create_one_edition(
    data: CreateEditionDTO,
    controller: ProductEditionController = Depends(ProductEditionControllerMarker),
):
    return await controller.create_one(data=data)
