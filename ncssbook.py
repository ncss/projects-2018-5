#!/usr/bin/env python3
from tornado.ncss import Server
from TemplatingParser import templatingParser
import json
import API


def index(response):
    response.write('''<h1>Hello fellow students</h1>
    <ul>
        <li><a href="/style-guide">Style Guide</a></li>
        <li><a href="/song-player">Song Player</a></li>
        <li><a href="/profile">Profile</a></li>
        <li><a href="/header">Header here</a></li>
        <li><a href="/footer">Footer here</a></li>
        <li><a href="/about">About page</a></li>
    </ul>
    ''')


def writeResponse(response, filename, context={}):
    response.write(templatingParser.translateToHTML(filename, context))


def profile(response):
    person = API.get_person()
    liked = person.good()
    disliked = person.bad()
    name = person.get_name()
    writeResponse(response, 'templates/profile.html', context={"liked" : liked, "disliked": disliked, "name": name})


def home(response):
    context = {
        "music": {
            "title": "SuperAwesomeSong",
            "artist": "SuperAwesomeSongWriter",
            "album": "SuperAwesomeAlbum",
            "tags": "Awesome"
        }
    }
    writeResponse(response, 'templates/home.html', context)


def style(response):
    writeResponse(response, 'templates/style.html')


def about(response):
    writeResponse(response, 'templates/about.html')


def songdb(response):
    out = []

    for music in API.get_all_songs():
        if music.location:
            out.append({"id" : music.id, "title": music.title, "artist": music.artist, "location": music.location, "coverlocation": music.cover})

    response.write(json.dumps(out))


def header(response):
    response.write('''
<!DOCTYPE html>
<head>
<Title>Header</Title>
</head>
<body>
<a href="/" img src="" alt="This will be logo">
<h3>{{ Person.name() }}</h3>
</body>
    ''')


def footer(response):
    response.write('''
<!DOCTYPE html>
<head>
<Title>Footer</Title>
</head>
<body>
<li><a href="/about"> About </a></li>
</body>
    ''')


def vote(response):
    user = response.get_field("user")  # simply "user" as for now
    song = response.get_field("song")  # Song ID
    vote = response.get_field("vote")  # 1:UP,0:DOWN
    params = [user, song, vote]
    respDict = {"user": user, "song": song, "vote": vote}
    respDict["success"] = API.vote(params)
    response.write(respDict)

def fourofourhandler(response):
    writeResponse(response, 'templates/404.html')


server = Server()
server.register('/', home)
server.register('/profile', profile)
server.register('/style-guide', style)
server.register('/song-player', index)
server.register('/about', about)
server.register('/vote', vote)
server.register('/songdb', songdb)
server.register(r'/.+', fourofourhandler)
server.run()
