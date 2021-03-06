from scrapy.spiders import XMLFeedSpider
import  dateutil.parser

class PythonSpider(XMLFeedSpider):
    name = 'python-spider'
    allowed_domains = ['packagist.org']
    start_urls = ['https://packagist.org/feeds/releases.rss']
    iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, response, node):
        self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.extract()))
        name_rel =  node.xpath('guid/text()').extract_first().split()
        day = node.xpath('pubDate/text()').extract_first()
        item = {}
        item['day'] = dateutil.parser.parse(day).strftime("%Y-%m-%d")
        item['name'] = name_rel[0]
        item['release'] = name_rel[1]
        item['description'] = node.xpath('description/text()').extract_first()
        item['url'] = node.xpath('link/text()').extract_first()
        item['language'] = 'Php'
        yield item
