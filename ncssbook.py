#!/usr/bin/env python3
from tornado.ncss import Server
from TemplatingParser import templatingParser

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
    writeResponse(response, 'templates/profile.html')

def home(response):
    context = {
        "music" : {
            "title" : "SuperAwesomeSong",
            "artist": "SuperAwesomeSongWriter",
            "album" : "SuperAwesomeAlbum",
            "tags" : "Awesome"
        }
    }
    writeResponse(response, 'templates/home.html', context)

def style(response):
    writeResponse(response, 'templates/style.html')

def about(response):
    with open("templates/about.html") as f:
        response.write(f.read())


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

server = Server()
server.register('/', index)
server.register('/profile', profile)
server.register('/style-guide',style)
server.register('/song-player',home)
server.register('/about', about)
server.register('/header',header)
server.register('/footer',footer)
server.run()
