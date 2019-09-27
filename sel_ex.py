from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#
# browser = webdriver.Chrome()
# browser.get('https://www.google.co.in')
# field = browser.find_element_by_name('q')
# field.send_keys('python')
# field.send_keys(Keys.RETURN)
# if 'python' in browser.title:
#     print('test case success')
# else:
#     print('test case failed')
# import time
# time.sleep(10)
# browser.close()

import unittest


class MyTests(unittest.TestCase):
    def setUp(self):
        print('In setup')
        self.browser = webdriver.Chrome()

    def test_test_case1(self):
        print('testcase1')
        browser = self.browser
        browser.get('https://www.google.co.in')
        field = browser.find_element_by_name('q')
        field.send_keys('python')
        field.send_keys(Keys.RETURN)
        if 'python' in browser.title:
            print('test case success')
        else:
            print('test case failed')

    def test_test_case3(self):
        print('testcase3')
        browser = self.browser
        browser.get('https://www.google.co.in')
        field = browser.find_element_by_name('q')
        field.send_keys('synechron')
        field.send_keys(Keys.RETURN)
        if 'synechron' in browser.title:
            print('test case success')
        else:
            print('test case failed')

    def test_test_case2(self):
        print('testcase2')
        browser = self.browser
        browser.get('https://www.google.co.in')
        field = browser.find_element_by_name('q')
        field.send_keys('wellsfargo')
        field.send_keys(Keys.RETURN)
        if 'wellsfargo' in browser.title:
            print('test case success')
        else:
            print('test case failed')

    def tearDown(self):
        import time
        time.sleep(5)
        self.browser.close()


if __name__ == '__main__':
    unittest.main()
