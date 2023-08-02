import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


class TestStezyLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up Chrome options to run in headless mode
        options = Options()

        options.add_argument('-headless')
        service = Service('path/to/geckodriver')
        # Create a new firefox browser instance with the headless options
        capabilities = {'loggingPrefs': {'browser': 'ALL'}}
        service = Service('path/to/geckodriver')
        cls.driver = webdriver.Firefox(options=options, executable_path='geckodriver', service_log_path='geckodriver.log', desired_capabilities=capabilities)
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
      #Find the login button and click it
        login_button = driver.find_element(By.NAME, "LogIn")
        login_button.click()
        time.sleep(10)
        # Check if login was successful
        self.assertIn("dashboard", self.driver.current_url, "Login failed")
        time.sleep(5)
        chaincode_link = self.driver.find_element(By.XPATH, '//span[text()="Chaincode"]')
        chaincode_link.click()
        time.sleep(5)
        SC_asset_link = self.driver.find_element(By.XPATH, '//p[text()="Chaincode From Scratch"]')
        SC_asset_link.click()
        time.sleep(5)
        formtitle_input = self.driver.find_element(By.NAME, "formtitle")
        formtitle_input.send_keys("test1")
        time.sleep(5)
        # Add text input field
        text_input_field = self.driver.find_element(By.XPATH, "//li[@data-type='text']")
        text_input_field.click()
        time.sleep(5)

        time.sleep(2)
        # Add number input field
        number_input_field = self.driver.find_element(By.XPATH, "//li[@data-type='number']")
        number_input_field.click()

        time.sleep(10)
        wait = WebDriverWait(driver, 10)
        deploy_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Deploy')]")))
        actions = ActionChains(driver)
        actions.move_to_element(deploy_button).click().perform()
        # Click the deploy button
        deploy_button.click()
        time.sleep(5)


    if __name__ == '__main__':
        unittest.main()
