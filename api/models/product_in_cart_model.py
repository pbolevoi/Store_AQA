from pydantic import BaseModel


class ProductInCartModel(BaseModel):
    productId: int | None = None
    quantity: int | None = None
