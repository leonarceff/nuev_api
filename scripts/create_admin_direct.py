from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user_model import User, Base
from services.auth_service import register_user, get_password_hash
from config.database import DATABASE_URL

def create_admin():
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    try:
        # Verificar si el usuario ya existe
        user = db.query(User).filter(User.email == "admin@example.com").first()
        if not user:
            # Crear nuevo usuario
            hashed_password = get_password_hash("admin123")
            user = User(email="admin@example.com", hashed_password=hashed_password, role="admin")
            db.add(user)
            db.commit()
            print("Usuario administrador creado exitosamente")
        else:
            print("El usuario administrador ya existe")
            # Actualizar la contraseña
            user.hashed_password = get_password_hash("admin123")
            db.commit()
            print("Contraseña actualizada")
        
        print(f"Email: admin@example.com")
        print(f"Contraseña: admin123")
        
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_admin()