import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.db import Base
from models.user_model import User
from passlib.context import CryptContext

# Configuración
DATABASE_URL = "sqlite:///territorio.db"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Crear el motor de base de datos
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db_and_create_admin():
    # Crear todas las tablas
    Base.metadata.create_all(bind=engine)
    
    # Crear sesión
    db = SessionLocal()
    
    try:
        # Verificar si el admin ya existe
        admin = db.query(User).filter(User.email == "admin@example.com").first()
        
        if not admin:
            # Crear usuario admin
            hashed_password = pwd_context.hash("admin123")
            admin = User(
                email="admin@example.com",
                hashed_password=hashed_password,
                role="admin"
            )
            db.add(admin)
            db.commit()
            print("Usuario administrador creado exitosamente")
        else:
            print("El usuario administrador ya existe")
            
        # Mostrar todos los usuarios
        print("\nUsuarios en la base de datos:")
        users = db.query(User).all()
        for user in users:
            print(f"Email: {user.email}, Rol: {user.role}")
            
    finally:
        db.close()

if __name__ == "__main__":
    init_db_and_create_admin()