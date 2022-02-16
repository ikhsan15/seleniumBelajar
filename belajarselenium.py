from selenium import webdriver

# create variable untuk chrome driver windows yg sudah kita download
driver = webdriver.Chrome()

# membuka alamat web untuk kita automasi
driver.get("https://the-internet.herokuapp.com/login")

# single method == find_element
# driver.find_element_by_id("username").send_keys("uno")
# driver.find_element_by_name("username").send_keys("ikhsan")
# driver.find_element_by_link_text("Elemental Selenium").click()
# driver.find_element_by_partial_link_text("Elemental").click()

# private method yg me-return sebuah list
# h2 = driver.find_element_by_tag_name("h2")
# print(h2)

# menghitung berapa link tag yang ada di 1 halaman dummy
# link tag di awali dengan tag "a"
link = driver.find_elements_by_tag_name("a")
print(len(link))
