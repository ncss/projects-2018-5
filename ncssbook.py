#!/usr/bin/env python3
from tornado.ncss import Server


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
    <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,400i,500,600,800" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link href="/static/css/styleguide.css" rel="stylesheet"/>
</head>
<body>

    <header>
        <h1> Style Guide </h1>
        <a href="/">Home</a>
    </header>
    <div class="page">
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
            <div class="icons">
                <i class="material-icons">thumb_down</i>
                <i class="material-icons">thumb_up</i>
                <i class="material-icons">pause</i>
                <i class="material-icons">play_arrow</i>
            </div>
            <ul>
            <li>Tim</li>
            <li>James</li>
            <li>Nicky</li>
            <li>Bruce</li>
            </ul>
    </div>
</body>


    ''')

def about(response):
    with open("templates/about.html") as f:
        response.write(f.read())


def song_player(response):
    response.write('''
    <!DOCTYPE html>
    {%include header.html}
    <head>
    <Title>Song Player</Title>
    <link href="https://use.fontawesome.com/releases/v5.0.3/css/all.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

    </head>
    <body>
    <h2><a href="/"> Return to Index</a></h2>
    <h1>{{ Music.title() }}</h1>
    <ul>
        <li>{{ Music.title() }}</li>
        <li>{{ Music.artist() }}</li>
        <li>{{ Music.album() }}</li>
        <li>{{ Music.tags() }}</li>
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
    <button><i class="material-icons">thumb_down</i></button>
    <button><i class="material-icons">thumb_up</i></button>
    </body>
    {% include footer.html %}


    ''')

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
server.register('/style-guide',style_guide)
server.register('/song-player',song_player)
server.register('/about', about)
server.register('/header',header)
server.register('/footer',footer)
server.run()
