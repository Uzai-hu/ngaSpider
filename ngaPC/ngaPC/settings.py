# -*- coding: utf-8 -*-

# Scrapy settings for ngaPC project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ngaPC'

SPIDER_MODULES = ['ngaPC.spiders']
NEWSPIDER_MODULE = 'ngaPC.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ngaPC (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Host':'nga.178.com',
'Connection':'keep-alive',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer':'http://nga.178.com/nuke.php?func=ucp&uid=42437889',
'Accept-Encoding':'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8',
'Cookie':'weiba_guide=weiba_guide; Hm_lvt_60031dda34b454306f907cbac1fb2081=1490174374; CNZZDATA1259004010=532973600-1500523434-http%253A%252F%252Fnga.178.com%252F%7C1500523434; UM_distinctid=15e4c16d00939c-0a7915abd745ca-31637e01-2a3000-15e4c16d00ac; __utmz=65687473.1505958030.553.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none); _e=31536000; CNZZDATA1256638869=1699580066-1509097326-http%253A%252F%252Fnga.178.com%252F%7C1511850006; __utma=65687473.2091384596.1461108710.1512440236.1512442719.651; CNZZDATA1256638919=1215248952-1469691399-http%253A%252F%252Fbbs.bigccq.cn%252F%7C1512624390; CNZZDATA1256638851=202847308-1461105759-http%253A%252F%252Fbbs.bigccq.cn%252F%7C1513563734; Hm_lvt_efa0bf813242f01d2e1c0da09e3526bd=1513579457; __wmbgid=sa4dd84d5abtz5l7p568fol2njoy82l1; CNZZDATA1264400273=1700367300-1508318745-http%253A%252F%252Fnga.178.com%252F%7C1513583673; CNZZDATA1256638943=1752948257-1469772004-http%253A%252F%252Fbbs.bigccq.cn%252F%7C1513668577; CNZZDATA1256638915=1362133799-1513758936-http%253A%252F%252Fnga.178.com%252F%7C1513758936; _178i=1; CNZZDATA1256638874=2120427837-1508139961-http%253A%252F%252Fnga.178.com%252F%7C1514890283; bbsmisccookies=%7B%22insad_refreshid%22%3A%7B0%3A%22/958d316f42d48ee579e36873%22%2C1%3A1515461110%7D%7D; CNZZDATA1262314555=210071853-1499319319-http%253A%252F%252Fnga.178.com%252F%7C1514946131; CNZZDATA1256638924=990097088-1461113128-http%253A%252F%252Fbbs.bigccq.cn%252F%7C1514948599; CNZZDATA1256638820=574939486-1479718564-http%253A%252F%252Fnga.178.com%252F%7C1515038794; CNZZDATA1256638828=397345234-1461105438-http%253A%252F%252Fbbs.bigccq.cn%252F%7C1515035075; CNZZDATA30043604=cnzz_eid%3D977382771-1461104056-null%26ntime%3D1515043717; CNZZDATA30039253=cnzz_eid%3D1654229514-1461104653-null%26ntime%3D1515048915; lastpath=/thread.php?searchpost=1&authorid=42437889; ngacn0comUserInfo=POWERHUZY%09POWERHUZY%0942%0942%09%09-17%0915639%094%090%090%0916_-450%2C67_100%2C85_-150%2C61_2; ngacn0comUserInfoCheck=a43a45e9a1139ad06002473dec55eaea; ngacn0comInfoCheckTime=1515049070; ngaPassportUid=1376077; ngaPassportUrlencodedUname=POWERHUZY; ngaPassportCid=e173e35512a058848b5be6543486910f6a6fbd77; lastvisit=1515049080'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ngaPC.middlewares.NgapcSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'ngaPC.middlewares.NgapcDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'ngaPC.pipelines.NgapcPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
