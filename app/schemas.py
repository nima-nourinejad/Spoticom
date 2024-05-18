# schemas.py

from pydantic import BaseModel

class ItemResponse(BaseModel):
    id: int
    name: str
