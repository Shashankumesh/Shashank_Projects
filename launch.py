from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Create Chrome options
options = Options()
#options.add_argument("--start-maximized")  # Optional: Open browser maximized

# Set up ChromeDriver using webdriver-manager
#service = Service(ChromeDriverManager().install())

# Launch the browser
driver = webdriver.Chrome(options=options)

# Open a webpage
driver.maximize_window()
driver.get("https://www.google.com")
time.sleep(10)
driver.close()
