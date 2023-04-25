import unittest
import self
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


import time

from selenium.webdriver.support.wait import WebDriverWait


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

        # Find the Blockchain element and click it
        blockchain_button = self.driver.find_element(By.XPATH, "//span[@class='nav-label' and text()='Blockchain']")
        blockchain_button.click()
        time.sleep(5)

        create_private_element = self.driver.find_element(By.XPATH, '//span[@class="nav-label" and text()="Private"]')
        create_private_element.click()
        time.sleep(5)

        consotrium_name_input = self.driver.find_element(By.NAME, "name")
        consotrium_name_input.send_keys("eth rohith test")
        time.sleep(5)
        description_textarea = self.driver.find_element(By.TAG_NAME, "textarea")
        description_textarea.send_keys("hi")
        time.sleep(5)
        time.sleep(5)
        next_button = self.driver.find_element(By.XPATH, "//button[@class='ml-auto' and text()='Next']")
        next_button.click()
        time.sleep(5)
        # select blockchain and blockchain type
        ethereum_button = self.driver.find_element(By.XPATH,
                                                   "//div[@class='card ng-star-inserted']//img[contains(@src, 'ethereum.png')]")
        ethereum_button.click()
        time.sleep(5)
        poa_button = self.driver.find_element(By.XPATH,
                                              "//img[@class='ng-star-inserted' and contains(@src, 'poa.jpeg')]")
        poa_button.click()
        time.sleep(5)
        next_button = self.driver.find_element(By.XPATH, "//button[text()='Next']")
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(5)
        SZM_element = self.driver.find_element(By.XPATH, '//img[@src="https://cdn.stezy.io/assets/images/cloud/stezy.jpeg"]')
        SZM_element.click()
        time.sleep(5)
        next_button = self.driver.find_element(By.XPATH, "//button[text()='Next']")
        driver.execute_script("arguments[0].click();", next_button)
        name_element = self.driver.find_element(By.NAME, "name")
        name_element.send_keys("node1")
        description_element = self.driver.find_element(By.XPATH,'//textarea[@placeholder="Example: Node description"]')
        description_element.send_keys("node des")

        dropdown_element = self.driver.find_element(By.NAME,'region')
        dropdown_element.click()


        # Wait for the dropdown options to be visible
        wait = WebDriverWait(self.driver, 10)
        dropdown_options = wait.until(
            EC.visibility_of_all_elements_located((By.XPATH, "//select[@name='region']/option")))

        # Loop through the dropdown options and select the desired option by its text
        for option in dropdown_options:
            if option.text == 'East Asia':
                option.click()
                break

        time.sleep(10)
        wait = WebDriverWait(self.driver, 10)
        instance_options = wait.until(
            EC.visibility_of_all_elements_located((By.XPATH, "//select[@name='type']/option")))
        # Click on the option element
        # Loop through the dropdown options and select the desired option by its text
        for option in instance_options:
            if option.text == 'Standard_A2_v2 (2 VCPUs, 4 GB)':
                option.click()
                break

        time.sleep(5)

        save_button = driver.find_element(By.CLASS_NAME, "ml-auto")
        save_button.click()
        time.sleep(5)

