import unittest
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import FirefoxOptions, Firefox

class TestStezyLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up Firefox options to run in headless mode
        options = FirefoxOptions()
        options.add_argument('--headless')
        cls.driver = Firefox(options=options)

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
        nft_builder_tile = self.driver.find_element(By.XPATH,"//*[contains(text(), 'NFT Builder')]")
        nft_builder_tile.click()
        time.sleep(5)
        # find the element with the text "ERC-721" using XPath
        erc_element = driver.find_element(By.XPATH,"//div[contains(@class, 'cardTitle') and contains(text(), 'ERC-721')]")
        erc_element.click()
        time.sleep(5)
        next_button = self.driver.find_element(By.ID,"proceedBtn")
        next_button.click()
        time.sleep(5)
        add_element = self.driver.find_element(By.XPATH,"//span[contains(@class, 'material-icons') and contains(text(), 'add')]")
        add_element.click()
        time.sleep(5)
        #upload_element = self.driver.find_element(By.ID,"uploadTitleWrapper")
        #upload_element.click()
        wait = WebDriverWait(driver, 10)
        nft_type_element = self.driver.find_element(By.XPATH, "//div[@class='mat-step-text-label ng-star-inserted'][text()='Choose NFT Type']")
        nft_type_element.click()

        time.sleep(5)
        erc_element = self.driver.find_element(By.CLASS_NAME, "protocolCardContent")
        erc_element.click()
        time.sleep(5)
        name_element = self.driver.find_element(By.XPATH, "//div[@class='mat-step-text-label ng-star-inserted'][text()='Enter collection name']")
        name_element.click()
        input_element = self.driver.find_element(By.ID,"mat-input-0")
        input_element.send_keys("test")
        symbol_element = self.driver.find_element(By.ID, 'cdk-step-label-0-3')
        symbol_element.click()
        symbol_input = self.driver.find_element(By.ID, "mat-input-1")
        symbol_input.send_keys("test")
        time.sleep(5)
        description_element = self.driver.find_element(By.ID, "cdk-step-label-0-4")
        description_element.click()
        description_element_input = self.driver.find_element(By.ID, "mat-input-2")
        description_element_input.send_keys("test")
        create_button = self.driver.find_element(By.ID, "createBtn")
        create_button.click()
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
