# Video 044 - Locating Elements by link text and partial link text
# Import library
# import pdb
from selenium import webdriver
# Make sure to use latest chromedriver. Chrome and chromedriver version should be matched.
chrome_driver_path = "/Users/rajadavid/PycharmProjects/learning-selenium-python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# Open webpage
driver.get('http://www.seleniumhq.org')

# Get element by class name
# --------
# pdb.set_trace() #Python Debugger untuk pause eksekusi
# wd_link = driver.find_element_by_link_text('Selenium WebDriver')
# wd_link.click()
# --------

# If multiple match, it will pick the first always
# y = driver.find_element_by_partial_link_text('many browsers')
# y.click()

element = driver.find_element_by_link_text('many browsers')
element.click()
# print element.text

# Run this script
# python 044_locating_elements_by_link_text.py
