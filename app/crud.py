from sqlalchemy.future import select
from sqlalchemy.orm import Session
from .models import Item

async def get_item(db: Session, item_id: int):
    result = await db.execute(select(Item).filter(Item.id == item_id))
    return result.scalar_one_or_none()

async def create_item(db: Session, name: str):
    new_item = Item(name=name)
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)
    return new_item
