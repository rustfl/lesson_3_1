import unittest

from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)

    def tearDown(self) -> None:
        self.browser.quit()

    def fill_form_fields(self) -> None:
        self.browser.find_element_by_css_selector('.first_block .first').send_keys('Harry')
        self.browser.find_element_by_css_selector('.first_block .second').send_keys('Potter')
        self.browser.find_element_by_css_selector('.first_block .third').send_keys('harry_potter@hogwarts.com')

        self.browser.find_element_by_xpath('//button').click()

    def test_success_login(self) -> None:
        self.browser.get("http://suninjuly.github.io/registration1.html")

        self.fill_form_fields()

        self.assertEqual("Congratulations! You have successfully registered!", self.browser.find_element_by_xpath('//h1').text)

    def test_fail_login(self) -> None:
        self.browser.get("http://suninjuly.github.io/registration2.html")

        # with self.assertRaises(NoSuchElementException):
        #     self.fill_form_fields()

        self.fill_form_fields()

        self.assertEqual("Congratulations! You have successfully registered!", self.browser.find_element_by_xpath('//h1').text)


if __name__ == '__main__':
    unittest.main()
