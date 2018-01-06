## 运行流程
> 图解
1. Spiders发送第一个URL给引擎
2. 引擎从Spider中获取到第一个要爬取的URL后，在调度器(Scheduler)以Request调度
3. 调度器把需要爬取的request返回给引擎
4. 引擎将request通过下载中间件发给下载器(Downloader)去互联网下载数据
5. 一旦数据下载完毕，下载器获取由互联网服务器发回来的Response，并将其通过下载中间件发送给引擎
6. 引擎从下载器中接收到Response并通过Spider中间件发送给Spider处理
7. Spider处理Response并从中返回匹配到的Item及(跟进的)新的Request给引擎
8. 引擎将(Spider返回的)爬取到的Item给Item Pipeline做数据处理或者入库保存，将(Spider返回的)Request给调度器入队列
9. (从第三步)重复直到调度器中没有更多的request
