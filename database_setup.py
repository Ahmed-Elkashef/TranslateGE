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
    short_description = Column(String(250), nullable=False)
    long_description = Column(String(250), nullable=False)

    word_familie_1st_label = Column(String(250))
    word_familie_1st_score = Column(Integer)
    word_familie_1st_color = Column(String(250))

    word_familie_2nd_label = Column(String(250))
    word_familie_2nd_score = Column(Integer)
    word_familie_2nd_color = Column(String(250))

    word_familie_3rd_label = Column(String(250))
    word_familie_3rd_score = Column(Integer)
    word_familie_3rd_color = Column(String(250))

    word_familie_4th_label = Column(String(250))
    word_familie_4th_score = Column(Integer)
    word_familie_4th_color = Column(String(250))

    word_familie_5th_label = Column(String(250))
    word_familie_5th_score = Column(Integer)
    word_familie_5th_color = Column(String(250))

    voice_clip = Column(String(250))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'vocabulary_word': self.vocabulary_word,
            'id': self.id,
            'short_description': self.short_description,
            'long_description': self.long_description,
            'voice_clip': self.voice_clip
        }


engine = create_engine('sqlite:///words.db')


Base.metadata.create_all(engine)
