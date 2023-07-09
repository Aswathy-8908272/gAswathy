# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.w3schools.com/")
time.sleep(3)

# Open the W3Schools website
driver.get("https://www.w3schools.com/")

# Find the search input element by its ID and enter the search query
search_input = driver.find_element(id, "gsc-i-id1")  # Replace "gsc-i-id1" with the actual search input ID
search_input.send_keys("Python")

# Press Enter to perform the search
search_input.send_keys(Keys.RETURN)

# Wait for the search results to load
driver.implicitly_wait(5)

# Click on the "Try Yourself" button
try_yourself_button = driver.find_element(By.XPATH, "//a[contains(text(),'Try Yourself')]")
try_yourself_button.click()

# Switch to the iframe containing the interactive code editor
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[contains(@src, 'default') and contains(@src, 'tryit') and not(contains(@src, 'result'))]"))

# Find the input code editor and enter the correct answer
input_code_editor = driver.find_element(By.ID, "textareaCode")
input_code_editor.clear()
input_code_editor.send_keys("print('Hello, world!')")

# Click on the "Submit" button
submit_button = driver.find_element(BY.XPATH, "//button[contains(text(),'Submit')]")
submit_button.click()

# Quit the browser
driver.quit()

