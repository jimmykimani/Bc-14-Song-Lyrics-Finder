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
    track_lyrics = Column(Text())
    '''
    An engine that stores data in the local directory
    '''

engine =  create_engine('sqlite:///sqlalchemy_lyrics.db')
'''
insert LyricSave in the lyrics table
'''

def save_lyrics(track_id,track_lyrics):
    lyrics=LyricSave(track_id=track_id,track_lyrics=track_lyrics)
    session.add(lyrics)
    session.commit()
def  clear_lyrics():
    song_deleted=session.query(LyricSave).delete()
    session()


Base.metadata.create_all(engine)    
