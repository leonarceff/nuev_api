from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import database

app = FastAPI(title="API Territorio", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Importar y registrar routers aquí (auth, territorio, municipio)
from controllers.auth_controller import router as auth_router
from controllers.territorio_controller import router as territorio_router
from controllers.municipio_controller import router as municipio_router
app.include_router(auth_router)
app.include_router(territorio_router)
app.include_router(municipio_router)

@app.get("/")
def root():
    return {"message": "API Territorio funcionando"}
