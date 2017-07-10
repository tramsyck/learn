# BS4解析Html
from bs4 import BeautifulSoup
fp = open("index.html")
soup1 = BeautifulSoup(fp)
soup2 = BeautifulSoup("<html>data</html>")


lxml
 from lxml import etree

   selector = etree.HTML(html)
     links = selector.xpath('//h4/a/text()')
       for link in links:
             print link
