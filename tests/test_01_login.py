# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestlogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testlogin(self):
    self.driver.get("https://reunion.azurewebsites.net/")
    self.driver.set_window_size(1524, 822)
    self.driver.find_element(By.ID, "email_login").click()
    self.driver.find_element(By.ID, "email_login").send_keys("testuser123@gmail.com")
    self.driver.find_element(By.ID, "password_login").click()
    self.driver.find_element(By.ID, "password_login").send_keys("123")
    self.driver.find_element(By.ID, "log").click()
    elements = self.driver.find_elements(By.ID, "create-post")
    assert len(elements) > 0
  
