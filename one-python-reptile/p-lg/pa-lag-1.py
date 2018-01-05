#coding=utf-8


from pymongo import MongoClient
import requests

client = MongoClient('mongodb://')
db = client.reptile
my_set = db.lagou

url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0'
payload = {
	'first':'true',
	'pn':'1',
	'kd':'python运维'
}
headers = {
	'Cookie':'',
	'User-Agent':'',
	'Referer':'',
}

repsponse = requests.post(url, data = payload, headers = headers)
my_set.insert(repsponse.json()['content']['positionResult']['result'])
