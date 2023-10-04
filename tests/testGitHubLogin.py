import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Beginning script testGitHubLogin...")

# Retrieve email and password from environment variables
print("Retrieving email and password from environment variables...")
expected_username = os.environ.get('USERNAME')
email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')

if not email or not password or not expected_username:
    print("Error: USERNAME/EMAIL/PASSWORD environment variables are not set.")
    exit(1)

# Set up the Chrome WebDriver and navigate to GitHub's login page
print("Setting up the Chrome WebDriver and navigating to GitHub's login page...")
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")  # This flag will prevent the "controlled by automation" bar from appearing
driver = webdriver.Chrome(options=options)
driver.get("https://github.com/login")

# Find the email input field and enter the email from the environment variable
print("Finding the email input field and entering an email...")
email_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "login_field"))
)
email_input.send_keys(email)

# Find the password input field and enter the password from the environment variable
print("Finding the password input field and entering the password...")
password_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "password"))
)
password_input.send_keys(password)

# Find the "Sign in" button and click it
print("Finding the 'Sign in' button and clicking it...")
sign_in_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@type='submit'][@value='Sign in']"))
)
sign_in_button.click()

# After logging in, check the metadata for the username
print("Checking the metadata for the username...")
meta_tag = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//meta[@name='user-login']"))
)
meta_content = meta_tag.get_attribute("content")

# Compare the content of the meta tag with the expected username
if meta_content == expected_username:
    print(f"Metadata username matches expected: {meta_content}")
else:
    print(f"Error: Expected username '{expected_username}' in metadata but found '{meta_content}'.")

# ... Continue with the rest of your test steps, i.e. verify login, etc...

# Close the browser at the end
print("Closing the browser....")
driver.quit()

print("Script testGitHubLogin completed.")
