# Video 039 - Running Test in Chrome
from selenium import webdriver

# Make sure to use latest chromedriver. Chrome and chromedriver version should be matched
chrome_driver_path = '/Users/rajadavid/PycharmProjects/learning-selenium-python/chromedriver'
driver = webdriver.Chrome(chrome_driver_path)
driver.get('http://google.com')

# Run this script
# python _039_test_in_chrome.
