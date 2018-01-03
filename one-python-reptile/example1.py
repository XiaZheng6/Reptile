#encoding='utf-8'
#SETUP1:  get_data
import requests

r = requests.get('https://book.douban.com/subject/1084336/comments/').text


#SETUP2:  analytical_data
from bs4 import BeautifulSoup
soup = BeautifulSoup(r,'lxml')
pattern = soup.find_all('p','comment-content')
for item in pattern:
	print item.string


#SETUP3:  save_data
import pandas
comments = []
for item in pattern:
	comments.append(item.string)
df = pandas.DataFrame(comments)
df.to_csv('comments.csv')
