#!/usr/bin/env python3
from tornado.ncss import Server


def index(response):
    response.write('''<h1>Hello fellow students</h1>
    <a href="/style-guide">Style Guide Here</a>
    <p>from <span style="color: #cccccc;">Group 5</span></p>''')

def style_guide(response):
    response.write('''
<!DOCTYPE html>
<body>
<h1> Style Guide </h1>
<a href="/">Home</a>
</body>


    ''')

server = Server()
server.register('/', index)
server.register('/style-guide',style_guide)
server.run()
