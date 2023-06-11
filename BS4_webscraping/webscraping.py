################################################################################
# Import necessary modules part
################################################################################

# The code imports the necessary libraries for web scraping and data manipulation. It disables SSL verification using ssl._create_default_https_context = ssl._create_unverified_context, which may be helpful when dealing with websites that have SSL certificate issues.
from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd
import ssl
import time
ssl._create_default_https_context = ssl._create_unverified_context




################################################################################
# This part prepares links of the websites
################################################################################

# The url variable is assigned a specific URL that will be scraped. The urlopen function from the request module is used to open the URL and retrieve the HTML content. The BeautifulSoup constructor is used to create a BeautifulSoup object named bs, which represents the parsed HTML.
# The code then uses the find_all method on the bs object to search for all <a> tags with a class attribute that matches the regular expression 'page-link'. The extracted href attributes from these tags are appended to the base URL 'https://nofluffjobs.com', resulting in a list of complete URLs assigned to the variable links.
# Overall, this code snippet retrieves HTML content from a specified URL, extracts specific links from it, and constructs a list of complete URLs based on those extracted links.


start_time = time.time()

# Specify the URL to scrape
url = 'https://nofluffjobs.com/pl/?lang=en&criteria=jobLanguage%3Den&page=1'

# Open URL and retrieve HTML content
html = request.urlopen(url)
bs = BS(html, 'html.parser')

# Find all <a> tags with class matching the regular expression pattern 'page-link'
tags = bs.find_all('a', {'class':re.compile('page-link')})

# Extract the 'href' attribute value from each <a> tag and append it to the links list
links = ['https://nofluffjobs.com' + tag['href'] for tag in tags]




################################################################################
# This part prepares real job ads links
################################################################################

# A new empty list named job_ads_links is created to store the final job advertisement links. A loop is started to iterate through each link in the links list. Inside the loop, the urlopen function is used to open each link and retrieve the HTML content. 
# The HTML content is passed to the BeautifulSoup constructor along with the parser to create a new BeautifulSoup object named bs for each link. Using the find_all method on the bs object, the code searches for all <a> tags with a class attribute that matches the regular expression 'posting-list-item.*'. 
# A temporary list named link_temp_list is created to store the extracted job advertisement links. Inside a nested loop, the code iterates through each tag in the tags list.
# Within the nested loop, the code attempts to append a modified version of the extracted link to the link_temp_list by concatenating 'https://nofluffjobs.com', the href attribute from the tag, and '?lang=en'. 
# If an exception occurs during the appending process (likely due to a missing or invalid href attribute), the except block does nothing. After the nested loop, the link_temp_list is extended to the job_ads_links list, adding all the extracted job advertisement links to the final list.
# By executing this code, the script extracts the job advertisement links from the previously extracted links. Each link is modified and appended to the job_ads_links list.

#A new empty list named job_ads_links is created to store the final job advertisement links.
job_ads_links = []

#A loop is started to iterate through each link in the links list.
job_ads_links = []

for link in links:
    # Iterate through the links list

    # Open URL and retrieve HTML content
    html = request.urlopen(link)
    bs = BS(html, 'html.parser')

    # Find all <a> tags with class matching the regular expression pattern 'posting-list-item.*'
    tags = bs.find_all('a', {'class':re.compile('posting-list-item.*')})

    link_temp_list = []
    for tag in tags:
        try:
            # Extract the 'href' attribute value from the <a> tag and append it to the link_temp_list
            link_temp_list.append('https://nofluffjobs.com' + tag['href']+'?lang=en')
        except:
            # If extraction fails, do nothing (placeholder 0 is used)
            0 

    # Extend the job_ads_links list with the link_temp_list
    job_ads_links.extend(link_temp_list)



################################################################################
# This part scraps the required atribiutes of the job_ads
################################################################################

d = pd.DataFrame({'position': [], 'salary_range': [], 'company': [], 'category1': [], 'category2': [], 'location': [], 'remote': [], 'must have': [], 'nice to have': [], 'seniority': []})


for url in job_ads_links[:5]:
    # Iterate through the first 5 URLs in the job_ads_links list

    # Open URL and retrieve HTML content
    html = request.urlopen(url)
    bs = BS(html.read(), 'html.parser')

    try:
        # Extract job position
        position = bs.find('h1', {'class': 'font-weight-bold'}).text.strip()
    except:
        # Set position to an empty string if extraction fails
        position = ''

    try:
        # Extract salary
        salary = bs.find('h4', {'class': 'tw-mb-0'}).text.strip()
    except:
        # Set salary to an empty string if extraction fails
        salary = ''

    try:
        # Extract company name
        company = bs.find('a', {'id': 'postingCompanyUrl'}).text.strip()
    except:
        # Set company to an empty string if extraction fails
        company = ''

    try:
        # Extract categories
        categories = bs.find_all('a', {'class': 'font-weight-semi-bold'})
        # Extract first category if available, otherwise set it to an empty string
        category1 = categories[0].text.strip() if len(categories) >= 1 else ''
        # Extract second category if available, otherwise set it to an empty string or 'None'
        category2 = categories[1].text.strip() if len(categories) >= 2 else ''
    except:
        # Set categories to empty strings if extraction fails
        category1 = ''
        category2 = 'None'

    try:
        # Extract location
        location = bs.find('li', {'id': 'backToCity'}).text.strip()
    except:
        # Set location to an empty string if extraction fails
        location = ''

    try:
        # Extract 'Must have' skills
        must_have_element = bs.find('h2', text='Must have')
        ul_element = must_have_element.find_next('ul')
        # Extract text content of each <li> element within the <ul> element
        must_have_list = [li.text.strip() for li in ul_element.find_all('li')]
        # Join the extracted skills into a comma-separated string
        must_have = ', '.join(must_have_list)
    except:
        # Set must_have to an empty string if extraction fails
        must_have = ''

    try:
        # Extract 'Nice to have' skills
        nice_to_have_element = bs.find('h2', text='Nice to have')
        ul_element = nice_to_have_element.find_next('ul')
        # Extract text content of each <li> element within the <ul> element
        nice_to_have_list = [li.text.strip() for li in ul_element.find_all('li')]
        # Join the extracted skills into a comma-separated string
        nice_to_have = ', '.join(nice_to_have_list)
    except:
        # Set nice_to_have to an empty string if extraction fails
        nice_to_have = ''

    if not nice_to_have:
        # Set nice_to_have to 'None' if it is empty
        nice_to_have = 'None'

    # Extract seniority information
    seniority_element = bs.find('span', {'class': 'mr-10 font-weight-medium'})
    if seniority_element:
        # Extract seniority from the first type of element
        seniority = seniority_element.text.strip()
    else:
        seniority_element = bs.find('span', {'class': 'font-weight-medium'})
        if seniority_element:
            # Extract seniority from the second type of element
            seniority = seniority_element.text.strip()
        else:
            # Set seniority to an empty string if extraction fails
            seniority = ''



# Save DataFrame to CSV
d.to_csv('job__ads_data.csv', index=False)

# Calculate the execution time
end_time = time.time()
execution_time = end_time - start_time 

# Print the execution time
print(f"BF4 execution time: {execution_time} seconds")
