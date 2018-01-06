#coding=utf-8

import requests

url = 'https://www.xxxxxxxx/api/v4/members/fanclover/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=40&limit=20'
response = requests.get(url).text

print(response)
