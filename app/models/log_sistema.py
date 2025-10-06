from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Text, JSON
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class LogSistema(BaseModel):
    __tablename__ = "logs_sistema"
    
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    acao = Column(String(100), nullable=False)
    tabela_afetada = Column(String(50))
    registro_id = Column(Integer)
    dados_anteriores = Column(JSON)
    dados_novos = Column(JSON)
    ip_address = Column(String(45))
    
    # Relationships
    usuario = relationship("Usuario")