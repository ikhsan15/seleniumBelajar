from select import select
from tkinter.tix import Select
from selenium import webdriver
from webbrowser import get
import time

driver = webdriver.Chrome()
driver.get("http://200.10.11.2/home/")

driver.find_element_by_xpath(
    '//*[@id="case-studies-section"]/div/div[2]/div/div/div[1]/div[2]/div/a').click()
# driver.find_element_by_css_selector(
#     "#case-studies-section > div > div:nth-child(2) > div > div > div.bg-primary.text-center.card-contents > div.card-desc-box.d-flex.align-items-center.justify-content-around > div > a").click()
driver.find_element_by_id("username").send_keys("ikhsan")
driver.find_element_by_id("userpass").send_keys("gip")

driver.find_element_by_css_selector(
    "body > div.limiter > div > div > form > div.container-login100-form-btn > button").click()


driver.find_element_by_xpath(
    "/html/body/div[1]/aside/section/ul/li[3]").click()
