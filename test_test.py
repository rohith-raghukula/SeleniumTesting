import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.options import Options



class TestStezyLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up Chrome options to run in headless mode
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        # Create a new Chrome browser instance with the headless options
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

    def test_stezy_login(self):
        # Navigate to the app.stezy.io homepage
        self.driver.get("https://app.stezy.io")

        # Find the email and password input fields and enter login credentials
        email_input = self.driver.find_element(By.NAME, "username")
        email_input.send_keys("rohit@stezy.io")

        password_input = self.driver.find_element(By.NAME, "Password")
        password_input.send_keys("Stezy@123")

        # Find the login button and click it
        login_button = self.driver.find_element(By.NAME, "LogIn")
        login_button.click()

        time.sleep(10)


# Check if login was successful
        self.assertIn("dashboard", self.driver.current_url, "Login failed")
        # Click on the Vulnerability Check link
        EFS_link = self.driver.find_element(By.LINK_TEXT, "EFS")
        EFS_link.click()

        # Find the "Files" tab and click it
        files_tab = self.driver.find_element(By.XPATH, "//div[text()='Files']")
        files_tab.click()
        time.sleep(5)
        download_button = self.driver.find_element(By.XPATH,
                                                  "//span[contains(@class, 'pointer') and contains(text(), 'Download')]")
        download_button.click()

        time.sleep(5)
