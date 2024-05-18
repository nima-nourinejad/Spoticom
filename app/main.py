# main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .schemas import ItemResponse
from . import crud

app = FastAPI()

# Endpoint for creating an item
@app.post("/items/", response_model=ItemResponse)
async def create_item(name: str, db: Session = Depends(get_db)):
    return await crud.create_item(db, name)

# Endpoint for reading an item
@app.get("/items/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    item = await crud.get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
