import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Word(Base):
    __tablename__ = 'word'

    id = Column(Integer)
    vocabulary_word = Column(String(250), nullable=False, primary_key=True)
    translated_word = Column(String(250), nullable=False)
    vocabulary_word_pron = Column(String(250))
    primary_def = Column(String(250), nullable=False)
    primary_def_example = Column(String(250), nullable=False)
    wordtype = Column(String(250), nullable=False)
    word_family_1st = Column(String(250))
    word_family_2nd = Column(String(250))
    word_family_3rd = Column(String(250))
    word_family_4th = Column(String(250))
    word_family_5th = Column(String(250))
    voice_clip = Column(String(250))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'vocabulary_word': self.vocabulary_word,
            'translated_word': self.translated_word,
            'primary_def': self.primary_def,
            'primary_def_example': self.primary_def_example,
            'vocabulary_word_pron': self.vocabulary_word_pron,
            'voice_clip': self.voice_clip
        }


engine = create_engine('sqlite:///words.db')


Base.metadata.create_all(engine)
