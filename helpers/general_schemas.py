from typing import Generic, TypeVar
from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar("T")


class ListBaseSchema(GenericModel, Generic[T]):
    next: int | None
    prev: int | None
    count: int = 0
    data: list[T] = []


class PersonSchema(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
