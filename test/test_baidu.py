import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.config import Config, DRIVER_PATH


class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.URL)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_search0(self):
        self.driver.find_element(*self.locator_kw).send_keys('selenium 灰蓝')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)

    def test_search1(self):
        self.driver.find_element(*self.locator_kw).send_keys('Python selenium')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)


if __name__ == '__main__':
    unittest.main()
