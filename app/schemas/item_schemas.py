from typing import Union

from pydantic import BaseModel


class ItemIn(BaseModel):
    name: str
    description: str


class ItemOut(BaseModel):
    id: int
    name: str
    description: str


class ItemUpdate(BaseModel):
    name: Union[str, None] = None
    description: Union[str, None] = None
