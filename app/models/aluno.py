from sqlalchemy import Column, Enum, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship
import enum
from app.models.base import BaseModel

class StatusPagamento(enum.Enum):
    EM_DIA = "em_dia"
    ATRASADO = "atrasado"
    PENDENTE = "pendente"

class Aluno(BaseModel):
    __tablename__ = "alunos"
    
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    status_pagamento = Column(Enum(StatusPagamento), default=StatusPagamento.PENDENTE)
    observacoes = Column(Text)
    
    # Relationships
    usuario = relationship("Usuario", back_populates="aluno")
    agendamentos = relationship("Agendamento", back_populates="aluno")
    evolucoes = relationship("Evolucao", back_populates="aluno")
    pagamentos = relationship("Pagamento", back_populates="aluno")