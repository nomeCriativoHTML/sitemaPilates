from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Professor(BaseModel):
    __tablename__ = "professores"
    
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    crefito = Column(String(50))
    crefi = Column(String(50))
    especialidade = Column(String(100))
    
    # Relationships
    usuario = relationship("Usuario", back_populates="professor")
    aulas = relationship("Aula", back_populates="professor")
    evolucoes = relationship("Evolucao", back_populates="professor")