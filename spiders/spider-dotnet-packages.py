import scrapy
import re

class DotNetSpider(scrapy.Spider):
    name = 'dotnet-spider'
    start_urls = ['https://www.nuget.org/packages']
    allowed_domains = ['nuget.org']
    
    def parse(self, response):
        for package in response.xpath('//section[@class="package"]'):
            name = package.xpath('.//h1/a/text()').extract_first().strip()
            url = package.xpath('.//h1/a/@href').extract_first()
            day = package.xpath('.//time/text()').extract_first()
            maintainer = ""
            release = ""
            description = package.xpath('.//article/p[2]/text()').extract_first()
            if description is None:
                description=""
            yield {'language': '.Net',
                       'day': day.strip(),
                       'name': name.replace("-" + release, ""),
                       'maintainer': maintainer,
                       'release': release,
                       'description': description.replace("\n", " ").replace("\t", " ").strip(),
                       'url': response.urljoin(url)}

