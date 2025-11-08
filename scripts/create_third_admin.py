import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from config.database import SessionLocal, init_db
from services.auth_service import register_user

def create_third_admin():
    db = SessionLocal()
    try:
        # Crear tercer usuario admin con contraseña más corta
        admin3 = register_user(db, "admin3@example.com", "admin3", "admin")
        if admin3:
            print("Tercer usuario administrador creado exitosamente")
            print(f"Email: admin3@example.com")
            print(f"Contraseña: admin3")
            print(f"Rol: {admin3.role}")
        else:
            print("El usuario admin3 ya existe")
            
    finally:
        db.close()

if __name__ == "__main__":
    create_third_admin()