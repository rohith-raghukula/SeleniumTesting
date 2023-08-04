import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import tracemalloc

class TestStezyLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        firefox_options = FirefoxOptions()
        firefox_options.headless = True
        geckodriver_path = os.path.join(os.path.dirname(__file__), 'geckodriver')
        service = Service('path/to/geckodriver')
        cls.driver = webdriver.Firefox(options=firefox_options, service=service)
        cls.driver.implicitly_wait(10)
    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

    def test_stezy_login(self):

        # Navigate to the app.stezy.io homepage
        driver = self.driver
        driver.get("https://app.stezy.io")

        # Find the email and password input fields and enter login credentials
        email_input = driver.find_element(By.NAME, "username")
        email_input.send_keys("rohit@stezy.io")

        password_input = driver.find_element(By.NAME, "Password")
        password_input.send_keys("Stezy@123")

        # Find the login button and click it
        login_button = driver.find_element(By.NAME, "LogIn")
        login_button.click()



        time.sleep(10)
        # Check if login was successful
        self.assertIn("dashboard", self.driver.current_url, "Login failed")

        time.sleep(5)
        chaincode_link = self.driver.find_element(By.XPATH, '//span[text()="Chaincode"]')
        chaincode_link.click()
        time.sleep(5)
        CC_asset_link = self.driver.find_element(By.XPATH, '//p[text()="Design Chaincode Asset"]')
        CC_asset_link.click()
        time.sleep(5)
        variable_input = self.driver.find_element(By.NAME, "form-name")
        variable_input.send_keys("cctest")
        time.sleep(5)
        add_button = self.driver.find_element(By.XPATH, "//button[text()='Add']")
        add_button.click()
        time.sleep(5)
        variable_input = self.driver.find_element(By.NAME, "form-name")
        variable_input.send_keys("test1")
        time.sleep(2)
        # Find the dropdown menu and select the "Integer" option
        integer_option = self.driver.find_element(By.XPATH, "//option[@value='integer']")
        integer_option.click()
        time.sleep(5)
        # Add text input field
        text_input_field = self.driver.find_element(By.NAME, "smart-contract-name")
        text_input_field.send_keys("test-sc")
        time.sleep(5)
        add_button = self.driver.find_element(By.XPATH, "//button[text()='Add']")
        add_button.click()
        time.sleep(5)
        wait = WebDriverWait(driver, 10)
        deploy_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Deploy')]")))
        actions = ActionChains(driver)
        actions.move_to_element(deploy_button).click().perform()
        # Click the deploy button
        deploy_button.click()

        time.sleep(5)

if __name__ == '__main__':
    tracemalloc.start()
    unittest.main()
