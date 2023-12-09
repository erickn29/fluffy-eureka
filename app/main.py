# from dataclasses import Field
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

items = [
    {'id': 1, 'msg': 'Ivan'},
    {'id': 2, 'msg': 'Olga'}
]


class Item(BaseModel):
    """Model Item"""

    id: int = Field(ge=0)
    msg: str = Field(max_length=5)
    role: str = None


@app.get("/")
def read_root() -> dict:
    """Fake Annotation"""
    return {"Hello": "World"}


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, q: Union[str, None] = None) -> dict:
    """Fake Annotation"""
    for i in items:
        if item_id == i.get('id'):
            return {'msg': i}
    return {"item_id": item_id, "q": q}


@app.post("/items")
def write_item(item: Item) -> dict:
    """Fake Annotation"""
    items.append(item)
    return {"status": 201, "data": items}
