# from fastapi import APIRouter
# from fastapi import Depends
#
# from controllers.products import ProductController
# from di.markers import ProductControllerMarker
# from dto.products import GetProductDTO
#
# order_router = APIRouter()
#
#
# @order_router.get("/customers/{id_}/orders", response_model=GetProductDTO)
# async def get_orders(
#     id_: int,
#     controller: ProductController = Depends(ProductControllerMarker),
# ):
#     return await controller.get_one_from_id(id_=id_)
