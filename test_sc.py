import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait


class TestStezyLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up Chrome options to run in headless mode
        options = Options()
        options.headless = True
        # Create a new Chrome browser instance with the headless options
        cls.driver = webdriver.Firefox(options=options)
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
        smartcontract_link = self.driver.find_element(By.XPATH, '//span[text()="SmartContract"]')
        smartcontract_link.click()
        time.sleep(5)
        SC_asset_link = self.driver.find_element(By.XPATH, '//p[text()="Design Smart Contract Asset"]')
        SC_asset_link.click()
        time.sleep(5)
        variable_input = self.driver.find_element(By.NAME, "form-name")
        variable_input.send_keys("sctest")
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

        print("hi")
        # Find the blockchain radio button and select it
        blockchain_radio = self.driver.find_element(By.NAME, "blockchains")
        blockchain_radio.click()
        time.sleep(5)
        # Find the Next button and click it
        next_button = self.driver.find_element(By.XPATH, "//button[text()='Next']")
        next_button.click()
        time.sleep(5)
        # Find the radio button element for nodes
        nodes_radio_button = self.driver.find_element(By.NAME, "nodes")
        # Verify that the radio button is displayed on the page
        self.assertTrue(nodes_radio_button.is_displayed())
        # Click the radio button
        nodes_radio_button.click()
        time.sleep(5)
        deploy_button = self.driver.find_element(By.XPATH, "//button[text()='Deploy']")
        deploy_button.click()
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()
