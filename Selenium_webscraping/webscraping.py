################################################################################
# Import necessary modules
################################################################################

# The code imports the necessary libraries for web scraping and data manipulation.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


################################################################################
# Section with important parameters and driver
################################################################################

#The code snippet below imports necessary modules and defines three functions: initiate_driver, set_parameters, and take_all_adv_links.
#The initiate_driver function initializes the WebDriver by creating an instance of the Chrome WebDriver using the specified gecko_path and returns the driver object.
#The set_parameters function sets the parameters n_pages and n based on the value of max_100. If max_100 is True, n_pages is set to 5 and n is set to 100. Otherwise, if max_100 is False, n_pages is set to 100 and n is set to 2000. The function returns the values of n_pages and n.
#The take_all_adv_links function retrieves all advertisement links by iterating through each page. It initializes an empty list named links to store the advertisement links. For each page, a temporary list named link_temp_list is created. The URL for the current page is constructed based on the page number. The take_adv_links function is called to retrieve the advertisement links for the current page using the WebDriver object driver and the constructed URL. The link_temp_list is then extended to the links list. Finally, the function returns the advertisement links, limited to the specified maximum number n.

def initiate_driver(gecko_path):
    # Function to initiate the WebDriver
    driver = webdriver.Chrome(gecko_path)
    return driver

def set_parameters(max_100):
    # Function to set parameters based on the value of max_100
    if max_100:
        # If max_100 is True, set n_pages to 5 and n to 100
        n_pages = 5
        n = 100
    else:
        # If max_100 is False, set n_pages to 100 and n to 2000
        n_pages = 100
        n = 2000
    return n_pages, n

################################################################################
# This part prepares preliminary links - links for lists of links 
################################################################################



def take_all_adv_links(driver, n_pages, n):
    # Function to retrieve all advertisement links
    links = []
    for i in range(1, n_pages + 1):
        # Iterate through each page
        link_temp_list = []
        url = 'https://nofluffjobs.com/pl/?lang=en&criteria=jobLanguage%3Den&page=' + str(i)
        # Construct the URL for the current page
        link_temp_list = take_adv_links(driver, url)
        # Call a function to retrieve advertisement links for the current page
        links.extend(link_temp_list)
        # Extend the links list with the advertisement links from the current page

    return links[:n]
    # Return the advertisement links, limited to the specified maximum number


################################################################################
# This part prepares the links for the links
################################################################################



# The code below includes two functions.
# The find_property_one_attribute function attempts to find an element using the specified XPath in the provided WebDriver object. 
# If the element is found, its text content is returned. If the element is not found or an error occurs, an empty string is returned.
# The take_adv_links function takes a WebDriver object and a URL as input. It loads the URL in the WebDriver and finds the body element. It then performs a scrolling action on the body element to simulate scrolling down the page. The function waits for 2 seconds after each scroll action. It finds all <a> tags within a specific XPath and stores them in the new_tags list. The function compares the number of elements in new_tags with tags to determine if new tags are found. If new tags are found, tags is updated with the new tags; otherwise, the loop is broken. Finally, the function iterates through each tag, extracts the href attribute, and appends it to the link_temp_list. 
# The function returns the link_temp_list containing the extracted URLs.



def take_adv_links(driver, url):
    link_temp_list = []
    # Load the specified URL in the WebDriver
    driver.get(url)
    body = driver.find_element(By.TAG_NAME, 'body')
    tags = []

    while True:
        # Simulate scrolling down the page
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

        # Find all <a> tags within a specific XPath and store them in new_tags
        new_tags = driver.find_elements(By.XPATH, "/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-postings-search/div/common-main-loader/nfj-search-results/nfj-postings-list/div[3]/a")

        # Check if new_tags contains more elements than tags
        if len(new_tags) > len(tags):
            tags = new_tags
        else:
            # If no new tags are found, break the loop
            break

    # Iterate through each tag and extract the href attribute
    for tag in tags:
        url = tag.get_attribute('href')
        link_temp_list.append(url)

    return link_temp_list

################################################################################
# This part scraps the required atribiutes of the job_ads
################################################################################

# The code above defines the find_all_properties_all_attributes function and find_property_one_attribute. 
# This function takes a WebDriver object driver and a list of links links as input. It initializes an empty DataFrame named df to store the properties and their attributes.
# The xpaths dictionary contains the XPath expressions for each attribute of the property.
# The function iterates through each link in the links list. For each link, it loads the link in the WebDriver using driver.get(link). 
# It then uses a dictionary comprehension to iterate through each attribute and XPath pair in the xpaths dictionary. For each attribute, it calls the find_property_one_attribute function to find the corresponding element using the XPath in the current page and retrieves its text content. 
# The attribute-value pairs are stored in the property_attributes dictionary.
# Finally, the property_attributes dictionary is appended as a new row to the df DataFrame using the _append method. The function repeats this
# The find_property_one_attribute function attempts to find an element using the specified XPath in the provided WebDriver object. 

def find_property_one_attribute(driver, xpath):
    try:
        # Try to find an element using the specified XPath and retrieve its text content
        return driver.find_element(By.XPATH, xpath).text
    except:
        # Return an empty string if the element is not found or an error occurs
        return ''   

def find_all_properties_all_attributes(driver, links):
    df = pd.DataFrame({})  # Create an empty DataFrame to store the properties and their attributes
    
    #The xpaths dictionary contains the XPath expressions for each attribute of the property.
    xpaths = {
        'positon'      : '/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-posting-details/div/common-main-loader/main/article/div[1]/common-posting-content-wrapper/div[1]/common-posting-header/div/div/h1',
        'salary_range' : '/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-posting-details/div/common-main-loader/main/article/div[2]/common-apply-box/div/div[1]/common-posting-salaries-list/div/h4',
        'company'      : '//*[@id="postingCompanyUrl"]',
        'category1'    : '/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-posting-details/div/common-main-loader/main/article/div[1]/common-posting-content-wrapper/div[1]/section[1]/ul/li[1]/div/aside/div/a[1]',
        'category2'    : '/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-posting-details/div/common-main-loader/main/article/div[1]/common-posting-content-wrapper/div[1]/section[1]/ul/li[1]/div/aside/div/a[2]',
        'must_have'    : '/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-posting-details/div/common-main-loader/main/article/div[1]/common-posting-content-wrapper/div[1]/div[1]/section[1]/ul/li[1]',
        'nice_to_have' : '/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-posting-details/div/common-main-loader/main/article/div[1]/common-posting-content-wrapper/div[1]/div[1]/section[2]/ul/li[1]',
        'location'     : '//li[@id="backToCity"]',
        'seniority'    : '/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-posting-details/div/common-main-loader/main/article/div[1]/common-posting-content-wrapper/div[1]/section[1]/ul/li[2]/div[1]'
    }

    for link in links:
        driver.get(link)  # Load the link in the WebDriver
        
        # Initialize an empty dictionary to store the attributes of the current property
        property_attributes = {}
        
        # Iterate through each attribute and its corresponding XPath
        for attr, xpath in xpaths.items():
            # Call the find_property_one_attribute function to find the element and retrieve its text content
            attribute_value = find_property_one_attribute(driver, xpath)
            # Store the attribute-value pair in the property_attributes dictionary
            property_attributes[attr] = attribute_value
        
        # Append the property_attributes dictionary as a new row to the df DataFrame
        df = df._append(property_attributes, ignore_index=True)

    return df

################################################################################
# This part is for the execucation of the function  
################################################################################


#The code below defines the main function, which serves as the entry point of the script. It performs the following steps:
#It records the start time of the script execution using time.time().
#The max_100 and gecko_path variables are set to the desired values.
#The n_pages and n parameters are set using the set_parameters function based on the max_100 value.
#The WebDriver is initialized by calling the initiate_driver function, passing the gecko_path.
#The take_all_adv_links function is called to retrieve the advertisement links, passing the WebDriver, n_pages, and n as arguments. The links are stored in the links variable.
#The find_all_properties_all_attributes function is called to find the properties and their attributes, passing the WebDriver and the links list as arguments. The results are stored in the df DataFrame.
#The WebDriver is quit using the quit method.
#The DataFrame is saved as a CSV file named "job_ads_atribiutes_selenium.csv" using the to_csv method.
#The end time of the script execution is recorded using time.time().
#The total execution time is calculated by subtracting the start time from the end time.
#The script execution time is printed to the console.

def main():
    start_time = time.time()  # Get the start time of the script execution

    # Set parameters
    max_100 = True
    gecko_path = '/usr/local/bin/chromedriver'
    n_pages, n = set_parameters(max_100)

    # Initialize the WebDriver
    driver = initiate_driver(gecko_path)

    # Retrieve advertisement links
    links = take_all_adv_links(driver, n_pages, n)

    # Find properties and their attributes
    df = find_all_properties_all_attributes(driver, links)

    # Quit the WebDriver
    driver.quit()

    # Save the DataFrame as a CSV file
    df.to_csv('job_ads_atribiutes_selenium.csv', index=False, encoding='utf-8-sig')

    end_time = time.time()  # Get the end time of the script execution
    execution_time = end_time - start_time  # Calculate the execution time
    print(f"Script execution time: {execution_time} seconds")

main()
