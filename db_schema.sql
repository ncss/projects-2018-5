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
	