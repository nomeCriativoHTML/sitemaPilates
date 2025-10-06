from sqlalchemy import Column, String, Boolean, Enum, Integer, ForeignKey
from sqlalchemy.orm import relationship
import enum
from app.models.base import BaseModel

class TipoUsuario(enum.Enum):
    ADMINISTRADOR = "administrador"
    PROFESSOR = "professor"
    ALUNO = "aluno"

class Usuario(BaseModel):
    __tablename__ = "usuarios"
    
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    telefone = Column(String(20))
    senha = Column(String(255), nullable=False)
    tipo = Column(Enum(TipoUsuario), nullable=False)
    estudio_id = Column(Integer, ForeignKey("estudios.id"), nullable=False)
    is_fisioterapeuta = Column(Boolean, default=False)
    ativo = Column(Boolean, default=True)
    
    # Relationships
    estudio = relationship("Estudio", back_populates="usuarios")
    aluno = relationship("Aluno", back_populates="usuario", uselist=False)
    professor = relationship("Professor", back_populates="usuario", uselist=False)