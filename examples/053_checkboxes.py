# Video 053 - Checkboxes
# Import library
from selenium import webdriver
# Make sure to use latest chromedriver. Chrome and chromedriver version should be matched.
chrome_driver_path = "/Users/rajadavid/PycharmProjects/learning-selenium-python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# Open webpage
url = 'cari web yang ada checkboxnya'
driver.get(url)


def assert_element_is_checkbox(element):
    my_element_type = element.get_attribute('type')

    if my_element_type != 'checkbox':
        raise AssertionError('The passed is not a checkbox.')

    return


def is_checkbox_selected(element):
    assert_element_is_checkbox(element)

    if element.is_selected():
        return True
    else:
        return False


def assert_checkbox_is_selected(element):
    assert_element_is_checkbox(element)

    if not is_checkbox_selected(element):
        raise AssertionError('The element is not selected.')

    return


def assert_checkbox_is_enabled(element):
    assert_element_is_checkbox(element)

    if not element.is_enabled():
        raise AssertionError('The checkbox is not enabled.')


# Demo
# Cari dulu alamat website yang bisa dijadikan demo
my_check_box = driver.find_element_by_class_name('nama_element')

print is_checkbox_selected(my_check_box)
assert_checkbox_is_enabled(my_check_box)

# Run this script
# python 053_checkboxes.py
