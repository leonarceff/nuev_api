from jose import jwt, JWTError
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models.user_model import User
import hashlib
import os
import base64

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def get_password_hash(password: str) -> str:
    salt = base64.b64encode(os.urandom(16)).decode('utf-8')
    password_hash = hashlib.sha256(password.encode() + salt.encode()).hexdigest()
    return f"{salt}${password_hash}"

def verify_password(plain_password: str, hashed_password: str) -> bool:
    if not hashed_password or '$' not in hashed_password:
        return False
    salt, stored_hash = hashed_password.split('$')
    password_hash = hashlib.sha256(plain_password.encode() + salt.encode()).hexdigest()
    return password_hash == stored_hash


def register_user(db: Session, email: str, password: str, role: str = "user"):
    user = db.query(User).filter(User.email == email).first()
    if user:
        return None
    hashed_password = get_password_hash(password)
    new_user = User(email=email, hashed_password=hashed_password, role=role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, str(user.hashed_password)):
        return None
    return user

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
