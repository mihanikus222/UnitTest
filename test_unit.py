import unittest
import time
from selenium import webdriver

class UNIC (unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome(executable_path="C:\\ChromeDriver.exe")
        browser.get(link)
        browser.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.first_class > input').send_keys("Vachoc")
        browser.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.second_class > input').send_keys("Petrov")
        browser.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.third_class > input').send_keys("Vachoc@mail.ru")
        browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome(executable_path="C:\\ChromeDriver.exe")
        browser.get(link)
        browser.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.first_class > input').send_keys("Vachoc")
        browser.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.second_class > input').send_keys("Petrov")
        browser.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.third_class > input').send_keys("Vachoc@mail.ru")
        browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text


if __name__ == "__main__":
    unittest.main()
    
