from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.base import Base
from models.professor import Professor
from models.turma import Turma
from models.aluno import Aluno

# Engine centralizado
engine = create_engine("sqlite:///meu_banco.db", echo=True)

# Session factory
SessionLocal = sessionmaker(bind=engine)

# Cria todas as tabelas no banco
Base.metadata.create_all(bind=engine)