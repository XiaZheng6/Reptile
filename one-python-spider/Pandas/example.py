#coding=utf-8

import requests
from lxml import etree
import pandas

url = 'https://book.douban.com/subject/1084336/comments/'
r = requests.get(url).text

s = etree.HTML(r)
file = s.xpath('//*[@id="comments"]/ul/li/div[2]/p/text()')

df = pandas.DataFrame(file)
df.to_csv('pinglun.csv')
