# belajar implicitly wait
# metode wait yg akan menunggu dalam waktu tertentu untuk menjalankan setiap step selanjutnya

from lib2to3.pgen2 import driver
from selenium import webdriver
from webbrowser import get
import time

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get("https://demoqa.com/login")
time.sleep(2)
driver.get("https://demoqa.com/books")
time.sleep(2)
driver.find_element_by_id("login").click()
