#!/usr/bin/env python3
from tornado.ncss import Server


def index(response):
    response.write('<h1>Hello fellow students</h1><p>from <span style="color: #cccccc;">Group 5</span></p><img src="https://static.groklearning-cdn.com/static/images/marketing/about/james-2017-07@2x.png">')


server = Server()
server.register('/', index)
server.run()
