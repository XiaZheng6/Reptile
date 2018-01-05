#coding=utf-8

import requests
import pandas

headers = {
	'authorization':'',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
	'x-udid':'',
}

url = 'https://www.zhihu.com/api/v4/members/fanclover/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=40&limit=20'
response = requests.get(url,headers=headers).json()['data']

df = pandas.DataFrame.from_dict(response)
df.to_csv('user.csv')