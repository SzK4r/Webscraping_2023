from selenium import webdriver
import time

path = '/usr/local/bin/chromedriver'
url = 'http://www.google.com'


driver = webdriver.Chrome(executable_path = path)
time.sleep(3)
driver.get(url)
time.sleep(5)
driver.close()