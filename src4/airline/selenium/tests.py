import os
import pathlib
import unittest

from selenium import webdriver


def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome()

#driver = webdriver.Firefox()


class WebpageTests(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, "Counter")

    def test_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element_by_id("increase")
        increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "1")

    def test_baci_5(self):
        driver.get(file_uri("counter.html"))
        baci_5 = driver.find_element_by_id("baci_5")
        baci_5.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "5")

    def test_decrease(self):
        driver.get(file_uri("counter.html"))
        decrease = driver.find_element_by_id("decrease")
        decrease.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "-1")

    def test_multiple_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element_by_id("increase")
        for i in range(10):
            increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "10")


if __name__ == "__main__":
    unittest.main()
