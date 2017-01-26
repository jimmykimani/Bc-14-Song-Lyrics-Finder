# Discovr
__A song Lyric Finder. Andela Bootcamp Project Cohort 14 2017.__

#Introduction

__Discovr__ is an application that allows a user to find lyrics using either lyrics, song name or artist name.
It is Command Line Application that uses an API

__Discovr__ is written in python by leveraging the
 Click python package : (http://www.click.pocoo.org)
 SQLalchemy :(http://docs.sqlalchemy.org/en/latest/orm/)

 and also an Api from

 Musixmatch https://musixmatch.com/

## Main Features
* Allow user to search and view song name or artist
* Allow user to view Lyrics based on the song id
* Allow user to save Lyrics locally to the Database
* User can choose to clear the Database

## Installation
1. First git clone this project at https://github.com/jimmykimani/Bc-14-Song-Lyrics-Finder

2. Cd  to the Discovr folder.

3. Install a virtual environment, preferably virtualenv in this folder and activate it, using  virtualenv env ($ source venv/bin/activate)

4. $ pip install -r requirements.txt

5. Run the app by executing app.py (python app.py)


## How to use

* song find==<search_query_string> --->> Returns a list of Artist and song names in a tabulized way

* song view ==<song_id> --->> View song lyrics based on it’s id.

* song save == <song_id> --->> Store song details and lyrics locally.

* song clear== None --->> Clear entire local song database.

## Bugs
* Optimized by checking if there’s a local copy before checking online not working

Made with love by James Kimani(Jimmy)
