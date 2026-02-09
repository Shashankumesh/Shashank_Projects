from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Launch browser
driver = webdriver.Chrome()

# Open a sample page with dropdown
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")
driver.maximize_window()

# Switch to iframe (W3Schools demo pages use iframes)
driver.switch_to.frame("iframeResult")
time.sleep(5)

# Locate the dropdown element
dropdown = driver.find_element(By.XPATH, "//select[@id='cars']")

# Create Select object
select = Select(dropdown)

# Select by visible text
select.select_by_visible_text("Volvo")
time.sleep(5)

# Select by value attribute
select.select_by_value("saab")
time.sleep(5)

# Select by index (0-based)
select.select_by_index(2)  # selects "Opel"
time.sleep(5)

# Print all options
for option in select.options:
    print("Option:", option.text)

driver.quit()