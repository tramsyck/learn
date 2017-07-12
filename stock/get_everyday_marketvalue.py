#!/usr/bin/env python
#coding=utf8

#########################
# 获取股票的每天的市值
# Date: 2017-7-10
########################


import requests
from bs4 import BeautifulSoup 

#url = http://vip.stock.finance.sina.com.cn/quotes_service/view/vMS_tradehistory.php?symbol=sh600321&date=2017-07-07
def get_stock_history_info(stockid, date):
    url = "http://vip.stock.finance.sina.com.cn/quotes_service/view/vMS_tradehi\
story.php?symbol={}&date={}".format(stockid, date)
    res = requests.get(url)
    res.encoding = 'gbk' 
    print res.text 
    soup = BeautifulSoup(res.text, 'html.parser')
    r = soup.select('#hqDetails > table > tbody > tr:nth-of-type(3) > td:nth-of-type(2)::text ')
    print r


 
if __name__ == '__main__':
     get_stock_history_info('sz000651','2017-03-31')
