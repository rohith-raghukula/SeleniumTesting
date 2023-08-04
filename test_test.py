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
        driver = self.driver
        driver.get("https://app.stezy.io")

        # Find the email and password input fields and enter login credentials
        email_input = driver.find_element(By.NAME, "username")
        email_input.send_keys("stezy@stezy.io")

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
        consotrium_name_input.send_keys("fab rohith test")
        time.sleep(5)
        description_textarea = self.driver.find_element(By.TAG_NAME, "textarea")
        description_textarea.send_keys("hi")
        time.sleep(5)
        time.sleep(5)
        next_button = self.driver.find_element(By.XPATH, "//button[@class='ml-auto' and text()='Next']")
        next_button.click()
        time.sleep(5)
        # select blockchain and blockchain type
        fabric_button = self.driver.find_element(By.XPATH, '//*[@id="selectWrapper"]/div[3]')
        fabric_button.click()
        time.sleep(5)
        raft_button = self.driver.find_element(By.XPATH,'/html/body/app-root/div/main/section/app-create-blockchain/div/div/div[1]/div/div[1]/div[2]/div[2]/app-select-tabs/div/div/img')
        raft_button.click()
        time.sleep(5)
        next_button = self.driver.find_element(By.XPATH, "//button[text()='Next']")
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(5)
        SZM_element = self.driver.find_element(By.XPATH,
                                               '//img[@src="https://cdn.stezy.io/assets/images/cloud/stezy.jpeg"]')
        SZM_element.click()
        time.sleep(5)
        next_button = self.driver.find_element(By.XPATH, "//button[text()='Next']")
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(5)
        cluster_element = self.driver.find_element(By.XPATH,"/html/body/app-root/div/main/section/app-create-blockchain/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[2]/input")
        cluster_element.send_keys("1")
        time.sleep(5)

        locations_element = self.driver.find_element(By.XPATH, "/html/body/app-root/div/main/section/app-create-blockchain/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]")
        locations_element.click()
        time.sleep(2)
        eastasia_element = self.driver.find_element(By.XPATH,"/html/body/app-root/div/main/section/app-create-blockchain/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/select/option[9]")
        eastasia_element.click()
        time.sleep(10)
        save_button = driver.find_element(By.CLASS_NAME, "ml-auto")
        save_button.click()
        time.sleep(5)
        ca_element = self.driver.find_element(By.XPATH,"/html/body/app-root/div/main/section/app-create-blockchain/div/div/div[1]/div/ul/li[2]")
        ca_element.click()
        time.sleep(2)
        Name_element = self.driver.find_element(By.NAME,"name")
        Name_element.send_keys("1")
        time.sleep(2)
        caid_element = self.driver.find_element(By.NAME,"ca-id")
        caid_element.send_keys("1")
        time.sleep(2)
        casecreat_element = self.driver.find_element(By.NAME,"ca-secret")
        casecreat_element.send_keys("1")
        time.sleep(2)
        instance_element = self.driver.find_element(By.XPATH,"/html/body/app-root/div/main/section/app-create-blockchain/div/div/div[1]/div/div[1]/div/div[2]/div[6]/div/div[2]/div/div[1]/select")
        instance_element.click()
        time.sleep(2)
        instance2_element = self.driver.find_element(By.XPATH,"/html/body/app-root/div/main/section/app-create-blockchain/div/div/div[1]/div/div[1]/div/div[2]/div[6]/div/div[2]/div/div[1]/select/option[2]")
        instance2_element.click()
        time.sleep(2)
        add_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Add')]")

        # Add an explicit wait to ensure the button is clickable
        wait = WebDriverWait(self.driver, 10)
        add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add')]")))

        # Click the element using JavaScript click
        self.driver.execute_script("arguments[0].click();", add_button)
        time.sleep(5)
        order_element = self.driver.find_element(By.XPATH, "/html/body/app-root/div/main/section/app-create-blockchain/div/div/div[1]/div/ul/li[3]")
        order_element.click()
        time.sleep(2)
        name_element = self.driver.find_element(By.XPATH,"/html/body/app-root/div/main/section/app-create-blockchain/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[2]/input")
        name_element.send_keys("1")
        time.sleep(2)
        MSP_elemetn = self.driver.find_element(By.XPATH,"/html/body/app-root/div/main/section/app-create-blockchain/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/input")
        MSP_elemetn.send_keys("2")
        time.sleep(2)
        caadmin_element = self.driver.find_element(By.XPATH,"/html/body/app-root/div/main/section/app-create-blockchain/div/div/div[1]/div/div[1]/div/div[2]/div[4]/div/div[2]/input")
        caadmin_element.send_keys("1")
        time.sleep(2)
        node_element = self.driver.find_element(By.XPATH,"/html/body/app-root/div/main/section/app-create-blockchain/div/div/div[1]/div/div[1]/div/div[2]/div[6]/div/div[2]/div/div[1]/select/option[2]")
        node_element.click()
        time.sleep(2)
        add_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Add')]")

        # Add an explicit wait to ensure the button is clickable
        wait = WebDriverWait(self.driver, 10)
        add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add')]")))

        # Click the element using JavaScript click
        self.driver.execute_script("arguments[0].click();", add_button)
        time.sleep(5)
        peer_element = self.driver.find_element(By.XPATH,"/html/body/app-root/div/main/section/app-create-blockchain/div/div/div[1]/div/ul/li[4]")
        peer_element.click()
        time.sleep(2)
        peer_name_element = self.driver.find_element(By.XPATH,"/html/body/app-root/div/main/section/app-create-blockchain/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div/table/tbody/tr[1]/td[1]/input")
        peer_name_element.send_keys("1")
        time.sleep(2)
        description_element = self.driver.find_element(By.XPATH,"/html/body/app-root/div/main/section/app-create-blockchain/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div/table/tbody/tr[1]/td[2]/input")
        description_element.send_keys("1")
        time.sleep(2)
        button_element = self.driver.find_element(By.XPATH,"/html/body/app-root/div/main/section/app-create-blockchain/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div/table/tbody/tr[1]/td[4]/div/img")
        button_element.click()
        time.sleep(2)
        instance3_element = self.driver.find_element(By.XPATH,"/html/body/app-root/div/main/section/app-create-blockchain/div/div/div[1]/div/div[1]/div/div[2]/div[3]/div/div[2]/div/div[1]/select/option[2]")
        instance3_element.click()
        time.sleep(2)
        add_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Add')]")

        # Add an explicit wait to ensure the button is clickable
        wait = WebDriverWait(self.driver, 10)
        add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add')]")))

        # Click the element using JavaScript click
        self.driver.execute_script("arguments[0].click();", add_button)
        time.sleep(5)





