from selenium import webdriver

class TestGoogleSearch():
    @classmethod
    def setup_class(cls):
        # Create a new Chrome browser instance
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)


    # Navigate to Google search page
    driver.get("https://www.google.com/")

    # Locate the search bar element and enter a search query
    search_box = driver.find_element_by_name("q")
    search_box.send_keys("python selenium")
    search_box.submit()

    # Verify that the search results page was loaded successfully
    assert "Python Selenium - Google Search" in driver.title

    # Close the driver instance
    driver.quit()
