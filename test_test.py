import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
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
        email_input.send_keys("rohith5@mailinator.com")
        time.sleep(5)
        # Find the radio button for admin role
        admin_radio_button = self.driver.find_element(By.XPATH, "//input[@name='isAdmin' and @value='admin']")
        # Click the radio button
        admin_radio_button.click()
        time.sleep(5)
        Text_label = self.driver.find_element(By.CSS_SELECTOR,
                                         "label[for='Do you want admin to delete blockchain & nodes?']")
        Text_label.click()
        add_user_button = self.driver.find_element(By.NAME, "LogIn")
        add_user_button.click()
        print("hola")
        time.sleep(10)
        close_button = self.driver.find_element(By.XPATH, "//button[text()='Close']")
        close_button.click()
        time.sleep(10)
