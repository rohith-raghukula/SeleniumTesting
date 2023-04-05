import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait

class TestStezyLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up Firefox options to run in headless mode
        options = Options()
        options.headless = True
        # Create a new Firefox browser instance with the headless options
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


        print("hi")
        time.sleep(10)
        # Check if login was successful
        self.assertIn("dashboard", self.driver.current_url, "Login failed")

        smartcontract_link = self.driver.find_element(By.XPATH, '//span[text()="SmartContract"]')
        smartcontract_link.click()
        time.sleep(5)
        SC_asset_link = self.driver.find_element(By.XPATH, '//p[text()="Code Builder Smart Contract"]')
        SC_asset_link.click()
        time.sleep(5)
        supplychain_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Supplychain")]'))
        )

        # Double-click the button
        action_chains = ActionChains(self.driver)
        action_chains.double_click(supplychain_button).perform()
        track_and_trace_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Track and Trace")
        track_and_trace_link.click()
        time.sleep(10)
        text_field = self.driver.find_element(By.ID, "smart-contract-name")
        text_field.send_keys("Test Smart Contract")
        time.sleep(5)

        wait = WebDriverWait(self.driver, 10)
        deploy_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Deploy']")))
        self.driver.execute_script("arguments[0].click();", deploy_button)
        time.sleep(5)

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
