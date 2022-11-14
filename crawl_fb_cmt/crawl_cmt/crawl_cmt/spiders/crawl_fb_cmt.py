import scrapy 
from crawl_cmt.items import CrawlCmtItem
from crawl_cmt.crawl_cmt.items import CrawlCmtItem

class CrawlFbCmtSpider(scrapy.Spider):
    name = 'crawl_fb_cmt'
    allowed_domains = ['www.facebook.com']
    start_urls = ['https://www.facebook.com/']

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'cmt.csv'
    }

    def parse(self, response):
        items = CrawlCmtItem()
        user_name = response.xpath('//*[@id="mount_0_0_Gx"]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div[4]/div/div/div[2]/ul/li[1]/div[1]/div[2]/div/div[1]/div/div/div/div/span[1]/span')
        comment = response.xpath('//*[@id="mount_0_0_Gx"]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div[4]/div/div/div[2]/ul/li[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div/span/div')
        cmt1 = zip(user_name, comment)

        for cmt in cmt1:
            items['UserName'] = cmt[0]
            items['Comment'] = cmt[1]

