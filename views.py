import requests
import click
from model import LyricSave
from tabulate import tabulate
from colorama import Fore, Back, Style


class Lyrics():
    def __init__(self):
        self.api = "http://api.musixmatch.com/ws/1.1/"
        self.api_key="fd50ee54d357935a8742edaa76394ff8"
        self.headers={
        'Authorization': 'Bearer fd50ee54d357935a8742edaa76394ff8'
        }


    def song_find(self,query):
        '''
        This function receives a users querry_string and
        returns songs that matches with the querry from the API.
        '''
        method = "track.search"
        query_string = {"apikey": self.api_key, "q": query}
        try:
             data = requests.get(self.api + method, params=query_string,headers=self.headers).json()
        except:
            raise requests.exceptions.ConnectionError("****No Connection****")

        '''
        Tabualtion is python library designed to make it quick
        and easy to represent data in a visually appealing table
        '''

        table_headers = ['Index', 'ID', 'Title', 'Artist','Album']
        index=1
        table = []

        for item in data['message']['body']['track_list']:
            track_id = item['track']['track_id']
            track_name = item['track']['track_name']
            artist_name = item['track']['artist_name']
            album_name = item['track']['album_name']

            table.append([index,track_id, track_name, artist_name, album_name])
        '''
        prints out the tabulated data
        '''
        index+=1

        print tabulate(table, table_headers,tablefmt="fancy_grid")


    def song_view(self,track_id):

        #if self.session.query(music).filter_by(song_id=track_id):
        method="track.lyrics.get"
        query_string = {"apikey": self.api_key, "track_id": track_id}
        response = requests.get(self.api + method, params=query_string)
        data = response.json()
        lyrics=data["message"]["body"]["lyrics"]["lyrics_body"]
        if save:
            app.save_lyrics(track_id, lyrics)
        print lyrics
