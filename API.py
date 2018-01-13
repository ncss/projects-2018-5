import random
import re
import sqlite3

drop_votes = 'DROP TABLE IF EXISTS votes;'
create_votes = '''
CREATE TABLE votes (
	song_id INTEGER UNIQUE,
	vote TEXT
);
'''
drop_songs = 'DROP TABLE IF EXISTS songs;'
create_songs = '''
CREATE TABLE songs (
	id INTEGER UNIQUE,
	location TEXT,
	title TEXT,
	artist TEXT
);
'''

insert_songs = '''INSERT INTO songs VALUES (1, '', 'Havana', 'Camilla Cabello'),
(2, '', 'Paradise', 'Coldplay'),
(3,  '', 'Blank Space', 'Taylor Swift'),
(4, '', 'Achilles Come Down', 'Gang of Youths'),
(5, '', 'The Final Countdown', 'James Curran'),
(6, '', 'Bohemian Rhapsody', 'Queen'),
(7, '', 'Thunder', 'Imagine Dragons'),
(8, '', 'Short Circuit', 'Daft Punk'),
(9, '', 'Hotline Bling', 'Drake'),
(10, '', 'The A Team', 'Ed Sheeran');'''

insert_votes = '''INSERT INTO votes VALUES (1, 'up'),
(2, 'down'),
(3, 'up'),
(4, 'up'),
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
        cur = self.con.cursor()
        cur.execute(drop_votes)
        cur.execute(create_votes)
        cur.execute(drop_songs)
        cur.execute(create_songs)
        cur.execute(insert_songs)
        #cur.execute(insert_votes)

    def reboot(self):
        self.con.close()
        self.con = sqlite3.connect("ncssbook.db")
        cur = self.con.cursor()
        cur.execute(drop_votes)
        cur.execute(create_votes)
        cur.execute(drop_songs)
        cur.execute(create_songs)
        cur.execute(insert_songs)
        #scur.execute(insert_votes)


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


class Person:

    def __init__(self, con):
        self.name = "James" #get the current users username
        self.good = []
        self.bad = []
        up_votes = '''SELECT title FROM songs s JOIN votes v ON s.id=v.song_id WHERE v.vote = 'up';'''
        cur = con.cursor()
        cur.execute(up_votes)
        for row in cur:
            self.good.append(row)

        down_votes ='''SELECT title FROM songs s JOIN votes v ON s.id=v.song_id WHERE v.vote = 'down';'''
        cur.execute(down_votes)
        for row in cur:
            self.bad.append(row)


    def name(self):
        return(self.name)

    def good(self): #returns list of songs a user likes
        return(self.good)

    def bad(self): #returns list of songs a user dislikes
        return(self.bad)

    #def add_song(self, vote):
        #if vote == "BAD":
            #add that vote to the database
        #elif vote == "GOOD":
            #add that vote to the database
        #else:
            #raise ValueError("vote should be \"BAD\" or \"GOOD\"")


class Song:

        def __init__(self, name, artist, location):
            self.title = name
            self.artist = artist
            self.location = location




db = Database()
con = db.con
cur = con.cursor()


def get_all_songs():
    song_details = 'SELECT * FROM songs;'
    cur.execute(song_details)
    musics = []
    for row in cur:
        location = row[1]
        name = row[2]
        artist = row[3]
        musics.append(Song(name,artist,location))
    return musics

def vote(input):
    if input[2] == 0:
        cur.execute('''INSERT INTO votes VALUES ({}, 'down');'''.format(input[1]))
    else:
        cur.execute('''INSERT INTO votes VALUES ({}, 'up');'''.format(input[1]))
