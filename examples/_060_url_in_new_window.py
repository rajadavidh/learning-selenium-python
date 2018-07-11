# Video 060 - Open link URL in new windows
# Import library
from selenium import webdriver
# mau ambil fingsi get_link_url, tapi gak jadi
import _059_dealing_urls as url
# Make sure to use latest chromedriver. Chrome and chromedriver version should be matched.
chrome_driver_path = "/Users/rajadavid/PycharmProjects/learning-selenium-python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# Open webpage
url_link = 'http://www.amazon.com'
driver.get(url_link)


# Copy fungsi get_link_url dari _059_dealing_urls.
# Tadinya mau pake import aja, tapi gak jadi
def get_link_url(element):
    tag_type = element.tag_name
    if tag_type != 'a':
        print ('The element is not a link. Checking if it contains other element or links within it.')
        child_elements = element.find_elements_by_tag_name('a')

        num_of_links = len(child_elements)

        if num_of_links == 0:
            raise Exception('The element is not a link')
        elif num_of_links > 1:
            raise Exception('There are multiple element. Please provide specific element')
        else:
            link_url = child_elements[0].get_attribute('href')
    else:
        link_url = element.get_attribute('href')

    return link_url


# Revisi jadi order karena strukturnya sudah beda
# wishlist = driver.find_element('id', 'nav-link-wishlist')
wishlist = driver.find_element('id', 'nav-orders')

# Perintah dibawah ini kalo pake import _059_dealing_urls
# Kalo pake ini main Open webpage yang ada di _059_dealing_urls juga ikut dieksekusi
my_url = url.get_link_url(wishlist)

# Panggil fungsi yang udah dicopy dari _059_dealing_urls
# my_url = get_link_url(wishlist)
print '*********************'
print my_url
print '*********************'

# New windownya disini
browser = webdriver.Chrome(chrome_driver_path)
browser.get(my_url)

print browser.title

name_field = browser.find_element_by_name('email')
name_field.send_keys('test multiple')

# Run this script
# python _060_url_in_new_window.py
