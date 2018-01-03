import requests
from lxml import etree

url = 'https://book.douban.com/subject/1084336/comments/'
r = requests.get(url).text
# print r 
s = etree.HTML(r)

print s.xpath('//*[@id="comments"]/ul/li[1]/div[2]/p/text()')