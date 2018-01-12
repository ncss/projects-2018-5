#!/usr/bin/env python3
from tornado.ncss import Server


def index(response):
    response.write('''<h1>Hello fellow students</h1>
    <a href="/style-guide">Style Guide Here</a>
    <p>from <span style="color: #cccccc;">Group 5</span></p>''')

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

server = Server()
server.register('/', index)
server.register('/style-guide',style_guide)
server.run()
