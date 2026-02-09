import handle
from selenium import webdriver
import time

from variables import a

# Launch browser
driver = webdriver.Chrome()

# Open the main page
driver.maximize_window()
driver.get("https://www.amazon.in")
#driver.find_element("xpath","//button[@type='submit']").click()
# Store the ID of the original window
parent_window = driver.current_window_handle
#import pdb;pdb.set_trace()
print(parent_window)
# Click a link that opens a new window
driver.find_element("xpath","//div[@id='nav-cart-count-container']").click()
# Wait for new window to open
all_handles = driver.window_handles
print(all_handles)
for handles in all_handles:
    if handles != parent_window:
        driver.switch_to.window(handles)
        break
time.sleep(5)
print("Title of new window",driver.title)
driver.close()

driver.switch_to.window(parent_window)
print("back to main window:",driver.title)
#driver.find_element("xpath","//span[@class='a-button a-button-base']").click()
time.sleep(5)
# Quit browser
driver.quit()

