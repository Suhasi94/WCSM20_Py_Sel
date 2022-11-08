from selenium import webdriver
import pytest
import time

@pytest.fixture()
def fixture():
    driver = webdriver.Chrome(r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe")
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    yield driver
    print(driver.title)
    driver.save_screenshot("test_fixture_ex.png")
    driver.quit()
