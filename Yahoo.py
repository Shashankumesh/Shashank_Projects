from selenium import webdriver

import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.yahoo.com/")
time.sleep(2)

driver.find_element("xpath","//a[text()='Sign in']").click()
time.sleep(2)
driver.find_element("xpath","//input[@name='username']").send_keys("shashank_rock@yahoo.com")
time.sleep(2)
driver.find_element("xpath","//input[@type='submit']").click()
time.sleep(2)
driver.find_element("xpath","//input[@type='password']").send_keys("Win@7829")
time.sleep(2)
driver.find_element("xpath","//button[@type='submit']").click()
time.sleep(10)
