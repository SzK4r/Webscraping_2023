# Webscraping_NoFlufJobs.com
This project is a web scraping application built with Scrapy, Selenium, and BeautifulSoup (BS4), powerful and flexible web scraping frameworks in Python. The purpose of this project is to extract job advertisement data from the website "nofluffjobs.com" and gather information such as job positions, salary ranges, company details, categories, locations, seniority levels, and required skills.

# Scrapy is in the second branch (master) 

## Features

- Scrape job advertisement data from "nofluffjobs.com"
- Utilize Scrapy for efficient and high-performance web scraping
- Employ Selenium for interacting with JavaScript-heavy pages
- Leverage BeautifulSoup (BS4) for HTML parsing and data extraction
- Extract job positions, salary ranges, company details, categories, locations, seniority levels, and required skills
- Store the scraped data in structured formats (e.g., CSV files)

## Prerequisites

To run this application, you need to have the following installed:

- Python (version 3.6 or above)
- Scrapy (version 2.5.1 or above)
- Selenium (version 4.0.0 or above)
- BeautifulSoup (version 4.9.3 or above)
- Chrome WebDriver (for Selenium)

## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies
3. Modify the spider configuration and settings as needed:
- `links.csv`: Provide the list of URLs from which to scrape job advertisement links.
- `get_links.csv`: Modify the URLs to specify the starting point for scraping job advertisement links.
4. Run the scraper using the following command:
Replace `<spider_name>` with the name of the spider you want to run (`job_ads_attributes` or `links`).
5. The scraped data will be stored in the specified output format (e.g., CSV files).


## More information 
Below you can find the links to the report and presentation recordings.

Link to the presentation recordings: 
https://drive.google.com/drive/folders/1dqX-XoL1A3bfNT9vYoo8Jk28bjpcGZGR?usp=drive_link
Link to the report: 
https://docs.google.com/document/d/1cG36OtaB34dqOuqHwJ5r50YlUAKUh0r4-FlNeOCSKwo/edit?usp=sharing

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
