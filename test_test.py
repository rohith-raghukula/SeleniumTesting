import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait
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

        user_element = self.driver.find_element(By.XPATH, "//span[contains(text(),'User')]")
        user_element.click()
        time.sleep(5)
        create_user_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'+ Create User')]")
        create_user_button.click()
        time.sleep(5)
        email_input = self.driver.find_element(By.NAME, "email")
        email_input.send_keys("rohit2@mailinator.com")
        time.sleep(5)
        # for member user
        member_radio_button = self.driver.find_element(By.XPATH, "//input[@name='isAdmin' and @value='member']")

        # Click the radio button
        member_radio_button.click()
        time.sleep(5)
        create_consortium_label = self.driver.find_element(By.CSS_SELECTOR, "label[for='Create consortium']")
        create_consortium_label.click()
        delete_consortium_label = self.driver.find_element(By.CSS_SELECTOR, "label[for='Delete consortium']")
        delete_consortium_label.click()
        view_user_label = self.driver.find_element(By.CSS_SELECTOR, "label[for='View User']")
        view_user_label.click()
        invite_user_label = self.driver.find_element(By.CSS_SELECTOR, "label[for='Invite User']")
        invite_user_label.click()
        revoke_user_label = self.driver.find_element(By.CSS_SELECTOR, "label[for='Revoke User']")
        revoke_user_label.click()
        add_user_button = self.driver.find_element(By.NAME, "LogIn")
        add_user_button.click()
        print("hola")
        time.sleep(10)
        close_button = self.driver.find_element(By.XPATH, "//button[text()='Close']")
        close_button.click()
        time.sleep(10)
