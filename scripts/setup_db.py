from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user_model import User, Base
from services.auth_service import register_user
from config.database import SessionLocal, DATABASE_URL

def setup_database():
    # Crear el engine
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    
    # Crear todas las tablas
    Base.metadata.create_all(bind=engine)
    
    # Crear sesión
    db = SessionLocal()
    
    try:
        # Verificar si ya existe un admin
        admin = db.query(User).filter(User.email == "admin@example.com").first()
        if not admin:
            # Crear usuario admin
            admin = register_user(db, "admin@example.com", "admin123", "admin")
            print("Usuario administrador creado exitosamente")
        else:
            print("El usuario administrador ya existe")
            # Actualizar contraseña del admin existente
            admin = register_user(db, "admin2@example.com", "admin123", "admin")
            print("Se creó un usuario administrador alternativo")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    setup_database()