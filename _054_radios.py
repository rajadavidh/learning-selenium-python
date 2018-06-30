# Video 054 - Radios
# Import library
from selenium import webdriver
# Make sure to use latest chromedriver. Chrome and chromedriver version should be matched.
chrome_driver_path = "/Users/rajadavid/PycharmProjects/learning-selenium-python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)


# Open webpage
# Mirip dengan checkbox
def assert_element_is_radio(element):
    my_element_type = element.get_attribute('type')

    if my_element_type != 'radio':
        raise AssertionError('The passed element is not a radio input.')
    else:
        # Dibagian ini bisa untuk print log
        print('The element is a radio input')

    return


def assert_radio_is_selected(element):
    assert_element_is_radio(element)

    if element.is_selected():
        print('The element is selected.')
    else:
        raise AssertionError('The element is not selected')

    return


def select_radio_by_value(elements, value):
    found = False

    for element in elements:
        assert_element_is_radio(element)

        current_value = element.get_attribute('value')

        if current_value == value:
            element.click()
            found = True
            break

    if not found:
        raise Exception('None of the radios have the requested value')

    return


# Demo
my_radio = driver.find_element_by_name('nama_element')
print my_radio
print type(my_radio)

select_radio_by_value(my_radio, 'value_element(cth: 30-40)')

# Run this script
# python _054_radios.py
