import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Beginning script testGitHubLogin...")

# Retrieve email and password from environment variables
print("Retrieving username/email/password from environment variables...")
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

def get_username_from_tags(driver, tags):
    for tag, attribute in tags:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//meta[@name='{tag}']"))
            )
            content = element.get_attribute(attribute)
            if content:
                return content
        except:
            continue
    return None

# After logging in, check the metadata for the username
print("Checking the metadata for the username...")

tags_to_check = [
    ("octolytics-actor-login", "content"),
    ("user-login", "content"),
    ("alternate", "href")
]

found_username = get_username_from_tags(driver, tags_to_check)

# Compare the found username with the expected username
if found_username == expected_username:
    print(f"Username matches expected: {found_username}")
else:
    print(f"Error: Expected username '{expected_username}' but found '{found_username if found_username else 'None'}'.")
    print(driver.page_source)

# ... Continue with the rest of your test steps, i.e. verify login, etc...

# Close the browser at the end
print("Closing the browser....")
driver.quit()

print("Script testGitHubLogin completed.")
