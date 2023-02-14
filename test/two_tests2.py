from selenium import webdriver

def test_button_click():
    # Create a Chrome driver instance
    driver = webdriver.Chrome()

    # Navigate to the test page
    driver.get("http://example.com")

    # Find the button element and click on it
    button = driver.find_element_by_xpath("//button[@id='my-button']")
    button.click()

    # Verify that the button click worked
    assert "Button clicked!" in driver.page_source

    # Close the driver instance
    driver.quit()
