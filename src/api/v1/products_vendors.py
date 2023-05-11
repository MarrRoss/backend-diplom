from fastapi import APIRouter, Depends
from controllers.products_vendors import ProductVendorController
from di.markers import ProductVendorControllerMarker
from dto.products_vendors import CreateProductVendorDTO
from dto.products_vendors import GetProductVendorDTO

product_vendor = APIRouter()


@product_vendor.get("/products_vendors/{id_}", response_model=GetProductVendorDTO)
async def get_one_product_vendor(
    id_: int,
    controller: ProductVendorController = Depends(ProductVendorControllerMarker),
):
    return await controller.get_one_from_id(id_=id_)


@product_vendor.get("/products_vendors", response_model=list[GetProductVendorDTO])
async def get_all_product_vendor(
    controller: ProductVendorController = Depends(ProductVendorControllerMarker),
):
    return await controller.get_all()


@product_vendor.post("/products_vendors", response_model=GetProductVendorDTO)
async def create_one_product_vendor(
    data: CreateProductVendorDTO,
    controller: ProductVendorController = Depends(ProductVendorControllerMarker),
):
    return await controller.create_one(data=data)
