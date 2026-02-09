from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://zigzag.lk/collections/gift-cards")

time.sleep(5)

driver.find_element("xpath","//a[text()='Zigzag E-Gift Cards']").click()

time.sleep(5)

driver.close()