#!/usr/bin/env python
#coding=utf8

import threading

def count(n):
    c = 0
    for i in xrange(n):
        c += i
    print c
    return c

count(10000000)
count(10000000)
t1 = threading.Thread(target=count, args=(10000000,))
t2 = threading.Thread(target=count, args=(10000000,))

t1.start()
t2.start()


