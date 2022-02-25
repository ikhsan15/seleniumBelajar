from lib2to3.pgen2 import driver
from webbrowser import get
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/alerts")
time.sleep(5)

#  ===================================================================================================
# CASE 1 =============================================================================================
# driver.find_element_by_id("alertButton").click()
# time.sleep(5)
# # handle alert with accept
# driver.switch_to.alert.accept()

#  ===================================================================================================
# CASE 2 =============================================================================================
# driver.find_element_by_id("confirmButton").click()
# time.sleep(5)
# # handle alert with cancel
# driver.switch_to.alert.dismiss()

#  ===================================================================================================
# CASE 3 =============================================================================================
# driver.find_element_by_id("promtButton").click()
driver.find_element_by_css_selector("#promtButton").click()
# time.sleep(5)

driver.switch_to.alert.send_keys("saya sedang test")
driver.switch_to.alert.accept()
