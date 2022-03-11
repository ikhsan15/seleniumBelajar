from lib2to3.pgen2 import driver
from re import I
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demoqa.com/upload-download")

driver.find_element_by_id("uploadFile").send_keys(
    "C:/Users/ikhsan.n/Downloads/A4-1.pdf")
