import scrapy

# In this code, the GetLinksSpider class is a subclass of scrapy.Spider, which is the base class for defining spiders in Scrapy. 
# The spider is named "get_links", and the allowed domain is set to "nofluffjobs.com" to restrict crawling to this domain.
# The spider starts with a single URL, "https://nofluffjobs.com/pl/?lang=en&criteria=jobLanguage%3Den&page=1", defined in the start_urls list.
# The parse method is the callback function that is called for each URL in start_urls. It is responsible for extracting links from the web page.
#  The Link class defines the field for the scraped link using scrapy.Field().
# An XPath expression is defined to locate the link elements on the web page. 
# The expression selects the href attributes of anchor elements (<a>) with a class attribute that matches the regular expression "page-link". 
# The response.xpath() method is then used to apply the XPath expression on the response object and obtain a list of selected elements.
# Inside the loop, a new Link object is created to store the scraped link. 
# The link is obtained by concatenating the base URL ("https://nofluffjobs.com") with the value of the href attribute of the selected element. 
# The scraped link is assigned to the "link" field of the Link object.
# Finally, the yield statement is used to return the Link object, effectively generating the scraped item. 
# The scraped item is then processed by Scrapy's pipeline for further handling or storage.


################################################################################
# Code section 
################################################################################

class Link(scrapy.Item):
    # Define the field for the scraped link
    link = scrapy.Field()


class GetLinksSpider(scrapy.Spider):
    # Spider class for getting job advertisement links
    name = "get_links"
    allowed_domains = ["nofluffjobs.com"]
    start_urls = ["https://nofluffjobs.com/pl/?lang=en&criteria=jobLanguage%3Den&page=1"]

    def parse(self, response):
        # Parsing method for extracting links from the web page
        xpath = '//a[re:test(@class, "page-link")]//@href'
        # Define an XPath expression to locate the link elements
        # with class "page-link" and extract their "href" attributes
        selection = response.xpath(xpath)
        # Apply the XPath expression on the response object to obtain
        # a list of selected elements

        for s in selection:
            # Iterate over each selected element
            l = Link()
            # Create a new Link object to store the scraped link
            l['link'] = 'https://nofluffjobs.com' + s.get()
            # Assign the scraped link to the "link" field of the Link object
            yield l
            # Yield the Link object to return it as a scraped item

        pass