from selenium import webdriver

# Create a new Chrome browser instance
driver = webdriver.Chrome()

# Navigate to the Google homepage
driver.get("https://www.google.com")

# Find the search input field and enter a search query
search_box = driver.find_element_by_name("q")
search_box.send_keys("example search query")
search_box.submit()

# Verify that the search results page was loaded
assert "Google Search Results" in driver.title

# Close the browser
driver.quit()
