import scrapy


# In this code, the JobAdsAtribiutesSpider class is a subclass of scrapy.Spider, which is the base class for defining spiders in Scrapy. 
# The spider is named "job_ads_atribiutes", and the allowed domain is set to "https://nofluffjobs.com/" to restrict crawling to this domain.
# The spider reads a file named "links.csv" to obtain the URLs of job advertisements. 
# These URLs are stored in the start_urls list. The file is opened and read line by line, excluding the first line (header) and limiting the number of URLs to 104 (from index 1 to 104).
# The parse method is the callback function that is called for each URL in start_urls. 
# It is responsible for extracting data from the web page. The JobItem class defines the fields for the scraped data using scrapy.Field().
# XPath expressions are used to locate the elements containing the desired attributes on the web page. Each attribute's XPath expression is assigned to a variable. 
# The response.xpath() method is then used to extract the data from the web page based on the XPath expressions, and the extracted data is assigned to the corresponding fields of the JobItem object (p).
# Finally, the yield statement is used to return the JobItem object, effectively generating the scraped data item. 
# The data item is then processed by Scrapy's pipeline for further handling or storage.


################################################################################
# Code section 
################################################################################

class JobItem(scrapy.Item):
    # Define the fields for the scraped data
    position = scrapy.Field()
    salary_range = scrapy.Field()
    company = scrapy.Field()
    category1 = scrapy.Field()
    category2 = scrapy.Field()
    location = scrapy.Field()
    seniority = scrapy.Field()
    remote = scrapy.Field()
    must_have = scrapy.Field()
    nice_to_have = scrapy.Field()


class JobAdsAtribiutesSpider(scrapy.Spider):
    # Spider class for scraping job advertisement attributes
    name = "job_ads_atribiutes"
    allowed_domains = ["https://nofluffjobs.com/"]

    try:
        with open("links.csv", "rt") as f:
            # Read the links from 'links.csv' file
            start_urls = [url.strip() for url in f.readlines()][1:105]
    except:
        start_urls = []

    def parse(self, response):
        # Parsing method for extracting data from each job advertisement page
        p = JobItem()

        # Define XPath expressions for each attribute
        position     = '//*[@id="posting-header"]/div/div/h1/text()'
        salary_range = '/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-posting-details/div/common-main-loader/main/article/div[2]/common-apply-box/div/div[1]/common-posting-salaries-list/div[1]/h4/text()'
        company      = '//*[@id="postingCompanyUrl"]/text()'
        category1    = '/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-posting-details/div/common-main-loader/main/article/div[1]/common-posting-content-wrapper/div[1]/section[1]/ul/li[1]/div/aside/div/a[1]/text()'
        category2    = '/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-posting-details/div/common-main-loader/main/article/div[1]/common-posting-content-wrapper/div[1]/section[1]/ul/li[1]/div/aside/div/a[2]/text()'
        location     = '//*[@id="backToCity"]/a/text()'
        seniority    = '//*[@id="posting-seniority"]/div[1]/span/text()'
        must_have    = '//*[@id="posting-requirements"]/section/h2[text()="Must have"]/following-sibling::*/li/span/text()'
        nice_to_have = '//*[@id="posting-requirements"]/section/h2[text()="Nice to have"]/following-sibling::*/li/span/text()'

        # Extract the data using XPath expressions and assign them to the corresponding fields
        p['position']     = response.xpath(position).getall()
        p['salary_range'] = response.xpath(salary_range).getall()
        p['company']      = response.xpath(company).getall()
        p['category1']    = response.xpath(category1).getall()
        p['category2']    = response.xpath(category2).getall()
        p['location']     = response.xpath(location).getall()
        p['seniority']    = response.xpath(seniority).getall()
        p['must_have']    = response.xpath(must_have).getall()
        p['nice_to_have'] = response.xpath(nice_to_have).getall()

        # Yield the scraped data item
        yield p