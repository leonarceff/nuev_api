
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.db import Base

class Municipio(Base):
    __tablename__ = "municipios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    territorios = relationship("Territorio", back_populates="municipio")

class Territorio(Base):
    __tablename__ = "territorios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    producto = Column(String, nullable=False)
    municipio_id = Column(Integer, ForeignKey("municipios.id"), nullable=False)
    municipio = relationship("Municipio", back_populates="territorios")
