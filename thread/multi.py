#!/usr/bin/env python
#coding=utf8
########################################
############## Info ####################
# Time:2017-7-9
# Author: Yc Jiang
# Purpose: learn multi thread/process
########################################


import threading
from multiprocessing.dummy import Pool as ThreadPool
import urllib2

usrls = [
    'https://www.douban.com',
    'https://www.douban.com',
    'https://www.douban.com',
    'https://www.douban.com',
    'http://www.baidu.com',
]
result = []
pool = ThreadPool(4)
#     pool.map(urllib2.urlopen, usrls)
result.append(pool.map_async(urllib2.urlopen,usrls)) 
pool.close()
pool.join()
for item in result:
    print len(result)
    print len(item.get(0))
#    0print item.get(0).pop().read()

