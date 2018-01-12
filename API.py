import random
import re
import sqlite3


class Database:
    def __init__(self):
        con = sqlite3.connect("ncssbook.db")
        cur = conn.cursor()

    def reboot(self):
        cur.close()
        con.close()
        con = sqlite3.connect("ncssbook.db")
        cur = conn.cursor()

    def rand_music():
        pass
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

    def __init__(self, good, bad):
        self.name = "James" #get the current users username
        self.good = [] #get liked song ids
        self.bad = [] #get disliked song ids

    def name(self):
        return(self.name)
    
    def good(self):
        return(self.good)
    
    def bad(self):
        return(self.good)

    def add_song(self, vote):
        if vote == "BAD":
            #add that vote to the database
        elif vote == "GOOD":
            #add that vote to the database
        else:
            raise ValueError("vote should be \"BAD\" or \"GOOD\"")

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
    
        def __init__(self):
            self.name = #name
            self.artist = #artist
            self.location = #location

        def title(self):
            return(self.title)

        def artist(self):
            return(self.artist)

        #def music(self):
            #return(self.location)

        

