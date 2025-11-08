from config.database import SessionLocal
from models.user_model import User

def check_users():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        for user in users:
            print(f"Usuario: {user.email}, Rol: {user.role}")
    finally:
        db.close()

if __name__ == "__main__":
    check_users()