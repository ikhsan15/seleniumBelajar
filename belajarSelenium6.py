# belajar explicitly wait
# hanya menunggu hanya 1 atau beberapa element yang di pilih

from lib2to3.pgen2 import driver
from selenium import webdriver
from webbrowser import get
import time

# kebutuhan explicitly wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# handle agar script tetap jalan ketika element tidak muncul2
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")

driver.find_element_by_id("timerAlertButton").click()

try:
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    print("alert di klick")

except TimeoutException:
    print("alert tidak muncuk")
    pass
