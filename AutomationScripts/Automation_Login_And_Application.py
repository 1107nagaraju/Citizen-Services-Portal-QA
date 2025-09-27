from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# --- Test 1: Login ---
try:
    driver.get("http://citizenportal.test/login")
    driver.maximize_window()

    # Enter username
    driver.find_element(By.ID, "username").send_keys("user1")
    # Enter password
    driver.find_element(By.ID, "password").send_keys("Pass123")
    # Click login button
    driver.find_element(By.ID, "loginBtn").click()

    time.sleep(2)  # wait for page to load

    assert "Dashboard" in driver.title
    print("Login Test: PASSED")

except Exception as e:
    print("Login Test: FAILED", e)

# --- Test 2: Service Application Submission ---
try:
    driver.get("http://citizenportal.test/applyService")

    # Fill out service form fields
    driver.find_element(By.ID, "service").send_keys("Housing")
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "email").send_keys("john@example.com")
    # Submit form
    driver.find_element(By.ID, "submitBtn").click()

    time.sleep(2)  # wait for confirmation

    # Validate confirmation message (assume element id = confirmation)
    confirmation_text = driver.find_element(By.ID, "confirmation").text
    assert "Application submitted" in confirmation_text
    print("Service Application Test: PASSED")

except Exception as e:
    print("Service Application Test: FAILED", e)

# Close browser
driver.quit()
