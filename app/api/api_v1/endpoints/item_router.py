from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud import item_crud
from app.db import get_db
from app.schemas.item_schemas import ItemIn, ItemOut, ItemUpdate


router = APIRouter()


@router.post("/", response_model=ItemOut)
def create_item(item_in: ItemIn, db: Session = Depends(get_db)):
    item = item_crud.create_item(db, item_in)
    return jsonable_encoder(item)


@router.get("/", response_model=List[ItemOut])
def get_all_items(db: Session = Depends(get_db)):
    items = item_crud.read_items(db)
    return jsonable_encoder(items)


@router.patch("/{item_id}", response_model=ItemOut)
def patch_item(item_id: int, item_update: ItemUpdate, db: Session = Depends(get_db)):
    item = item_crud.patch_item(db, item_id, item_update.dict(exclude_none=True))
    return jsonable_encoder(item)


@router.put("/{item_id}", response_model=ItemOut)
def put_item(item_id: int, item_in: ItemIn, db: Session = Depends(get_db)):
    item = item_crud.put_item(db, item_id, item_in)
    return jsonable_encoder(item)


@router.delete("/{item_id}", response_model=ItemOut)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = item_crud.delete_item(db, item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} was not found.",
        )
    return jsonable_encoder(item)
