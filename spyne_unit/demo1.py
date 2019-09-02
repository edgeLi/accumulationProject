#!/usr/bin/python
# -*- coding:utf-8 -*-

from spyne import Application
from spyne import rpc
from spyne import ServerBase
from spyne import Iterable,Integer,Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


class HelloWorldService(ServerBase):
    @rpc(Unicode,Integer,_return=Iterable(Unicode))
    def say_hello(self,name,times):
        for i in range(times):
            yield u'Hello,%s' % name

soap_app = Application([HelloWorldService],'spyne.examples.hello.soap',in_protocol=Soap11(valiator="lxml"),out_protocol=Soap11())


wsgi_app = WsgiApplication(soap_app)

if __name__ == "__main__":
    import logging
    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)
    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1',8000, wsgi_app)
    server.serve_forever()