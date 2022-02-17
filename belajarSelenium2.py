from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")

time.sleep(10)
driver.find_element_by_link_text("Click Here").click()

time.sleep(5)
# pindah ke tab pertama
# value == 0
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_link_text("Click Here").click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_link_text("Click Here").click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_link_text("Click Here").click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_link_text("Click Here").click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
