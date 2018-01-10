#!/usr/bin/env python3
from tornado.ncss import Server


def index(response):
    response.write('Hello my dudes from Group 5')


server = Server()
server.register('/', index)
server.run()
