
from selenium.webdriver.common.by import By

def test_valid_login(driver):
    driver.get("file:///C:/Users/Bruger/CitizenPortal_Demo/login.html")

    driver.find_element(By.ID, "username").send_keys("user1")
    driver.find_element(By.ID, "password").send_keys("Pass123")
    driver.find_element(By.ID, "loginBtn").click()

    assert "Welcome" in driver.page_source

def test_invalid_login(driver):
    driver.get("http://citizenportal.test/login")

    driver.find_element(By.ID, "username").send_keys("user1")
    driver.find_element(By.ID, "password").send_keys("WrongPass")
    driver.find_element(By.ID, "loginBtn").click()

    assert "Invalid username or password" in driver.page_source
