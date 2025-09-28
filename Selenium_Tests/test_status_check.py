from selenium.webdriver.common.by import By

def test_check_status_valid(driver):
    driver.get("file:///C:/Users/Bruger/CitizenPortal_Demo/status.html")

    driver.find_element(By.ID, "applicationId").send_keys("12345")
    driver.find_element(By.ID, "checkBtn").click()

    assert "Pending" in driver.page_source or "Approved" in driver.page_source

def test_check_status_invalid(driver):
    driver.get("http://citizenportal.test/status")

    driver.find_element(By.ID, "applicationId").send_keys("invalidID")
    driver.find_element(By.ID, "checkBtn").click()

    assert "Application not found" in driver.page_source
