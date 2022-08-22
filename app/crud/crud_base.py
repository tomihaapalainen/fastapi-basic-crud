from typing import Any, Dict, Type

from sqlalchemy.orm import Session

from app.db import DeclarativeBase


def create(db: Session, model: Type[DeclarativeBase]):
    db.add(model)
    db.commit()
    db.refresh(model)
    return model


def read_multiple(db: Session, model_cls: Type[DeclarativeBase], *criterion):
    return db.query(model_cls).filter(*criterion).all()


def read_single(db: Session, model_cls: Type[DeclarativeBase], *criterion):
    return db.query(model_cls).filter(*criterion).first()


def patch(db: Session, model: Type[DeclarativeBase], data: Dict[str, Any]):
    for field in data:
        if hasattr(model, field):
            setattr(model, field, data[field])
    db.add(model)
    db.commit()
    db.refresh(model)
    return model


def put(db: Session, model: Type[DeclarativeBase], data: Dict[str, Any]):
    for field in data:
        setattr(model, field, data[field])
    db.add(model)
    db.commit()
    db.refresh(model)
    return model


def delete(db: Session, model: Type[DeclarativeBase], model_id):
    model = read_single(db, model, model.id == model_id)
    if model is None:
        return None
    db.delete(model)
    db.commit()
    return model
