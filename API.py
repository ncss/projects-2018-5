import random
import re
import sqlite3

drop_votes = 'DROP TABLE IF EXISTS votes;'
create_votes = '''
CREATE TABLE votes (
    song_id INTEGER,
    vote TEXT
);
'''
drop_songs = 'DROP TABLE IF EXISTS songs;'
create_songs = '''
CREATE TABLE songs (
    id INTEGER UNIQUE,
    location TEXT,
    title TEXT,
    artist TEXT,
    album_cover TEXT
);
'''
insert_songs = r'''INSERT INTO songs VALUES (1, '/static/mp3/Havana.mp3', 'Havana', 'Camilla Cabello', '/static/albumCovers/Havana.png'),
(2, '/static/mp3/Paradise.mp3', 'Paradise', 'Coldplay', '/static/albumCovers/Paradise.jpg'),
(3, '/static/mp3/BlankSpace.mp3', 'Blank Space', 'Taylor Swift', '/static/albumCovers/BlankSpace.png'),
(4, '/static/mp3/AchillesComeDown.mp3', 'Achilles Come Down', 'Gang of Youths', '/static/albumCovers/Achilles.jpg'),
(5, '/static/mp3/TheFinalCountdown.mp3', 'The Final Countdown', 'Europe', '/static/albumCovers/Countdown.jpg'),
(6, '/static/mp3/BohemianRhapsody.mp3', 'Bohemian Rhapsody', 'Queen', '/static/albumCovers/Queen.jpg'),
(7, '/static/mp3/Thunder.mp3', 'Thunder', 'Imagine Dragons', '/static/albumCovers/Thunder.jpg'),
(8, '/static/mp3/ShortCircuit.mp3', 'Short Circuit', 'Daft Punk', '/static/albumCovers/Circuit.png'),
(9, '/static/mp3/HotlineBling.mp3', 'Hotline Bling', 'Drake', '/static/albumCovers/Hotline.png'),
(10, '/static/mp3/TheATeam.mp3', 'The A Team', 'Ed Sheeran', '/static/albumCovers/Ateam.jpg'),
(11, '/static/mp3/NeverGonnaGiveYouUp.mp3', 'Never Gonna Give You Up', 'Rick Astley', '/static/albumCovers/NeverGonnaGiveYouUp.jpg'),
(12, "/static/mp3/HowFarI'llGo.mp3", "How Far I'll Go", 'James Curran', '/static/albumCovers/Moana.jpg');'''
insert_votes = '''INSERT INTO votes VALUES (4, 'up'),
(5, 'down'),
(6, 'up'),
(7, 'down'),
(8, 'down'),
(9, 'up'),
(10, 'down');'''

#cur = sqlite3.cursor()
class Database:
    def __init__(self):
        self.con = sqlite3.connect("ncssbook.db")
        self.cur = self.con.cursor()
        self.cur.execute(drop_votes)
        self.cur.execute(create_votes)
        self.cur.execute(drop_songs)
        self.cur.execute(create_songs)
        self.cur.execute(insert_songs)
        self.cur.execute(insert_votes)

    def reboot(self):
        self.con.close()
        self.con = sqlite3.connect("ncssbook.db")
        self.cur = self.con.cursor()
        self.cur.execute(drop_votes)
        self.cur.execute(create_votes)
        self.cur.execute(drop_songs)
        self.cur.execute(create_songs)
        self.cur.execute(insert_songs)
        self.cur.execute(insert_votes)

    @staticmethod
    def rand_music(musics):
        return random.choice(musics)
        #return object of random music(that has not been played)


    #def name_find(self, name):
        #if name is in the database
            #return True
        #else:
            #return True
        #pass

    #def all_names(self):
        #return()#all names in the database

db = Database()
cur = db.cur
class Person:

    def __init__(self):
        self.name = "Jimmy Neutron" #get the current users username

    def get_name(self):
        return self.name

    def good(self): #returns list of songs a user likes
        rows = cur.execute("SELECT title, artist FROM songs s JOIN votes v ON s.id=v.song_id WHERE v.vote = 'up'")
        songs = []
        for row in rows:
            song = {}
            song["title"] = row[0]
            song["artist"] = row[1]
            songs.append(song)
        return songs

    def bad(self): #returns list of songs a user dislikes
        rows = cur.execute("SELECT title, artist FROM songs s JOIN votes v ON s.id=v.song_id WHERE v.vote = 'down'")
        songs = []
        for row in rows:
            song = {}
            song["title"] = row[0]
            song["artist"] = row[1]
            songs.append(song)
        return songs

    #def add_song(self, vote):
        #if vote == "BAD":
            #add that vote to the database
        #elif vote == "GOOD":
            #add that vote to the database
        #else:
            #raise ValueError("vote should be \"BAD\" or \"GOOD\"")


class Song:
        def __init__(self, id, name, artist, location, cover):
            self.id = id
            self.title = name
            self.artist = artist
            self.location = location
            self.cover = cover


person = Person()

def get_all_songs():
    song_details = 'SELECT * FROM songs;'
    cur.execute(song_details)
    musics = []
    for row in cur:
        id = row[0]
        location = row[1]
        name = row[2]
        artist = row[3]
        cover = row[4]
        musics.append(Song(id,name,artist,location,cover))
    return musics

def vote(input):
    print(input)
    if input[2] == '0':
        cur.execute('''INSERT INTO votes VALUES ({}, 'down');'''.format(input[1]))
    else:
        cur.execute('''INSERT INTO votes VALUES ({}, 'up');'''.format(input[1]))

    up_votes = '''SELECT id, location, title, artist, album_cover FROM songs s JOIN votes v ON s.id=v.song_id WHERE v.vote = 'up';'''
    cur.execute(up_votes)
    for row in cur:
        id = row[0]
        location = row[1]
        name = row[2]
        artist = row[3]
        cover = row[4]
        person.good().append(Song(id,name,artist,location,cover))

    down_votes ='''SELECT id, location, title, artist, album_cover FROM songs s JOIN votes v ON s.id=v.song_id WHERE v.vote = 'down';'''
    cur.execute(down_votes)
    for row in cur:
        id = row[0]
        location = row[1]
        name = row[2]
        artist = row[3]
        cover = row[4]
        person.bad().append(Song(id,name,artist,location,cover))
    return True #to be fixed with try catch block


def get_person():
    return person
