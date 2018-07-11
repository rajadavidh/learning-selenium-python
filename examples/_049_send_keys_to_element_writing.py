# Video 049 - Sending keys to elements writing in fields
# Import library
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Make sure to use latest chromedriver. Chrome and chromedriver version should be matched.
chrome_driver_path = "/Users/rajadavid/PycharmProjects/learning-selenium-python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# Open webpage
url = 'http://www.google.com'
driver.get(url)

# Find the search element
search_field = driver.find_element('id', 'lst-ib')

# Hit special key on browser
# Dalam kasus ini akan diketik 'Selenium Webdriver' di searchbox google
search_field.send_keys('Selenium Webdriver')

# Perintah untuk tunjukkan petunjuk penggunaan 'Key'
# Ketik di console python: dir(Keys)

# Perintah untuk pindahkan kursor turun seperti pilih arrow_down
search_field.send_keys(Keys.DOWN)

# Pilih key ENTER kayak dari keyboard
search_field.send_keys(Keys.RETURN)

# Hapus text
search_field.clear()

# Isi lagi text fieldnya
search_field.send_keys('Test')

# Run this script
# python _049_send_keys_to_element_writing.py
