import sqlite3
conn = sqlite3.connect('ncssbook.db')
cur = conn.cursor()

create_db = '''CREATE DATABASE ncssbook;
CREATE SCHEMA project;'''

create_votes = '''CREATE TABLE votes (
	song-id INTEGER,
	vote TEXT,
);
'''

create_songs = '''CREATE TABLE songs (
	id INTEGER,
	location TEXT,
	title TEXT,
	artist TEXT
);
'''

cur.execute(create_db)
cur.execute(create_votes)
cur.execute(create_songs)
