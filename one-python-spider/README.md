# Python爬虫入门
### 如何写爬虫
* 获得源码（Requests）
* 解析源码（Beautiful Soup or Xpath）
* 保存数据（MongoDB）

### 通用的网络爬虫框架
* 选取挑选的种子URL
* 将这些URL放入待抓取URL队列
* 取出待抓取的URL，下载，存储进已下载网页库中。此外，将这些URL放进已抓取URL队列
* 分析已抓取队列中的URL，并且将URL放入待抓取URL队列，从而进入下一个循环

### 爬虫的知识体系
* 前端html,css,js,浏览器相关知识
* 各种数据库的运用
* http协议
* 前后台联动的方案
