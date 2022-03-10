from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("http://200.10.11.2/home/")

driver.maximize_window()
driver.implicitly_wait(10)

time.sleep(2)
driver.find_element_by_xpath(
    '//*[@id="case-studies-section"]/div/div[2]/div/div/div[1]/div[2]/div/a').click()
time.sleep(2)
# driver.find_element_by_css_selector(
#     "#case-studies-section > div > div:nth-child(2) > div > div > div.bg-primary.text-center.card-contents > div.card-desc-box.d-flex.align-items-center.justify-content-around > div > a").click()
driver.find_element_by_id("username").send_keys("ikhsan")
driver.find_element_by_id("userpass").send_keys("gip")
time.sleep(2)
driver.find_element_by_css_selector(
    "body > div.limiter > div > div > form > div.container-login100-form-btn > button").click()
time.sleep(2)
driver.find_element_by_xpath(
    "/html/body/div[1]/aside/section/ul/li[6]/a").click()


# driver.find_element_by_xpath(
#     "/html/body/div[1]/aside/section/ul/li[3]/ul/li[5]/a").click()

# driver.find_element_by_css_selector(
#     "body > div.wrapper > aside > section > ul > li.treeview.menu-open > ul > li:nth-child(5) > a").click()

# ActionChains(driver).move_to_element(
#     (driver.find_element_by_link_text("Publishing Admin"))).click()

ActionChains(driver).move_to_element(
    (driver.find_element_by_class_name(" Produk Set"))).click()
