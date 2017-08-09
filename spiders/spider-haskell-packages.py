import scrapy
import re

class HaskellSpider(scrapy.Spider):
    name = 'haskell-spider'
    start_urls = ['http://hackage.haskell.org/packages/recent']
    allowed_domains = ['hackage.haskell.org']
    
    def parse(self, response):
        for package in response.xpath('//div[@id="content"]//tr'):
            name = package.xpath('./td[3]/a/text()').extract_first().strip()
            url = package.xpath('./td[3]/a/@href').extract_first()
            day = package.xpath('./td[1]/text()').extract_first()
            maintainer = package.xpath('./td[2]/text()').extract_first()
            release = re.search(r"-(\d+.+)$", name).group(1)
            description = ""
            yield {'language': 'Haskell',
                       'day': day.strip(),
                       'name': name.replace("-" + release, ""),
                       'maintainer': maintainer,
                       'release': release,
                       'description': description.strip(),
                       'url': response.urljoin(url)}

