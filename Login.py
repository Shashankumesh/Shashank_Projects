from selenium import webdriver

import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.amazon.in/")
time.sleep(5)
#driver.find_element("xpath","//button[@type='submit']").click()
#time.sleep(2)
driver.find_element("xpath","//span[@class='nav-line-2 ']").click()
time.sleep(2)
driver.find_element("xpath","//input[@type='email']").send_keys("shashanksodu@gmail.com")
driver.find_element("xpath","//span[@class='a-button a-spacing-top-small a-button-span12 a-button-primary aok-relative']").click()
time.sleep(2)
driver.find_element("xpath","//input[@type='password']").send_keys("amazon123")
time.sleep(2)
driver.find_element("xpath","//span[@class='a-button a-button-span12 a-button-primary auth-disable-button-on-submit']").click()
time.sleep(2)

#driver.find_element("xpath","//input[@type='password']").send_keys("")

