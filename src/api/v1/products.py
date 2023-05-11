from fastapi import APIRouter
from fastapi import Depends

from controllers.products import ProductController
from di.markers import ProductControllerMarker
from dto.products import CreateProductDTO
from dto.products import GetProductDTO
from dto.products import GetSmallProductDTO

product_router = APIRouter()


@product_router.get("/products/{id_}", response_model=GetProductDTO)
async def get_one_city(
    id_: int,
    controller: ProductController = Depends(ProductControllerMarker),
):
    return await controller.get_one_from_id(id_=id_)


@product_router.get("/products", response_model=list[GetProductDTO])
async def get_cities(
    controller: ProductController = Depends(ProductControllerMarker),
):
    return await controller.get_all()


@product_router.post("/products", response_model=GetSmallProductDTO)
async def create_product(
    data: CreateProductDTO,
    controller: ProductController = Depends(ProductControllerMarker),
):
    return await controller.add_one(data=data)

