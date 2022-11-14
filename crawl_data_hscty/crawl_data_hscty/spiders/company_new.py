import scrapy
from crawl_data_hscty.items import CrawlDataHsctyItem
from scrapy import spiderloader    
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

class DataAprilSpider(scrapy.Spider):
    name = 'data_april'
    allowed_domains = ['hosocongty.vn']
    start_urls = ['https://hosocongty.vn/thang-04/2022-ho-chi-minh/page-%s' % page for page in range(1,229)]

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'April.csv'
    }

    def parse(self, response):
        items = CrawlDataHsctyItem()
        company_create_in_april = 'April'    
        companies_name = response.xpath('/html/body/div/div/div/div/div/div/ul[@class = "hsdn"]/li/h3/a/text()').extract()
        companies_code = response.xpath('/html/body/div/div/div/div/div/div/ul[@class = "hsdn"]/li/div/a/text()').extract()
        hosocty1 = zip(companies_name,companies_code)

        for hosocty in hosocty1 :
            items['month_create'] = company_create_in_april
            items['company_name'] = hosocty[0]
            items['company_code'] = hosocty[1]
            yield items

class DataMaySpider(scrapy.Spider):
    name = 'data_may'
    allowed_domains = ['hosocongty.vn']
    start_urls = ['https://hosocongty.vn/thang-05/2022-ho-chi-minh/page-%s' % page for page in range(1,242)]

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'May.csv'
    }

    def parse(self, response):
        items = CrawlDataHsctyItem()
        company_create_in_may = 'May'
        companies_name = response.xpath('/html/body/div/div/div/div/div/div/ul[@class = "hsdn"]/li/h3/a/text()').extract()
        companies_code = response.xpath('/html/body/div/div/div/div/div/div/ul[@class = "hsdn"]/li/div/a/text()').extract()
        hosocty1 = zip(companies_name,companies_code)

        for hosocty in hosocty1 :
            items['month_create'] = company_create_in_may
            items['company_name'] = hosocty[0]
            items['company_code'] = hosocty[1]
            yield items

class DataJuneSpider(scrapy.Spider):
    name = 'data_june'
    allowed_domains = ['hosocongty.vn']
    start_urls = ['https://hosocongty.vn/thang-06/2022-ho-chi-minh/page-%s' % page for page in range(1,236)]

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'June.csv'
    }

    def parse(self, response):
        items = CrawlDataHsctyItem()
        company_create_in_june = 'June'    
        companies_name = response.xpath('/html/body/div/div/div/div/div/div/ul[@class = "hsdn"]/li/h3/a/text()').extract()
        companies_code = response.xpath('/html/body/div/div/div/div/div/div/ul[@class = "hsdn"]/li/div/a/text()').extract()
        hosocty1 = zip(companies_name,companies_code)

        for hosocty in hosocty1 :
            items['month_create'] = company_create_in_june
            items['company_name'] = hosocty[0]
            items['company_code'] = hosocty[1]
            yield items

settings = get_project_settings()
process = CrawlerProcess(settings)
spider_loader = spiderloader.SpiderLoader.from_settings(settings)

for spider_name in spider_loader.list():
    print("Running spider %s" % (spider_name))
    process.crawl(spider_name)
process.start()

# process = CrawlerProcess()
# process.crawl(DataAprilSpider)
# process.crawl(DataMaySpider)
# process.crawl(DataJuneSpider)
# process.start()