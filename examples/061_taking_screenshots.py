# Video 061 - Taking Screenshots
# Import library
from selenium import webdriver
# Make sure to use latest chromedriver. Chrome and chromedriver version should be matched.
chrome_driver_path = "/Users/rajadavid/PycharmProjects/learning-selenium-python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# Open webpage
url = 'http://www.seleniumhq.org'
driver.get(url)
driver.get_screenshot_as_file('screenshot_demo.jpg')
driver.quit()

# Run this script
# python 061_taking_screenshots.py
