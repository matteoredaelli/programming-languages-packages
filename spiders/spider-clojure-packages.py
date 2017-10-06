import scrapy
import re

class ClojureSpider(scrapy.Spider):
    name = 'clojure-spider'
    start_urls = ['https://clojars.org/']
    allowed_domains = ['clojars.org']

    def parse(self, response):
        for package in response.xpath('//div[@class="recent-jar"]'):
            name = package.xpath('.//a[1]/text()').extract_first().strip()
            url = package.xpath('.//a[1]/@href').extract_first()
            #day = package.xpath('./span[@class="created_at"]/text()').extract_first()
            #maintainer = package.xpath('./a[@class="author"]/text()').extract_first()
            #release = package.xpath('./span[@class="version_name"]/text()').extract_first()
            description = response.xpath('.//p[@class="recent-jar-description"]/text()').extract_first().strip()
            yield {'language': 'Clojure',
                       #'day': day.strip(),
                       'name': name,
                       #'maintainer': maintainer,
                       #'release': release,
                       'description': description.strip(),
                       'url': response.urljoin(url)}
