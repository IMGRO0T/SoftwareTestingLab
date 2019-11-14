# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TC27Py(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_t_c27_py(self):
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
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Toggle navigation'])[1]/following::i[2]").click()
        driver.find_element_by_link_text("PROFILE SETTINGS").click()
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("NITK")
        driver.find_element_by_id("country").click()
        driver.find_element_by_id("country").clear()
        driver.find_element_by_id("country").send_keys("INDIA")
        driver.find_element_by_id("city").click()
        driver.find_element_by_id("city").clear()
        driver.find_element_by_id("city").send_keys("Surathkal")
        driver.find_element_by_name("updateprofile").click()
    
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
