from api.models.product_in_cart_model import ProductInCartModel
from pydantic import BaseModel


class CartModel(BaseModel):
    id: int
    userId: int
    products: list[ProductInCartModel]
