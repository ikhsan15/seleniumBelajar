# belajar implicitly wait
# metode wait yg akan menunggu dalam waktu tertentu untuk menjalankan setiap step selanjutnya

from lib2to3.pgen2 import driver
from selenium import webdriver
from webbrowser import get
import time

driver = webdriver.Chrome()

driver.implicitly_wait(10)
# hanya sekali declare dalam 1 project / file
# misalnya explicitly wait nya 10 detik
# setiap elemen yg di cek akan di tunggu max 10 detik

driver.get("https://demoqa.com/login")  # di tunggu max 10 detik
driver.get("https://demoqa.com/books")  # di tunggu max 10 detik
driver.find_element_by_id("login").click()  # di tunggu max 10 detik
