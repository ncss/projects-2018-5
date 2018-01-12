CREATE DATABASE ncssbook;
CREATE SCHEMA project;

CREATE TABLE votes (
	song-id INTEGER,
	vote TEXT,
);
	
CREATE TABLE songs (
	id INTEGER,
	location TEXT,
	title TEXT,
	artist TEXT
);

INSERT INTO songs VALUES (1, '', 'Havana', 'Camilla Cabello'),
(2, '', 'Paradise', 'Coldplay'),
(3,  '', 'Blank Space', 'Taylor Swift')
(4, '', 'Achilles Come Down', 'Gang of Youths'),
(5, '', 'The Final Countdown', 'James Curran'),
(6, '', 'Bohemian Rhapsody', 'Queen'),
(7, '', 'Thunder', 'Imagine Dragons'),
(8, '', 'Short Circuit', 'Daft Punk'),
(9, '', 'Hotline Bling', 'Drake'),
(10, '', 'The A Team', 'Ed Sheeran')
;
	
INSERT INTO votes VALUES (1, 'up'),
(2, 'down'),
(3, 'up'),
(4, 'up'),
(5, 'down'),
(6, 'up'),
(7, 'down'),
(8, 'down'),
(9, 'up'),
(10, 'down')
;

