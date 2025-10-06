from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Estudio(BaseModel):
    __tablename__ = "estudios"
    
    nome = Column(String(100), nullable=False, index=True)
    endereco = Column(Text)
    telefone = Column(String(20))
    
    # Relationships
    usuarios = relationship("Usuario", back_populates="estudio")
    aulas = relationship("Aula", back_populates="estudio")