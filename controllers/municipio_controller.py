from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.territorio_model import Municipio, Territorio
from config.database import get_db_session
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/municipios", tags=["municipios"])

class MunicipioBase(BaseModel):
    nombre: str
    descripcion: str | None = None

class MunicipioCreate(MunicipioBase):
    pass

class MunicipioOut(MunicipioBase):
    id: int
    class Config:
        orm_mode = True

@router.post("/", response_model=MunicipioOut)
def create_municipio(municipio: MunicipioCreate, db: Session = Depends(get_db_session)):
    db_municipio = Municipio(nombre=municipio.nombre, descripcion=municipio.descripcion)
    db.add(db_municipio)
    db.commit()
    db.refresh(db_municipio)
    return db_municipio

@router.get("/", response_model=List[MunicipioOut])
def list_municipios(db: Session = Depends(get_db_session)):
    return db.query(Municipio).all()

@router.get("/{municipio_id}", response_model=MunicipioOut)
def get_municipio(municipio_id: int, db: Session = Depends(get_db_session)):
    municipio = db.query(Municipio).filter(Municipio.id == municipio_id).first()
    if not municipio:
        raise HTTPException(status_code=404, detail="Municipio no encontrado")
    return municipio

@router.delete("/{municipio_id}")
def delete_municipio(municipio_id: int, db: Session = Depends(get_db_session)):
    municipio = db.query(Municipio).filter(Municipio.id == municipio_id).first()
    if not municipio:
        raise HTTPException(status_code=404, detail="Municipio no encontrado")
    db.delete(municipio)
    db.commit()
    return {"ok": True}
