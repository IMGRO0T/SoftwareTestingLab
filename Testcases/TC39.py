# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TC39(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_t_c39(self):
        driver = self.driver
        driver.get("http://localhost/carrentalproject/carrental/index.php")
        driver.find_element_by_link_text("LOGIN / REGISTER").click()
        driver.find_element_by_link_text("Forgot Password ?").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password Recovery'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password Recovery'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password Recovery'])[1]/following::input[1]").send_keys("test@gmail.com")
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("9999857868")
        driver.find_element_by_name("newpassword").click()
        driver.find_element_by_name("newpassword").clear()
        driver.find_element_by_name("newpassword").send_keys("1")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password Recovery'])[1]/following::input[4]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password Recovery'])[1]/following::input[4]").clear()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password Recovery'])[1]/following::input[4]").send_keys("1")
        driver.find_element_by_name("update").click()
    
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
