from selenium import webdriver

# Configure Chrome options to run in headless mode (no GUI)
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# Launch a new instance of Chrome with the configured options
with webdriver.Chrome(options=options) as driver:
    # Perform any necessary actions here, such as navigating to a URL or interacting with elements
    driver.get('https://www.google.com')
    print(driver.title)  # should print "Google"

# The browser window will automatically close when the `with` block is exited
