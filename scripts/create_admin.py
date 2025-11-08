from sqlalchemy.orm import Session
from config.database import SessionLocal, init_db
from services.auth_service import register_user

def create_admin():
    init_db()
    db = SessionLocal()
    try:
        admin = register_user(db, "admin@example.com", "admin123", "admin")
        if admin:
            print("Usuario administrador creado exitosamente")
        else:
            print("El usuario administrador ya existe")
    finally:
        db.close()

if __name__ == "__main__":
    create_admin()
