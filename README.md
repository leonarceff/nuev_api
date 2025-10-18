
# API Territorio

API RESTful para gestión de municipios y territorios con autenticación JWT y roles.

## Instalación

```bash
git clone <URL-del-repo>
cd nuev_api
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## Variables de entorno

Puedes usar un archivo `.env` para definir variables como `SECRET_KEY` si lo deseas.

## Cómo correr en desarrollo

```bash
uvicorn main:app --reload
```

## Cómo ejecutar pruebas

```bash
pytest test_api.py
```

## Roles y permisos

- `user`: Acceso básico (crear/login, consultar)
- `admin`: Acceso total (CRUD)

## Ejemplo de tokens

```json
{
	"access_token": "<jwt>",
	"token_type": "bearer"
}
```

## Flujo de autenticación

1. Registro: `/auth/register` (POST)
2. Login: `/auth/login` (POST) → Recibe JWT
3. Usar JWT en header: `Authorization: Bearer <token>`

## Endpoints principales

| Método | Endpoint              | Descripción                  | Protegido |
|--------|----------------------|------------------------------|-----------|
| POST   | /auth/register        | Registro de usuario          | No        |
| POST   | /auth/login           | Login y obtención de token   | No        |
| POST   | /municipios/          | Crear municipio              | Sí        |
| GET    | /municipios/          | Listar municipios            | No        |
| GET    | /municipios/{id}      | Obtener municipio            | No        |
| DELETE | /municipios/{id}      | Eliminar municipio           | Sí        |
| POST   | /territorios/         | Crear territorio             | Sí        |
| GET    | /territorios/         | Listar territorios           | No        |
| GET    | /territorios/{id}     | Obtener territorio           | No        |
| DELETE | /territorios/{id}     | Eliminar territorio          | Sí        |

## Pruebas mínimas incluidas

- Registro y login válidos/ inválidos
- Acceso a ruta protegida con/sin token

---
Autor: Tu Nombre | 2025
