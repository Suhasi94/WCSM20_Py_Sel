# explicit wait

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(path)

"""
url1 = "file:///C:/Users/User/OneDrive/Desktop/selenium_/progressbar%20(1).html"
driver.get(url1)
driver.maximize_window()
driver.find_element_by_xpath('//button[text()="Click Me"]').click()
wait_obj = WebDriverWait(driver,30)
wait_obj.until(EC.presence_of_element_located(("xpath",'//div[text()="100%"]')))
driver.find_element_by_xpath('//button[text()="Click Me"]').click()

"""


# create a function that checks for both visibility as well as enability

url = "file:///C:/Users/User/OneDrive/Desktop/selenium_/demo%20(1).html"
driver.get(url)
driver.maximize_window()
ele = driver.find_element_by_id("first_name")
print(ele.is_enabled())
print(ele.is_displayed())









