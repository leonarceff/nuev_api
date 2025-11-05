from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user_model import User
from services.auth_service import register_user
from config.database import get_db_session, SessionLocal

def create_admin():
    db = SessionLocal()
    try:
        admin = register_user(db, "admin@example.com", "admin123", "admin")
        if admin:
            print("Usuario administrador creado exitosamente")
        else:
            print("El usuario ya existe o hubo un error")
    finally:
        db.close()

if __name__ == "__main__":
    create_admin()