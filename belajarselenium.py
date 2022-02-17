from selenium import webdriver
# cara lain #1
from selenium.webdriver.common.by import By
#  ===================================================================================================
import time

# create variable untuk chrome driver windows yg sudah kita download
driver = webdriver.Chrome()

#  ===================================================================================================
# CASE 1 =============================================================================================

# membuka alamat web untuk kita automasi
# driver.get("https://the-internet.herokuapp.com/login")

# single method == find_element
# plural method == find_elements
# 1 -- by id
# driver.find_element_by_id("username").send_keys("uno")

# 2 -- by name
# driver.find_element_by_name("username").send_keys("ikhsan")

# 3 -- by link text
# driver.find_element_by_link_text("Elemental Selenium").click()
# driver.find_element_by_partial_link_text("Elemental").click()

# 4 -- by tag name
# private method yg me-return sebuah list
# h2 = driver.find_element_by_tag_name("h2")
# print(h2)

# menghitung berapa link tag yang ada di 1 halaman dummy
# link tag di awali dengan tag "a"
# link = driver.find_elements_by_tag_name("a")
# print(len(link))

# 5 -- by class name
# driver.find_element_by_class_name("radius").click()

# 6 -- by css selector
# time.sleep(20)
# driver.find_element_by_css_selector("tagname.classname").click()
# type 1
# driver.find_element_by_css_selector("button.radius").click()
# type 2 untuk elemen yg tidak memiliki nama class
# inspect --> klik kanan pada tag --> copy --> copy selector --> paste di dalam find_element
# driver.find_element_by_css_selector("#login > button").click()

#  ===================================================================================================
# CASE 2 =============================================================================================

# membuka alamat web untuk kita automasi
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

time.sleep(15)
# driver.find_element_by_css_selector("#content > div > button").click()

# 7 -- by xpath
# driver.find_element_by_xpath('//*[@id="content"]/div/button').click()

# cara lain #1
driver.find_element(By.XPATH, '//*[@id="content"]/div/button').click()
