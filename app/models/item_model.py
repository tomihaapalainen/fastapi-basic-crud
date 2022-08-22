import sqlalchemy.sql.sqltypes as st
import sqlalchemy.sql.schema as sa

from app.db import DeclarativeBase


class Item(DeclarativeBase):
    __tablename__ = "item"

    id = sa.Column(st.Integer, primary_key=True)
    name = sa.Column(st.String)
    description = sa.Column(st.String)


DeclarativeBase.metadata.create_all()
