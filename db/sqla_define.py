from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Word(Base):
    __tablename__ = 'word'
    id = Column(Integer, primary_key=True)
    word = Column(String(50), nullable=False, unique=True)


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    tag = Column(String(50), nullable=False, unique=True)


class WordTag(Base):
    __tablename__ = 'word_tag'
    id = Column(Integer, primary_key=True)
    word_id = Column(Integer, ForeignKey('word.id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tag.id'), primary_key=True)


engine = create_engine('postgres://postgres:postgres@localhost:5432/nostra_db', echo=True)
Base.metadata.create_all(engine)

