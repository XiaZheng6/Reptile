#coding-utf-8

from pymongo import MongoClient
from fake_useragent import UserAgent
import requests
import time

client = MongoClient('mongodb://')
db = client.reptile
my_set = db.lagou

headers = {
			'Cookie':'',
			'Referer':'https://xxxxxxxx/jobs/list_python%E8%BF%90%E7%BB%B4?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=',
		}


def get_python_op(page, kd):
	for i in range(page):
		url = 'https://xxxxxxxxm/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0'
		payload = {
			'first':'true',
			'pn':i,
			'kd':kd,
		}
		ua = UserAgent()
		headers['User-Agent'] = ua.random
		repsponse = requests.post(url, data = payload, headers = headers)

		if repsponse.status_code == 200:
			py_op_json = repsponse.json()['content']['positionResult']['result']
			my_set.insert(py_op_json)
		else:
			print('something wrong!!!')
		print("正在爬取第%s页" % str(i+1))
		time.sleep(3)

if __name__ == '__main__':
	get_python_op(31, 'python运维')
