#coding=utf-8

import requests
import pandas
import time

headers = {
    'authorization':'',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
}

user_data = []
def get_user_data(page):
    for i in range(page):
        url = 'https://www.zhihu.com/api/v4/members/fanclover/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'.format(i*20)
        response = requests.get(url,headers=headers).json()['data']
        user_data.extend(response)
        print("正在爬取第%s页" % str(i+1))
        time.sleep(3)

if __name__ == '__main__':
    get_user_data(3)
    df = pandas.DataFrame.from_dict(user_data)
    df.to_csv('user_all.csv')