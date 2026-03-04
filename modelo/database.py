from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

#base para os modelos
Base = declarative_base()

#tabela principal
class AlbumDB(Base):
    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    artista = Column(String, nullable=False)
    quant_musicas = Column(Integer, default=0)
    ativo = Column(Boolean, default=False)

    avaliacoes = relationship('RatingDB', back_populates='album', cascade='all, delete-orphan')

#tabela para ratings
class RatingDB(Base):
    __tablename__ = 'ratings'