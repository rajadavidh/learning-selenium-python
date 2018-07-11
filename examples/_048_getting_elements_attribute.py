# Video 048 - Getting elements attribute
# Import library
from selenium import webdriver
# Make sure to use latest chromedriver. Chrome and chromedriver version should be matched.
chrome_driver_path = "/Users/rajadavid/PycharmProjects/learning-selenium-python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# Open webpage#1
"""
# Dapatin jumlah kolom dan baris dari textarea yang udah terisi
url = 'http://www.w3schools.com/tags/tryit.asp?filename=tryhtml_textarea'
driver.get(url)

my_frame = driver.find_element('id', 'iframeResult')
driver.switch_to.frame(my_frame)
box = driver. find_element_by_tag_name('textarea')

box_text = box.get_attribute('value')
print box_text

num_of_cols = box.get_attribute('cols')
num_of_rows = box.get_attribute('rows')
print num_of_cols
print num_of_rows
"""

# Open webpage#2 - lanjut dari min 01:47
url = 'http://www.seleniumhq.org'
driver.get(url)

# Dapatin value dari button GO di searchbox kanan atas halaman web
sub_btn = driver.find_element_by_id('submit')
sub_btn_attribute = sub_btn.get_attribute('value')
print sub_btn_attribute

# Dapatin title value dari main menu: Support
support_tab = driver.find_element_by_xpath('//*[@id="menu_support"]/a')
support_tab_title = support_tab.get_attribute('title')
print '================'
print support_tab_title
print '================'

sel_image = driver.find_element_by_xpath('//*[@id="sidebar"]/img')
sel_image_alt = sel_image.get_attribute('alt')
print sel_image_alt

sel_image_src = sel_image.get_attribute('src')
print sel_image_src

# Run this script
# python _048_getting_elements_attribute.py
