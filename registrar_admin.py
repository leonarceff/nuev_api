import requests

# Registro de usuario admin con rol admin
resp = requests.post(
    "http://localhost:8000/auth/register",
    json={"email": "admin@admin.com", "password": "admin123", "role": "admin"}
)
print(resp.status_code, resp.json())
