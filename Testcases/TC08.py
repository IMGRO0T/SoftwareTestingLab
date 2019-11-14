# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TC08(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_t_c08(self):
        driver = self.driver
        driver.get("http://localhost/carrentalproject/carrental/index.php")
        driver.find_element_by_link_text("LOGIN / REGISTER").click()
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("test@gmail.com")
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("1")
        driver.find_element_by_name("login").click()
        driver.find_element_by_link_text("CAR LISTING").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='CNG'])[2]/following::a[1]").click()
        driver.find_element_by_name("fromdate").click()
        driver.find_element_by_name("fromdate").clear()
        driver.find_element_by_name("fromdate").send_keys("22/07/2019")
        driver.find_element_by_name("todate").click()
        driver.find_element_by_name("todate").clear()
        driver.find_element_by_name("todate").send_keys("23/07/2019")
        driver.find_element_by_name("message").click()
        driver.find_element_by_name("message").clear()
        driver.find_element_by_name("message").send_keys("Book")
        driver.find_element_by_name("submit").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
