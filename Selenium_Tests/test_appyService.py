from selenium.webdriver.common.by import By

def test_apply_service(driver):
    driver.get("file:///C:/Users/Bruger/CitizenPortal_Demo/applyService.html")

    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "serviceType").send_keys("Passport Renewal")
    driver.find_element(By.ID, "submitBtn").click()

    assert "Application submitted successfully" in driver.page_source

