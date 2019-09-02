#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis as redis

host = "localhost"
port = 6379

r = redis.Redis(host=host,port=port)
r.set('foo','bar')
print(r.get('foo'))