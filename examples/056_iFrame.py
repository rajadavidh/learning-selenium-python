# Video 056 - iFrames
# Import library
from selenium import webdriver
# Make sure to use latest chromedriver. Chrome and chromedriver version should be matched.
chrome_driver_path = "/Users/rajadavid/PycharmProjects/learning-selenium-python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# Open webpage
url = 'cari web yang ada iFrame'
driver.get(url)

# Contoh dari videonya mau ambil value paragraf yang punya id 'p-out'
p = driver.find_element_by_id('p-out')
paragraph = p.text
print paragraph

first_frame = driver.find_element('id', 'login-frame')
driver.switch_to.frame(first_frame)

username = driver.find_element('id', 'username')
username.send_keys('testuser')

driver.switch_to.default_content()

# Run this script
# python 056_iFrame.py
