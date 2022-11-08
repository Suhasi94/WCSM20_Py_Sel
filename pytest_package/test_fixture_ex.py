#from selenium import webdriver
#import time
#import pytest

#@pytest.fixture()
#def fixture():
#    driver = webdriver.Chrome(r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe")
#    driver.get("https://demowebshop.tricentis.com/")
#    driver.maximize_window()
#    yield driver
#    print(driver.title)
#   driver.quit()


def test_login(fixture):
    fixture.find_element_by_link_text("Log in").click()

def test_resgister(fixture):
    fixture.find_element_by_link_text("Register").click()


