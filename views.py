import requests
import urllib
import urllib.parse
import json
import socket
import musixmatch


class Lyrics(object):
    """docstring for ."""
    def __init__(self):
        self.api = "http://api.musixmatch.com/ws/1.1/"
        self.api_key='fd50ee54d357935a8742edaa76394ff8'

    def find_song(self,query):
        method="track.search?q="
        query_string = (self.api + method + urllib.parse.quote(query_name))
                        +"&apikey="+ self.api_key+"&format=plain")

        data = requests.get(self.api + method, params=query_string).json()

        results = data
        return results

     def get_song(self,song_id):
         method="track.lyrics.get?track_id="
         querystring = (self.api +
                    + method+
                   (urllib.parse.quote(track_id)) +
                   "&apikey=" +
                   self.api_key +
                   "&format=json" +
                   "&f_has_lyrics=1")

         response = requests.get(self.api + method, params=query_string)
         data = response.json()
         results=data
         return results
