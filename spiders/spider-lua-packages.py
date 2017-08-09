import scrapy
import re

class LuaSpider(scrapy.Spider):
    name = 'lua-spider'
    start_urls = ['https://luarocks.org/m/root/recent']
    allowed_domains = ['luarocks.org']
    
    def parse(self, response):
        for package in response.xpath('//div[@class="version_row"]'):
            name = package.xpath('./a[1]/text()').extract_first().strip()
            url = package.xpath('./a[1]/@href').extract_first()
            day = package.xpath('./span[@class="created_at"]/text()').extract_first()
            maintainer = package.xpath('./a[@class="author"]/text()').extract_first()
            release = package.xpath('./span[@class="version_name"]/text()').extract_first()
            description = ""
            yield {'language': 'Lua',
                       'day': day.strip(),
                       'name': name.replace("-" + release, ""),
                       'maintainer': maintainer,
                       'release': release,
                       'description': description.strip(),
                       'url': response.urljoin(url)}

