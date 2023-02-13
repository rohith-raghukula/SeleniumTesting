from selenium import webdriver

# Create an instance of the Chrome browser
driver = webdriver.Chrome()

# Navigate to the Google website
driver.get("https://www.google.com")

# Find the search input element and enter a search query
search_box = driver.find_element_by_name("q")
search_box.send_keys("python selenium")
search_box.submit()

# Assert that the search results page was loaded successfully
assert "Python Selenium - Google Search" in driver.title

# Close the browser
driver.quit()
