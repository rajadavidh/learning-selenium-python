# Video 058 - Window size and Location
# Import library
from selenium import webdriver
import time
# Make sure to use latest chromedriver. Chrome and chromedriver version should be matched.
chrome_driver_path = "/Users/rajadavid/PycharmProjects/learning-selenium-python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# Open webpage
url = 'http://www.google.com'
driver.get(url)

time.sleep(3)

driver.set_window_size(width=500, height=800)

time.sleep(3)
driver.set_window_size(width=800, height=500)

time.sleep(3)
driver.set_window_size(width=400, height=400)

time.sleep(3)
print driver.get_window_position()

time.sleep(3)
driver.maximize_window()

# position = driver.get_window_position()
# print position

# Run this script
# python 058_window_size_and_location.py
