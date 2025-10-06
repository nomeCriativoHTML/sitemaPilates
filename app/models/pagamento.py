from sqlalchemy import Column, Enum, Integer, ForeignKey, DateTime, String, Numeric, Date
from sqlalchemy.orm import relationship
import enum
from app.models.base import BaseModel

class StatusPagamento(enum.Enum):
    PENDENTE = "pendente"
    PAGO = "pago"
    ATRASADO = "atrasado"

class Pagamento(BaseModel):
    __tablename__ = "pagamentos"
    
    aluno_id = Column(Integer, ForeignKey("alunos.usuario_id"), nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)
    data_vencimento = Column(Date, nullable=False)
    data_pagamento = Column(Date, nullable=True)
    status = Column(Enum(StatusPagamento), default=StatusPagamento.PENDENTE)
    metodo_pagamento = Column(String(50))
    observacoes = Column(Text)
    
    # Relationships
    aluno = relationship("Aluno", back_populates="pagamentos")