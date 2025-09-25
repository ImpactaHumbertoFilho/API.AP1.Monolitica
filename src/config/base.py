from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Engine centralizado
engine = create_engine("sqlite:///meu_banco.db", echo=True)

# Session factory
SessionLocal = sessionmaker(bind=engine)