# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TC01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_t_c01(self):
        driver = self.driver
        driver.get("http://localhost/carrentalproject/carrental/index.php")
        driver.find_element_by_link_text("LOGIN / REGISTER").click()
        driver.find_element_by_link_text("Signup Here").click()
        driver.find_element_by_name("fullname").click()
        driver.find_element_by_name("fullname").clear()
        driver.find_element_by_name("fullname").send_keys("Rupesh")
        driver.find_element_by_name("mobileno").click()
        driver.find_element_by_name("mobileno").clear()
        driver.find_element_by_name("mobileno").send_keys("Nitnaware")
        driver.find_element_by_id("emailid").click()
        driver.find_element_by_id("emailid").clear()
        driver.find_element_by_id("emailid").send_keys("test03@gmail.com")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Sign Up'])[1]/following::input[4]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Email available for Registration .'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Email available for Registration .'])[1]/following::input[1]").send_keys("1")
        driver.find_element_by_name("confirmpassword").click()
        driver.find_element_by_name("confirmpassword").clear()
        driver.find_element_by_name("confirmpassword").send_keys("1")
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
