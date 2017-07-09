#!/usr/bin/env python
#coding=utf8
# 获取所有股票的代码，并存到文件或者数据库中
# Date : 2017-7-9


import re
import requests

url = 'http://quote.eastmoney.com/stocklist.html'
res = requests.get(url)
res.encoding = 'gbk'
#print res.text
#正则查找股票代码
#//*[@id="quotesearch"]/ul[2]/li[51]/a
t = '<a target="_blank" href="http://quote.eastmoney.com/sz000058.html">深赛格(000058)</a>'
pattern = r'<a target="_blank" href="http://quote.eastmoney.com/s[z|h)](\d+?).html">(.*?)\(\1\)</a>'

m = re.findall(pattern, res.text)

for item in m:
    if item[0].startswith(('3','6','0')):
        print item[0], item[1]
