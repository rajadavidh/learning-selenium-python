# Video 043 - Locating Elements by class name and by name
# Import library
from selenium import webdriver
# Make sure to use latest chromedriver. Chrome and chromedriver version should be matched.
chrome_driver_path = "/Users/rajadavid/PycharmProjects/learning-selenium-python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# Open webpage
driver.get('http://docs.seleniumhq.org')

# Get element by class name
# y = driver.find_element_by_class_name('downloadBox')
# print y.text

# Get multiple items
elements = driver.find_elements_by_class_name('downloadBox')
print elements

# Run this script
# python 043_locating_elements_by_class_name.py
