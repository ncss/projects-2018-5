#!/usr/bin/env python3
from tornado.ncss import Server


def index(response):
    response.write('<h1>Hello fellow students</h1><p>from <span style="color: #cccccc;">Group 5</span></p>')
def profile(response):
    with open('templates/profile_page.html') as f:
        response.write(f.read())

def profile(response):
    with open("templates/profile.html") as f:
        response.write(f.read())

def style_guide(response):
    response.write('''
<!DOCTYPE html>
<head>
    <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,400i,600,800" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link href="/static/css/styleguide.css" rel="stylesheet"/>
</head>
<body>

    <header>
        <h1> Style Guide </h1>
        <a href="/">Home</a>
    </header>
    <h1>This is a level 1 heading.</h1>
    <h2>This is a level 2 heading.</h2>
    <h3> This is a level 3 heading.</h3>
    <p>This is a paragraph.</p>
    <ol>
        <li>Song 1</li>
        <li>Song number 2</li>
        <li>Song #3</li>
        <li>Fourth Song</li>
    </ol>

    <ul>
        <li>Tim</li>
        <li>James</li>
        <li>Nicky</li>
        <li>Bruce</li>
    </ul>
    <i class="material-icons mats">thumb_down</i>
    <i class="material-icons">thumb_up</i>
    <i class="material-icons">pause</i>
    <i class="material-icons">play_arrow</i>
</body>


    ''')

def about(response):
    with open("templates/about.html") as f:
        response.write(f.read())


def song_player(response):
    response.write('''
    <!DOCTYPE html>
    <head>
    <Title>Song Player </Title>
    <link href="https://use.fontawesome.com/releases/v5.0.3/css/all.css" rel="stylesheet">
    </head>
    <body>
    <h1>Song Name</h1>
    <h2><a href="/"> Return to Index</a></h2>
    <ul>
        <li>Song Title</li>
        <li>Song Artist</li>
    </ul>
    <figure>
        <figcaption>This will be Album Cover</figcaption>
    </figure>
    <h1>Users Who Liked This:</h1>
    <ul>
        <li>Bob</li>
        <li>Cindy</li>
        <li>Jelly</li>
        <li>JimJim</li>
        <li>jamjam</li>
        <li>Em</li>
        <li>Sam</li>
        <li>Billy</li>
        <li>Bob</li>
    </ul>
    <p1 style="font-size:500%;""><i class="far fa-thumbs-down"></i>   <i class="far fa-play-circle"></i>  <i class="far fa-thumbs-up"></i></p1>
    </body>


    ''')

def header(response):
    response.write('''
<!DOCTYPE html>
<head>
<Title>Header</Title>
</head>
<body><img src=""
alt="This will be logo">
<h3>This will be Username</h3>
</body>
    ''')

def footer(response):
    response.write('''
<!DOCTYPE html>
<head>
<Title>Footer</Title>
</head>
<body>
<p1>Whatever we are actually putting in footer</p1>
</body>
    ''')

server = Server()
server.register('/', index)
server.register('/profile', profile)
server.register('/style-guide',style_guide)
server.register('/song-player',song_player)
server.register('/about', about)
server.register('/header',header)
server.register('/footer',footer)
server.run()
