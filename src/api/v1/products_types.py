from fastapi import APIRouter, Depends
from controllers.products_types import ProductTypeController
from di.markers import ProductTypeControllerMarker
from dto.products_types import GetProductTypeDTO

product_type = APIRouter()


@product_type.get("/products_types/{id_}", response_model=GetProductTypeDTO)
async def get_one_city(
    id_: int,
    controller: ProductTypeController = Depends(ProductTypeControllerMarker),
):
    return await controller.get_one_from_id(id_=id_)


@product_type.get("/products_types", response_model=list[GetProductTypeDTO])
async def get_cities(
    controller: ProductTypeController = Depends(ProductTypeControllerMarker),
):
    return await controller.get_all()
