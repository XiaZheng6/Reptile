## Robots协议
### https://www.zhihu.com/robots.txt
```
# 禁止今日头条和悟空问答爬虫抓取知乎网站内容
User-agent: *
Request-rate: 1/2 # load 1 page per 2 seconds
Crawl-delay: 10

Disallow: /login
Disallow: /logout
Disallow: /resetpassword
Disallow: /terms
Disallow: /search
Disallow: /notifications
Disallow: /settings
Disallow: /inbox
Disallow: /admin_inbox
Disallow: /*?guide*
Disallow: /people/*
```

### https://www.jd.com/robots.txt
```
User-agent: * 
Disallow: /?* 
Disallow: /pop/*.html 
Disallow: /pinpai/*.html?* 
User-agent: EtaoSpider 
Disallow: / 
User-agent: HuihuiSpider 
Disallow: / 
User-agent: GwdangSpider 
Disallow: / 
User-agent: WochachaSpider 
Disallow: /
```
