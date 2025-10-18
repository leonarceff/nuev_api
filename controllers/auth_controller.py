from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.auth_service import register_user, authenticate_user, create_access_token
from config.database import get_db_session
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix="/auth", tags=["auth"])


class UserRegister(BaseModel):
    email: EmailStr
    password: str
    role: str = "user"

class UserLogin(BaseModel):
    email: EmailStr
    password: str


@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db_session)):
    db_user = register_user(db, user.email, user.password, user.role)
    if not db_user:
        raise HTTPException(status_code=400, detail="Email ya registrado")
    return {"message": "Usuario registrado correctamente"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db_session)):
    db_user = authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    access_token = create_access_token({"sub": db_user.email, "role": db_user.role})
    return {"access_token": access_token, "token_type": "bearer"}
