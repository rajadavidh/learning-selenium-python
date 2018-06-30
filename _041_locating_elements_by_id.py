# Video 041 - Locating Elements by ID
from selenium import webdriver
# Make sure to use latest chromedriver. Chrome and chromedriver version should be matched.
chrome_driver_path = "/Users/rajadavid/PycharmProjects/learning-selenium-python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# Open webpage
driver.get('http://docs.seleniumhq.org')

# Get element by ID - ambil value dari ID html
# ini fungsi tersendiri untuk ambil ID
# driver.find_element_by_id('editPage')

# Ini ambil ID dari fungsi lebih general: find_element()
text_value = driver.find_element('id', 'editPage')
print text_value.text

# Run this script
# python _041_locating_elements_by_id.py
