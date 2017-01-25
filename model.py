import os
import sys
from sqlalchemy import Column, String, Text ,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import relationship


Base = declarative_base()

class LyricSave(Base):
    __tablename__="songs"
    song_id = Column(String, primary_key=True)
    track_id = Column(String(255))
    song_name=Column(String(250))
    song_lyrics = Column(Text())
