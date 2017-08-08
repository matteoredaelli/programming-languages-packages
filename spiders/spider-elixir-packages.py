import scrapy

class ElixirSpider(scrapy.Spider):
    name = 'elixir-spider'
    start_urls = ['https://hex.pm/packages?sort=updated_at']
    allowed_domains = ['hex.pm']
    
    def parse(self, response):
        for package in response.xpath('//div[@class="package-list"]/ul/li'):
            name = package.xpath('./a/text()').extract_first().strip()
            url = package.xpath('./a/@href').extract_first()
            day = ""
            version = package.xpath('./span[@class="version"]/text()').extract_first()
            description = package.xpath('./p/text()').extract_first()
            yield {'language': 'Elixir',
                       'day': day.strip(),
                       'name': name,
                       'version': version,
                       'description': description.strip(),
                       'url': response.urljoin(url)}

