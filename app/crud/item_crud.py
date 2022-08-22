from typing import Any, Dict, List

from sqlalchemy.orm import Session

from app.crud import crud_base
from app.models.item_model import Item
from app.schemas.item_schemas import ItemIn


def create_item(db: Session, item_in: ItemIn) -> Item:
    model = Item(**item_in.dict())
    return crud_base.create(db, model)


def read_items(db: Session, *criterion) -> List[Item]:
    return crud_base.read_multiple(db, Item, *criterion)


def read_item(db: Session, item_id: int) -> Item:
    return crud_base.read_single(db, Item, Item.id == item_id)


def patch_item(db: Session, item_id: int, data: Dict[str, Any]) -> Item:
    item = read_item(db, item_id)
    return crud_base.patch(db, item, data)


def put_item(db: Session, item_id: int, item_in: ItemIn) -> Item:
    item = read_item(db, item_id)
    return crud_base.put(db, item, item_in.dict())


def delete_item(db: Session, item_id: int) -> Item:
    return crud_base.delete(db, Item, item_id)
