import random
import re
import sqlite3

#cur = sqlite3.cursor()
class Database:
    def __init__(self):
        self.con = sqlite3.connect("ncssbook.db")

    def reboot(self):
        self.con.close()
        self.con = sqlite3.connect("ncssbook.db")

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
    
    def good(self):
        return(self.good)
    
    def bad(self):
        return(self.good)

    #def add_song(self, vote):
        #if vote == "BAD":
            #add that vote to the database
        #elif vote == "GOOD":
            #add that vote to the database
        #else:
            #raise ValueError("vote should be \"BAD\" or \"GOOD\"")

    def voted_song(self, vsong):
        for songs in self.bad:
            for song in self.bad[songs]:
                if song == vsong:
                    return True
        for songs in self.good:
            for song in self.good[songs]:
                if song == vsong:
                    return True
        return False

class Music:
    
        def __init__(self, name, artist, location):
            self.title = name
            self.artist = artist
            self.location = location


db = Database()
con = db.con
cur = con.cursor()
musics = []
song_details = 'SELECT * FROM songs;'
cur.execute(song_details)
for row in cur:
    location = row[1]
    name = row[2]
    artist = row[3]
    musics.append(Music(name,artist,location))
