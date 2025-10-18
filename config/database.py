from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.db import Base

DATABASE_URL = "sqlite:///territorio.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db_session():
    return SessionLocal()

def init_db():
    import models.territorio_model
    import models.user_model
    Base.metadata.create_all(bind=engine)
