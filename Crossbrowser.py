from selenium import webdriver

for browser in ["chrome", "firefox", "edge"]:
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()

    driver.maximize_window()

    driver.get("https://www.google.com")
    print(driver.title)
    driver.quit()