import scrapy

class GithubTrendySpider(scrapy.Spider):
    name = 'github-trendy-repositories-spider'
    
    def __init__(self, lang, *args, **kwargs):
        self.start_urls = ['https://github.com/trending/%s?since=daily' % lang]
        self.allowed_domains = ['github.com']
        self.lang = lang
        super(GithubTrendySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        for package in response.xpath('//ol[@class="repo-list"]/li'):
            name1 = package.xpath('./div/h3/a/span/text()').extract_first().replace("\n","").strip()
            name2 = package.xpath('./div/h3/a/text()').extract()[1].replace("\n","").strip()
            url = package.xpath('./div/h3/a/@href').extract_first()
            day = ""
            description = package.xpath('./div[@class="py-1"]/p/text()').extract_first().replace("\n","").strip()
            yield {'language': self.lang,
                       'day': day.strip(),
                       'name': name1 + name2,
                       'release': '',
                       'description': description.strip(),
                       'url': response.urljoin(url)}

