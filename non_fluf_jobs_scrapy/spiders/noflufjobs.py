import scrapy


class Link(scrapy.Item):
    link = scrapy.Field()

class NoflufjobsSpider(scrapy.Spider):
    name = "noflufjobs"
    allowed_domains = ["nofluffjobs.com"]
    start_urls = ["https://nofluffjobs.com/pl/?lang=en&criteria=jobLanguage%3Den&page=1"]



    def parse(self, response):
        xpath = '//a[re:test(@title, "List of painters.*")]//@href'
        selection = response.xpath(xpath)
        for s in selection:
            l = Link()
            l['link'] = 'https://en.wikipedia.org' + s.get()
            yield l

        pass
