from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
time.sleep(5)
# Click button that triggers alert
driver.find_element(By.ID,"alertButton").click()

# Switch to alert
alert = driver.switch_to.alert

# Print alert text
print("Alert says:", alert.text)

# Accept the alert (OK)
alert.accept()

time.sleep(2)

# Trigger another alert
driver.find_element(By.ID, "confirmButton").click()

# Switch to confirm alert
confirm = driver.switch_to.alert

# Dismiss the alert (Cancel)
confirm.dismiss()

time.sleep(5)

# Trigger prompt alert
driver.find_element(By.XPATH, "//button[@type='button']").click()

prompt = driver.switch_to.alert
print("Prompt text:", prompt.text)

# Send text to prompt
prompt.send_keys("Shashank")
prompt.accept()

driver.quit()

#driver.manage().timeouts().implicitly_wait(5)
#driver.switch_to.frame("iframeResult")


#driver.implicitly_wait(3)