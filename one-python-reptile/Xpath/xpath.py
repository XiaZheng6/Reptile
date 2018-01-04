#coding=utf-8

import requests
from lxml import etree

url = 'https://book.douban.com/subject/1084336/comments/'
r = requests.get(url).text

s = etree.HTML(r)

#print (s.xpath('//*[@id="comments"]/ul/li/div[2]/p/text()'))
file = s.xpath('//*[@id="comments"]/ul/li/div[2]/p/text()')

with open('pinglun.txt','w',encoding='utf-8') as f:
    for i in file:
        f.write(i)
