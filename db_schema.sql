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
(3,  '', 'Blank Space', 'Taylor Swift');
	
INSERT INTO votes VALUES (1, 'up'),
(2, 'down'),
(3, 'up');