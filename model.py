import os
import sys
from sqlalchemy import Column, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
#from sqlalchemy import relationship


engine =  create_engine('sqlite:///sqlalchemy_lyrics.db')
Session = sessionmaker(bind=engine)
session=Session()

Base = declarative_base()


class LyricSave(Base):
    __tablename__="Tracks"
    track_id = Column(String(255), primary_key=True)
    track_lyrics = Column(Text)
    def __init__(self,track_id,track_lyrics):
        self.track_id=track_id
        self.track_lyrics=track_lyrics





# def  clear_lyrics():
#     song_deleted=session.query(LyricSave).delete()
#     session.commit()


Base.metadata.create_all(engine)
