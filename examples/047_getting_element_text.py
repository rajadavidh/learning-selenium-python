# Video 047 - Getting an elements text
# Import library
from selenium import webdriver
# Make sure to use latest chromedriver. Chrome and chromedriver version should be matched.
chrome_driver_path = "/Users/rajadavid/PycharmProjects/learning-selenium-python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# Open webpage
url = 'http://www.w3schools.com/'
driver.get(url)

# Left_nav gak jalan karena harus di klik dulu biar muncul
# my_left_nav = driver.find_element('id','sidemenu')
# my_left_nav = driver.find_element_by_id('sidemenu')
# Sidemenu berubah jadi mySidenav
my_left_nav = driver.find_element_by_id('mySidenav')
left_nav_text = my_left_nav.text

# Top_nav jalan karena sudah muncul saat webpage ter load
# my_top_nav = driver.find_element_by_class_name('topnavlinks')
# my_top_nav = driver.find_element('class name','topnavlinks')
# top_nav_text = my_top_nav.text

print '=========================================='
print left_nav_text
print '-----------------'
# print top_nav_text
print '=========================================='


def assert_element_not_empty(element):
    element_text = element.text
    if element_text == '':
        raise AssertionError('The element does not contain any text.')
    else:
        print 'The element does contain some text. The text is %s' % element_text


def assert_element_contains_text(element, text):
    element_text = element.text

    if text in element_text:
        print ('The element contains the text: %s' % element_text)
    else:
        raise AssertionError('The element does not contain the text: %s' % element_text)
    return


print '=========================================='
# assert_element_not_empty(my_left_nav)
print '-----------------'
my_top_nav = driver.find_element('class name', 'topnavlinks')
assert_element_not_empty(my_top_nav)
print '=========================================='


# Run this script
# python 047_getting_element_text.py
