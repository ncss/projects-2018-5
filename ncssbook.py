#!/usr/bin/env python3
from tornado.ncss import Server


def index(response):
    response.write('<h1>Hello fellow students</h1><p>from <span style="color: #cccccc;">Group 5</span></p>')
def profile(response):
    with open('templates/profile_page.html') as f:
        response.write(f.read())


server = Server()
server.register('/', index)
server.register('/profile', profile)
server.run()
