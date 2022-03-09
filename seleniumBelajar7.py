from lib2to3.pgen2 import driver
# from time import time
from selenium import webdriver
from webbrowser import get
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

for i in range(2):
    driver.get("https://tees.co.id/")

    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]')))
        print("pop up muncul")
        driver.find_element_by_class_name("btn-modal-close").click()
        print("pop up di close")

    except TimeoutException:
        print("pop up tidak muncul")
    pass

    time.sleep(3)
