# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TC31(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_t_c31(self):
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
        driver.find_element_by_link_text("Update Password").click()
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("2")
        driver.find_element_by_name("chngpwd").click()
        driver.find_element_by_id("newpassword").click()
        driver.find_element_by_id("newpassword").clear()
        driver.find_element_by_id("newpassword").send_keys("1")
        driver.find_element_by_id("confirmpassword").click()
        driver.find_element_by_id("confirmpassword").clear()
        driver.find_element_by_id("confirmpassword").send_keys("1")
        driver.find_element_by_id("submit").click()
    
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
