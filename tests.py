from selenium import webdriver



# Launch a new instance of the browser
with webdriver.Firefox() as driver:
    pass  # nothing to do here, the browser will close automatically

# Launch a new instance of the browser with the configured options
with webdriver.Firefox(options=options) as driver:
    # Perform any necessary actions here, such as navigating to a URL or interacting with elements
    driver.get('https://www.google.com')
    print(driver.title)  # should print "Google"

# The browser window will automatically close when the `with` block is exited
This example uses Firefox as the browser, but you can replace webdriver.Firefox with webdriver.Chrome or webdriver.Edge to use a different browser. The options object is used to configure the browser to run in headless mode, which means that no GUI will be displayed.

Note that if you don't need to interact with the browser at all, you can simply create a new instance of the browser using the webdriver.<BrowserName>() constructor without any options, and the browser window will automatically close when the script completes. For example:

python
Copy code
from selenium import webdriver

# Launch a new instance of the browser
with webdriver.Firefox() as driver:
    pass  # nothing to do here, the browser will close automatically



Regenerate response
