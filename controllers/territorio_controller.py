from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.territorio_model import Territorio, Municipio
from config.database import get_db_session
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/territorios", tags=["territorios"])

class TerritorioBase(BaseModel):
    nombre: str
    producto: str
    municipio_id: int

class TerritorioCreate(TerritorioBase):
    pass

class TerritorioOut(TerritorioBase):
    id: int
    class Config:
        orm_mode = True

@router.post("/", response_model=TerritorioOut)
def create_territorio(territorio: TerritorioCreate, db: Session = Depends(get_db_session)):
    municipio = db.query(Municipio).filter(Municipio.id == territorio.municipio_id).first()
    if not municipio:
        raise HTTPException(status_code=404, detail="Municipio no encontrado")
    db_territorio = Territorio(nombre=territorio.nombre, producto=territorio.producto, municipio_id=territorio.municipio_id)
    db.add(db_territorio)
    db.commit()
    db.refresh(db_territorio)
    return db_territorio

@router.get("/", response_model=List[TerritorioOut])
def list_territorios(db: Session = Depends(get_db_session)):
    return db.query(Territorio).all()

@router.get("/{territorio_id}", response_model=TerritorioOut)
def get_territorio(territorio_id: int, db: Session = Depends(get_db_session)):
    territorio = db.query(Territorio).filter(Territorio.id == territorio_id).first()
    if not territorio:
        raise HTTPException(status_code=404, detail="Territorio no encontrado")
    return territorio

@router.delete("/{territorio_id}")
def delete_territorio(territorio_id: int, db: Session = Depends(get_db_session)):
    territorio = db.query(Territorio).filter(Territorio.id == territorio_id).first()
    if not territorio:
        raise HTTPException(status_code=404, detail="Territorio no encontrado")
    db.delete(territorio)
    db.commit()
    return {"ok": True}
