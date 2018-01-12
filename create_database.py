import sqlite3
conn = sqlite3.connect('ncssbook.db')
cur = conn.cursor()

#create_db = '''CREATE DATABASE ncssbook;
#CREATE SCHEMA project;'''


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
	id INTEGER,
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

#cur.execute(create_db)
cur.execute(drop_votes)
cur.execute(create_votes)
cur.execute(drop_songs)
cur.execute(create_songs)
cur.execute(insert_songs)
cur.execute(insert_votes)

cur.execute('SELECT * FROM songs;')
for row in cur:
    print(row)
