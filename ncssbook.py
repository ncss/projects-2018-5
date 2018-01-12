#!/usr/bin/env python3
from tornado.ncss import Server


def index(response):
    response.write('''<h1>Hello fellow students</h1>
<<<<<<< HEAD
    <a href="/style-guide">Style Guide Here</a>
    <a href="/song-player">Song Player Here</a>
    <a href="/header">Header here</a>
    <a href="/footer">Footer here</a>
=======
    <form action="/style-guide">
        <input type="submit" value="Style Guide Here" />
    </form>
    <form action="/song-player">
        <input type="submit" value="Song Player Here" />
    </form>
>>>>>>> origin/Song-Page
    <p>from <span style="color: #cccccc;">Group 5</span></p>''')

def style_guide(response):
    response.write('''
<!DOCTYPE html>
<head>
<link href="/static/css/styleguide.css" rel="stylesheet"/>
</head>
<body>
<h1> Style Guide </h1>
<a href="/">Home</a>

<h1>This is a level 1 heading.</h1>
<h2>This is a level 2 heading.</h2>
<p>This is a paragraph.</p>

</body>


    ''')

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
server.register('/style-guide',style_guide)
server.register('/song-player',song_player)
server.register('/header',header)
server.register('/footer',footer)
server.run()
