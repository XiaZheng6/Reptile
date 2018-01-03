import requests


r = requests.get('http://www.baidu.com')


>>> r.status_code
200
>>> r.text
'xxxxxxxxxx'
>>> r.content
'xxxxxxxxxxxxxxx'
>>> r.encoding
'ISO-8859-1'
>>> r.apparent_encoding
'utf-8'
