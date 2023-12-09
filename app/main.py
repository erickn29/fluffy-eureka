from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    """Fake Annotation"""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None) -> dict:
    """Fake Annotation"""
    return {"item_id": item_id, "q": q}
