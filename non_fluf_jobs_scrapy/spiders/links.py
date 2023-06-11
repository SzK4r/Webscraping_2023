import scrapy


# In this code, the LinksSpider class is a subclass of scrapy.Spider, which is the base class for defining spiders in Scrapy. 
# The spider is named "links", and the allowed domain is set to "https://nofluffjobs.com" to restrict crawling to this domain.
# The spider starts with multiple URLs loaded from a CSV file, "get_links.csv". 
# The file is opened in read mode, and the URLs are read from the file's lines. 
# The list comprehension [url.strip() for url in f.readlines()][1:7] is used to remove leading/trailing whitespace from each line and retrieve URLs from the second to the seventh line (index 1 to 6). 
# If any error occurs during file handling or URL extraction, an empty list is assigned to start_urls.
# The parse method is the callback function that is called for each URL in start_urls. 
# It is responsible for extracting links from the web page. 
# The Link class defines the field for the scraped link using scrapy.Field().
# The print(response) statement is used to print the response object for debugging purposes. 
# It can help in understanding the structure and content of the web page being parsed.
# An XPath expression is defined to locate the link elements on the web page. 
# The expression selects the href attributes of elements with IDs that match the regular expression "nfjPostingListItem*" and the attributes start with "/pl/job". 
# The response.xpath() method is then used to apply the XPath expression on the response object and obtain a list of selected elements.
# Inside the loop, a new Link object is created to store the scraped link. 
# The link is obtained by concatenating the base URL ("https://nofluffjobs.com"), the value of the href attribute of the selected element, and "?lang=en" to set the language parameter to English. 
# The scraped link is assigned to the "link" field of the Link object.
# The print(l) statement is used to print the Link object for debugging purposes. 
# It can help in verifying that the link is correctly scraped.
# Finally, the yield statement is used to return the Link object, effectively generating the scraped item. 
# The scraped item is then processed by Scrapy's pipeline for further handling or storage.
 
################################################################################
# Code section 
################################################################################

class Link(scrapy.Item):
    # Define the field for the scraped link
    link = scrapy.Field()


class LinksSpider(scrapy.Spider):
    # Spider class for scraping job advertisement links
    name = "links"
    allowed_domains = ["https://nofluffjobs.com"]

    try:
        with open("get_links.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:7]
    except:
        start_urls = []

    def parse(self, response):
        # Parsing method for extracting links from the web page
        print(response)
        # Print the response object for debugging purposes
        xpath = '//*[re:test(@id, "nfjPostingListItem*") and starts-with(@href, "/pl/job")]/@href'
        # Define an XPath expression to locate the link elements
        # with IDs starting with "nfjPostingListItem" and href attributes
        # starting with "/pl/job"
        selection = response.xpath(xpath)
        # Apply the XPath expression on the response object to obtain
        # a list of selected elements

        for s in selection:
            # Iterate over each selected element
            l = Link()
            # Create a new Link object to store the scraped link
            l['link'] = 'https://nofluffjobs.com' + s.get() + "?lang=en"
            # Assign the scraped link to the "link" field of the Link object
            print(l)
            # Print the Link object for debugging purposes
            yield l
            # Yield the Link object to return it as a scraped item

        pass
