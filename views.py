import requests
import click
from prettytable import PrettyTable as table
from tabulate import tabulate

class Lyrics():
    def __init__(self):
        self.api_url = "http://api.musixmatch.com/ws/1.1/"
        self.api_key="fd50ee54d357935a8742edaa76394ff8"
        self.songs={}
    '''    self.session = Session()'''
    '''searches for song details usi'''

    def song_find(self,query):

        method = "track.search"
        query_string = {"apikey": self.api_key, "q": query}
        data = requests.get(self.api_url + method, params=query_string).json()


        table_headers = ['ID', 'Title', 'Artist','Album']
        table = []

        for item in data['message']['body']['track_list']:
            track_id = item['track']['track_id']
            track_name = item['track']['track_name']
            artist_name = item['track']['artist_name']
            album_name =item['track']['album_name']
            table.append([track_id, track_name, artist_name , album_name])
            print tabulate(table, table_headers,tablefmt="fancy_grid")

    def song_view(self,track_id):

        #if self.session.query(music).filter_by(song_id=track_id):
        method="track.lyrics.get"
        query_string = {"apikey": self.api_key, "track_id": track_id}
        response = requests.get(self.api_url + method, params=query_string)
        data = response.json()
        print data
