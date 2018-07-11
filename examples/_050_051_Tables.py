# Video 050 and 051 - Tables
# Import library
from selenium import webdriver
# Make sure to use latest chromedriver. Chrome and chromedriver version should be matched.
chrome_driver_path = "/Users/rajadavid/PycharmProjects/learning-selenium-python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# Open webpage
# 050: Tables part 01
# Tambah implicit wait
driver.implicitly_wait(30)
url = 'http://www.w3schools.com/html/html_tables.asp'
driver.get(url)


def get_number_of_table_rows(my_table):
    # Dapatkan list dari tag <tr>
    all_rows = my_table.find_elements_by_tag_name('tr')
    number_of_rows = len(all_rows)

    return number_of_rows


def assert_number_of_rows_in_table(my_table, expected_num_of_rows):
    actual_num_rows = get_number_of_table_rows(my_table)
    if expected_num_of_rows != actual_num_rows:
        raise AssertionError('The number of row did not match. The actual number is: %s and the expected number is %s'
                             % (str(actual_num_rows), str(expected_num_of_rows)))

    return


def assert_row_contains_text(my_table, text_to_check, row_number):
    """
    Fungsi ini akan memastikan kalo sebuah baris mengandung text yang diinput
    :param my_table:
    :param text_to_check:
    :param row_number:
    :return:
    """
    all_rows = my_table.find_elements_by_tag_name('tr')
    my_row = all_rows[row_number]
    row_text = my_row.text

    if text_to_check not in row_text:
        raise AssertionError('The text %s is not in row %s' % (text_to_check, row_number))
    else:
        print 'The text %s is found in row %s' % (text_to_check, row_number)

    return


# 051: Tables part 02
def assert_col_in_row_contains_text(my_table, text_to_check, row_number=0, col_number=0):
    all_rows = my_table.find_elements_by_tag_name('tr')

    if row_number > len(all_rows):
        raise BaseException('The row number requested is more than the available rows')

    my_row = all_rows[row_number]
    all_cols = my_row.find_elements_by_tag_name('td')
    my_col = all_cols[col_number]
    col_text = my_col.text

    # Minutes -04:07
    if text_to_check not in col_text:
        raise AssertionError('The text %s is not in row %s column %s'
                             % (text_to_check, str(row_number), str(col_number)))
    else:
        print 'The text %s is in row %s column %s' % (text_to_check, str(row_number), str(col_number))

    return


# Demo
# table = driver.find_element_by_class_name('reference')
# Revisi berdasarkan kondisi terkini di web w3choolnya
table = driver.find_element_by_id('customers')

rows = get_number_of_table_rows(table)
print '**********'
print rows
print '**********'

# assert_number_of_rows_in_table(table, 5)
# assert_col_in_row_contains_text(table, 'Jill', row_number=4, col_number=1)

# Revisi berdasarkan kondisi terkini di web w3choolnya
assert_number_of_rows_in_table(table, 7)
assert_col_in_row_contains_text(table, 'UK', row_number=4, col_number=2)

# Run this script
# python _050_051_Tables.py
