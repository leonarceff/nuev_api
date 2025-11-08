import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from config.database import SessionLocal, init_db
from services.auth_service import register_user

def create_second_admin():
    db = SessionLocal()
    try:
        # Crear segundo usuario admin
        admin2 = register_user(db, "admin2@example.com", "admin456", "admin")
        if admin2:
            print("Segundo usuario administrador creado exitosamente")
            print(f"Email: admin2@example.com")
            print(f"Contraseña: admin456")
            print(f"Rol: {admin2.role}")
        else:
            print("El usuario admin2 ya existe")
            
    finally:
        db.close()

if __name__ == "__main__":
    create_second_admin()