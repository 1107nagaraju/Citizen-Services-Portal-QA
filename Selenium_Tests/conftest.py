import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()   # assumes chromedriver is installed
    driver.maximize_window()
    yield driver
    driver.quit()
