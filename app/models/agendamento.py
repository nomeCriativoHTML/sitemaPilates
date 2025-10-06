from sqlalchemy import Column, Enum, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import enum
from app.models.base import BaseModel

class StatusAgendamento(enum.Enum):
    AGENDADO = "agendado"
    PRESENTE = "presente"
    FALTOU = "faltou"
    CANCELADO = "cancelado"

class Agendamento(BaseModel):
    __tablename__ = "agendamentos"
    
    aula_id = Column(Integer, ForeignKey("aulas.id"), nullable=False)
    aluno_id = Column(Integer, ForeignKey("alunos.usuario_id"), nullable=False)
    status = Column(Enum(StatusAgendamento), default=StatusAgendamento.AGENDADO)
    data_agendamento = Column(DateTime, default=DateTime)
    data_presenca = Column(DateTime, nullable=True)
    
    # Relationships
    aula = relationship("Aula", back_populates="agendamentos")
    aluno = relationship("Aluno", back_populates="agendamentos")