# Video 059 - Dealing with URLs
# Import library
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Make sure to use latest chromedriver. Chrome and chromedriver version should be matched.
chrome_driver_path = "/Users/rajadavid/PycharmProjects/learning-selenium-python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# Open webpage
url = 'http://www.amazon.com'
driver.get(url)


def assert_url_contains_text(expected_text):
    current_url = driver.current_url

    if expected_text not in current_url:
        raise AssertionError("The text '%s' is not in the url. The current url is: '%s'" % (expected_text, current_url))
    else:
        print ('The text is present in the URL')


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


# Demo
search_field = driver.find_element('id', 'twotabsearchtextbox')
search_field.send_keys('B000LB67KU')
search_field.send_keys(Keys.RETURN)

time.sleep(2)
assert_url_contains_text('B000LB67KU')

my_element = driver.find_element_by_xpath('//*[@id="nav-xshop"]/a[5]')
link_url = get_link_url(my_element)
print link_url


# Run this script
# python _059_dealing_urls.py
