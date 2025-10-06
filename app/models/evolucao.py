from sqlalchemy import Column, Enum, Integer, ForeignKey, Text, Date
from sqlalchemy.orm import relationship
import enum
from app.models.base import BaseModel

class TipoEvolucao(enum.Enum):
    CLINICA = "clinica"
    EDUCACAO_FISICA = "educacao_fisica"

class Evolucao(BaseModel):
    __tablename__ = "evolucoes"
    
    aluno_id = Column(Integer, ForeignKey("alunos.usuario_id"), nullable=False)
    professor_id = Column(Integer, ForeignKey("professores.usuario_id"), nullable=False)
    aula_id = Column(Integer, ForeignKey("aulas.id"), nullable=False)
    data_avaliacao = Column(Date, nullable=False)
    tipo = Column(Enum(TipoEvolucao), nullable=False)
    exercicios_realizados = Column(Text)
    observacoes = Column(Text)
    avaliacao_postural = Column(Text)  # apenas para fisioterapeutas
    amplitude_movimento = Column(Text)  # apenas para fisioterapeutas
    nivel_dor = Column(Integer)  # 0-10, apenas para fisioterapeutas
    
    # Relationships
    aluno = relationship("Aluno", back_populates="evolucoes")
    professor = relationship("Professor", back_populates="evolucoes")
    aula = relationship("Aula", back_populates="evolucoes")