# Video 045 - Explicit Wait vs Implicit Wait
# Prefer yang implicit karena yang explicit harus ditambahkan di tiap line
# Import library
from selenium import webdriver
# Make sure to use latest chromedriver. Chrome and chromedriver version should be matched.
chrome_driver_path = "/Users/rajadavid/PycharmProjects/learning-selenium-python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
# ini berguna untuk melakukan cek elemen ajax yang belum terbuka. 30 artinya dalam waktu 30 detik
# letakkan setelah membuat obyek
driver.implicitly_wait(2)


# Open webpage

# Save url in variable
url = ''

# Navigate to url
driver.get(url)
open_summary = driver.find_element_by_link_text('Performance')
open_summary.click()

print('berhasil')

# Run this script
# python 045_explicit_wait_and_implicit_wait.py
