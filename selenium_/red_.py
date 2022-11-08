import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.redbus.in/")
driver.implicitly_wait(30)
driver.find_element_by_xpath('//a[@id="rYde"]').click()
driver.find_element_by_xpath("(//div[text()='Hourly Rental'])[2]").click()
time.sleep(2)
driver.switch_to.frame(driver.find_element_by_xpath("//object"))
driver.find_element_by_xpath('//div[text()="Cab"]').click()
