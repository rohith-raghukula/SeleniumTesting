from selenium import webdriver

def test_form_submission():
    # Create a Chrome driver instance
    driver = webdriver.Chrome()

    # Navigate to the test page
    driver.get("http://example.com")

    # Find the form elements and enter data
    name_input = driver.find_element_by_name("name")
    name_input.send_keys("John Doe")

    email_input = driver.find_element_by_name("email")
    email_input.send_keys("john.doe@example.com")

    # Submit the form
    form = driver.find_element_by_tag_name("form")
    form.submit()

    # Verify that the form was submitted successfully
    assert "Thank you for submitting the form!" in driver.page_source

    # Close the driver instance
    driver.quit()
