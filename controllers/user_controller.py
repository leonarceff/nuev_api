from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from models.user_model import User
from config.database import get_db_session
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["users"])

class UserResponse(BaseModel):
    id: int
    email: str
    role: str

    class Config:
        from_attributes = True

@router.get("/", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db_session)):
    users = db.query(User).all()
    return users