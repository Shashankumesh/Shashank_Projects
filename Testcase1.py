import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class TestBrowserLaunch(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.driver = None

    def setUp(self):
        options = Options()
        # Initialize the WebDriver with Chrome options
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)  # Wait for elements if needed

    def test_launch_browser(self):
        try:
            self.driver.get("https://www.google.com")
            time.sleep(3)  # Pause for visibility (not required for actual test)
            self.assertIn("Google", self.driver.title)
            # ✅ Pass if page title contains 'Google'
            print("Test Passed: Browser launched and Google opened successfully.")
        except Exception as e:
            print(f"Test Failed: {e}")
            self.fail("Browser did not launch or load Google page correctly.")

    def tearDown(self):
        if self.driver:
            self.driver.quit()  # Close the browser


if __name__ == "__main__":
    unittest.main()
