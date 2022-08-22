from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DeclarativeBase = declarative_base()

engine = create_engine("sqlite:///./site.db", pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
DeclarativeBase.metadata.bind = engine


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
