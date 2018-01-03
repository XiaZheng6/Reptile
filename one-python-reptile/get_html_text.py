

import requests

def getHTMLText(url):
	try:
		r = requests.get(url,timeout=20)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except :
		return "error"


if __name__ == '__main__':
	url = 'https://api.genedock.com/'
	print getHTMLText(url)