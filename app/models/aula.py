from sqlalchemy import Column, DateTime, Integer, Enum, String, ForeignKey
from sqlalchemy.orm import relationship
import enum
from app.models.base import BaseModel

class TipoAula(enum.Enum):
    PILATES_INICIANTE = "pilates_iniciante"
    PILATES_AVANCADO = "pilates_avancado"
    FISIOTERAPIA = "fisioterapia"
    REABILITACAO = "reabilitacao"

class StatusAula(enum.Enum):
    AGENDADA = "agendada"
    CONFIRMADA = "confirmada"
    CANCELADA = "cancelada"
    REALIZADA = "realizada"

class Aula(BaseModel):
    __tablename__ = "aulas"
    
    estudio_id = Column(Integer, ForeignKey("estudios.id"), nullable=False)
    professor_id = Column(Integer, ForeignKey("professores.usuario_id"), nullable=False)
    data_hora = Column(DateTime, nullable=False, index=True)
    duracao_minutos = Column(Integer, default=60)
    tipo_aula = Column(Enum(TipoAula), nullable=False)
    status = Column(Enum(StatusAula), default=StatusAula.AGENDADA)
    max_alunos = Column(Integer, default=3)
    
    # Relationships
    estudio = relationship("Estudio", back_populates="aulas")
    professor = relationship("Professor", back_populates="aulas")
    agendamentos = relationship("Agendamento", back_populates="aula")
    evolucoes = relationship("Evolucao", back_populates="aula")