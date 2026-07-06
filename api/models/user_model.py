from pydantic import BaseModel


class UserModel(BaseModel):
    id: int | None = None
    username: str | None = None
    email: str | None = None
    password: str | None = None
