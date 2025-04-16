from pydantic import BaseModel

from models.pagination import Pagination


class User(BaseModel):
    id: int
    telegram_id: int


class UserPage(BaseModel):
    users: list[User]
    pagination: Pagination
