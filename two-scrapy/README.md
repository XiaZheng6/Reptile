# scrapy

## startproject

```
[root@iZ2zeb0d9lqofqcc2s88arZ ~]# scrapy startproject city_58
New Scrapy project 'city_58', using template directory '/usr/lib64/python3.6/site-packages/scrapy/templates/project', created in:
    /root/city_58

You can start your first spider with:
    cd city_58
    scrapy genspider example example.com

[root@iZ2zeb0d9lqofqcc2s88arZ ~]# cd city_58/
[root@iZ2zeb0d9lqofqcc2s88arZ city_58]# ls
city_58  scrapy.cfg

[root@iZ2zeb0d9lqofqcc2s88arZ city_58]# tree
.
├── city_58
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── __pycache__
│   ├── settings.py
│   └── spiders
│       ├── __init__.py
│       └── __pycache__
└── scrapy.cfg

4 directories, 7 files

```

## genspider
```
[root@iZ2zeb0d9lqofqcc2s88arZ city_58]# scrapy genspider spider_city_58 58.com
Created spider 'spider_city_58' using template 'basic' in module:
  city_58.spiders.spider_city_58
[root@iZ2zeb0d9lqofqcc2s88arZ city_58]# ls
city_58  scrapy.cfg
[root@iZ2zeb0d9lqofqcc2s88arZ city_58]# cd city_58/
[root@iZ2zeb0d9lqofqcc2s88arZ city_58]# ls
__init__.py  items.py  middlewares.py  pipelines.py  __pycache__  settings.py  spiders
[root@iZ2zeb0d9lqofqcc2s88arZ city_58]# cd spiders/
[root@iZ2zeb0d9lqofqcc2s88arZ spiders]# ls
__init__.py  __pycache__  spider_city_58.py
[root@iZ2zeb0d9lqofqcc2s88arZ spiders]# cat spider_city_58.py 
# -*- coding: utf-8 -*-
import scrapy


class SpiderCity58Spider(scrapy.Spider):
    name = 'spider_city_58'
    allowed_domains = ['58.com']
    start_urls = ['http://58.com/']

    def parse(self, response):
        pass

```
