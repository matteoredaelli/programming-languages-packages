import scrapy

#import sys, os
#sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
#import utils

class ScalaSpider(scrapy.Spider):
    name = 'scala-spider'
    start_urls = ['https://index.scala-lang.org/']
    allowed_domains = ['scala-lang.org']
    
    def parse(self, response):
        for package in response.xpath('//section[@class="recent-projects"][1]//div[@class="row"]/div'):
            name = package.xpath('.//h4/text()').extract_first()
            url = package.xpath('./a/@href').extract_first()
            day = "" #package.xpath('.//div[@class="content-project-body"]/text()').extract_first()
            description = package.xpath('.//p[@class="description"]/text()').extract_first()
            yield {'language': 'Scala',
                       'day': day,
                       'name': name,
                       'release': '',
                       'description': description,
                       'url': response.urljoin(url)}

