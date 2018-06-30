# Video 046 - Verify element exists and is visible
# Import library
from selenium import webdriver
# Make sure to use latest chromedriver. Chrome and chromedriver version should be matched.
chrome_driver_path = "/Users/rajadavid/PycharmProjects/learning-selenium-python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# Open webpage
url = 'http://www.w3schools.com/'
driver.get(url)


def element_exists(locator_attribute, locator_text):
    """
    Finds an element and returns true or false if element is found or not.
    :param locator_attribute:
    :param locator_text:
    :return:
    """

    possible_locators = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name",
                         "css selector"]

    if locator_attribute not in possible_locators:
        raise BaseException(
            'The locator attribute provided is not in the approved attributes. '
            'Or the spelling and format does not match. The approved attributes are : %s ' % possible_locators)

    try:
        driver.find_element(locator_attribute, locator_text)
        return True
    except:
        return False


def assert_element_exists(locator_attribute, locator_text):
    """
    Fungsi ini didesain untuk mendapatkan fail
    Fungsi ini akan fail kalo elemennya gak ditemukan
    :param locator_attribute:
    :param locator_text:
    :return:
    """

    if not element_exists(locator_attribute, locator_text):
        # Ini menunjukkan kalo fungsi ini memang didesain untuk fail
        raise AssertionError("The requested element with '%s' of '%s' does not exist"
                             % (locator_attribute, locator_text))

    return


def element_visible(element):
    """
    Untuk memeriksa apakah elemennya muncul di browser
    Fungsi ini dibuat supaya bisa lebih mudah mengontrol output yang diinginkan yaitu
    Apakah nge print hasil atau cuma lempar value
    :param element:
    :return:
    """

    if element.is_displayed():
        return True
    else:
        return False


def assert_element_visible(element):
    if not element_visible(element):
        # raise AssertionError('The element with locator type "%s" and locator term "%s" is not displayed'
        #                      % (locator_attribute, locator_text))
        raise AssertionError('The element requested is not displayed')


def find_and_assert_element_visible(locator_type, search_term):
    """
    Author lebih suka fungsi ini dibandingkan assert_element_visible() diatas
    :param locator_type:
    :param search_term:
    :return:
    """

    element = driver.find_element(locator_type, search_term)

    if not element.is_displayed():
        raise AssertionError('The element with locator type "%s" and locator term "%s" is not displayed'
                             % (locator_type, search_term))
    else:
        print 'The element is visible'


# Contoh gak jalan
# assert_element_exists('name', 'bqresponse')

# Contoh jalan
assert_element_exists('id', 'navbtn_tutorials')
find_and_assert_element_visible('id', 'navbtn_tutorials')

# Run this script
# python _046_verify_element_exists.py
