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

server = Server()
server.register('/', index)
server.register('/style-guide',style_guide)
server.run()
