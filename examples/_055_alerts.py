# Video 055 - Alerts
# Import library
from selenium import webdriver
# Make sure to use latest chromedriver. Chrome and chromedriver version should be matched.
chrome_driver_path = "/Users/rajadavid/PycharmProjects/learning-selenium-python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)


# Open webpage
def is_alert_present():
    try:
        # TODO still not working
        driver.switch_to.alert
        return True
    except:
        return False


def assert_alert_present():
    if not is_alert_present():
        raise AssertionError('There is no alert present')

# Run this script
# python _055_alerts.py
