from selenium import webdriver

class TestGoogleSearch():
    @classmethod
    def setup_class(cls):
        # Create a new Chrome browser instance
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def teardown_class(cls):
        # Close the browser
        cls.driver.quit()

    def test_google_search(self):
        # Navigate to the Google homepage
        self.driver.get("https://www.google.com")

        # Find the search input element and enter a search query
        search_box = self.driver.find_element_by_name("q")
        search_box.send_keys("python selenium")
        search_box.submit()

        # Assert that the search results page was loaded successfully
        assert "Python Selenium - Google Search" in self.driver.title
