from pydantic import BaseModel


class ProductModel(BaseModel):
    id: int
    title: str
    price: float
    description: str
    category: str
    image: str
