import requests
import click
from model import LyricSave
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base
from tabulate import tabulate
from colorama import Fore, Back, Style
from model import session


class Lyrics():
    def __init__(self):
        self.api = "http://api.musixmatch.com/ws/1.1/"
        self.api_key="fd50ee54d357935a8742edaa76394ff8"
        self.headers={
        'Authorization': 'Bearer fd50ee54d357935a8742edaa76394ff8'
        }


    def song_find(self,query):
        if query:
            '''
            This function receives a users querry_string and
            returns songs that matches with the querry from the API.
            '''

            query_string = {"apikey": self.api_key, "q": query}
            try:
                 data = requests.get(self.api + "track.search", params=query_string,headers=self.headers).json()
            except:
                raise requests.exceptions.ConnectionError("****No Connection****")

            '''
            Tabualtion is python library designed to make it quick
            and easy to represent data in a visually appealing table
            '''

            table_headers = [ 'ID', 'Title', 'Artist','Album']
            table = []

            for item in data['message']['body']['track_list']:
                track_id = item['track']['track_id']
                track_name = item['track']['track_name']
                artist_name = item['track']['artist_name']
                album_name = item['track']['album_name']

                table.append([track_id, track_name, artist_name, album_name])
            '''
            prints out the tabulated data
            '''

            return Fore.YELLOW + tabulate(table, table_headers,tablefmt="fancy_grid")
        else:
            return Fore.RED + "Enter find <query> to search name of song or artist"



    def song_view(self,track_id):
        if track_id:
            self._track_id = track_id
            self._lyrics=None

            query_string = {"apikey": self.api_key, "track_id": track_id}
            response = requests.get(self.api + "track.lyrics.get", params=query_string)
            data = response.json()
            lyrics=data["message"]["body"]["lyrics"]["lyrics_body"]
            self._lyrics=lyrics
            return Fore.YELLOW +lyrics
        else:
            return Fore.RED + "Enter a valid Track id"


    def save_lyrics(self, track_id):
        if track_id:
            lyrics_to_save=LyricSave(track_id=self._track_id,track_lyrics=self._lyrics)
            session.add(lyrics_to_save)
            # return lyrics_to_save
            session.commit()
            return Fore.GREEN +"Success! Song saved!!!."
        else:
            return Fore.RED +"Track id must be valid!!!"

    def clear_lyrics(self):
        session.query(LyricSave).delete()
        session.commit()
