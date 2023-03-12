from selenium import webdriver
import os

url = "https://www.google.com/"

# Use headless mode
options = webdriver.FirefoxOptions()
options.headless = True

# Set the path of the Firefox binary
firefox_binary_path = "/usr/bin/firefox-esr"
options.binary_location = firefox_binary_path

# Set the display port as an environment variable
display_port = os.environ.get("DISPLAY_PORT", "99")
display = f":{display_port}"
os.environ["DISPLAY"] = display

# Start the Xvfb server
xvfb_cmd = f"Xvfb {display} -screen 0 1024x768x24 -nolisten tcp &"
os.system(xvfb_cmd)

# Start the Firefox driver
driver = webdriver.Firefox(options=options)

# Go to Google.com
driver.get(url)

# Print the page source
print(driver.page_source)

# Close the browser
driver.quit()
