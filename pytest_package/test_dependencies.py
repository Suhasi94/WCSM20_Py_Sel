# pip install pytest-dependency

import pytest
from selenium import webdriver
path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://demo.actitime.com/login.do")
driver.maximize_window()
driver.implicitly_wait(30)

@pytest.mark.dependency()
def test_login():
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_name("pwd").send_keys("manager")
    driver.find_element_by_xpath("//div[text()='Login ']").click()


@pytest.mark.dependency(depends=["test_login"])
def test_logout():
    driver.find_element_by_id("logoutLink").click()

