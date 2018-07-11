# Video 057 - Multiple windows
# Import library
import time
from selenium import webdriver
# Make sure to use latest chromedriver. Chrome and chromedriver version should be matched.
chrome_driver_path = "/Users/rajadavid/PycharmProjects/learning-selenium-python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# Open webpage
url = 'http://corporate.walmart.com'
driver.get(url)


def get_num_of_windows():
    """
    Test pindah tab di browser
    :return:
    """
    windows = driver.window_handles

    num_of_windows = len(windows)

    return num_of_windows


def switch_to_window_number(index):
    try:
        index = int(index)
    except ValueError:
        raise Exception('The index number requested is not a number. Please pass in an integer')

    total_win = get_num_of_windows()

    if index > total_win:
        raise Exception('The requested index is more than available windows')

    all_windows = driver.window_handles
    requested_window = all_windows[index]
    driver.switch_to.window(requested_window)

    return


def assert_current_title(title_text):
    """

    :param title_text:
    :return:
    """
    current_title = driver.title

    if current_title != title_text:
        raise AssertionError('The current title is not as expected. Current title is: %s. Expected title is: %s'
                             % (current_title, title_text))
    else:
        print 'the title is as expected. Current title is: %s. Expected title is: %s' % (current_title, title_text)


def my_walmart_test():
    expected_second_window_title = 'Welcome to Walmart Careers'

    main_page_title = driver.title
    main_win_handle = driver.current_window_handle
    print 'the main window handle is: %s' % main_win_handle

    career_link = driver.find_element_by_link_text('Walmart Careers')
    career_link.click()

    # Kadang muncul error, makanya ditambahka time.sleep di baris ini
    time.sleep(2)
    switch_to_window_number(1)
    new_win_title = driver.title

    if new_win_title != expected_second_window_title:
        raise AssertionError('the focus did not switch to desired window, or the new tab is not the correct page.')
    else:
        print 'Success'


my_walmart_test()

# Run this script
# python _057_multiple_window.py
