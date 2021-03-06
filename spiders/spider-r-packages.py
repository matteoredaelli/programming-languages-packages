import scrapy

class RSpider(scrapy.Spider):
    name = 'r-spider'
    start_urls = ['https://cran.r-project.org/web/packages/available_packages_by_date.html']
    allowed_domains = ['r-project.org']
    
    def parse(self, response):
        for package in response.xpath('//tr')[1:20]:
            name = package.xpath('./td/a/text()').extract_first().strip()
            url = package.xpath('./td/a/@href').extract_first()
            day = package.xpath('./td[1]/text()').extract_first()
            description = package.xpath('./td[3]/text()').extract_first()
            yield {'language': 'R',
                       'day': day.strip(),
                       'name': name,
                       'release': '',
                       'description': description.strip(),
                       'url': response.urljoin(url)}

