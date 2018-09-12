# Video 042 - Locating Elements by XPATH
# Import library
from selenium import webdriver
# Make sure to use latest chromedriver. Chrome and chromedriver version should be matched.
chrome_driver_path = "/Users/rajadavid/PycharmProjects/learning-selenium-python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# Open webpage
driver.get('http://www.python.org')

# Get element by xpath - ambil value dari xpath browser

# Ini fungsi tersendiri untuk ambil xpath
# driver.find_element_by_xpath('//*[@id="about"]/a')

# Ini ambil xpath dari fungsi lebih general: find_element()
text_value = driver.find_element('xpath', '//*[@id="about"]/a')
print text_value.text

# Run this script
# python 042_locating_elements_by_xpath.py
