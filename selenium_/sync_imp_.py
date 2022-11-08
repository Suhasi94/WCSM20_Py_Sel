#Synchronization
#1.unconditional  - time.sleep(sec)
# 2. conditional - 1.implicit wait 2. explicit wait
# implicit wait - only once for entire instance drive
#               driver.implicitly_wait(30) - find_element ,find_elements
# explicit wait -
# import WebDriverWait
#            from selenium.weddriver.support.ui import WebDriverWait
# import Expected_Conditions
#         from selenium.webdriver.support import expected_conditions as EC


from selenium import webdriver
import time

path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(path)

"""
url = "file:///C:/Users/User/OneDrive/Desktop/selenium_/loading%20(1).html"
driver.get(url)
driver.maximize_window()
start = time.time()
driver.implicitly_wait(30)
driver.find_element_by_name("fname").send_keys("Suhasini")
end = time.time()
print(end-start)
"""
url1 = "file:///C:/Users/User/OneDrive/Desktop/selenium_/progressbar%20(1).html"
driver.get(url1)
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_xpath('//button[text()="Click Me"]').click()
driver.find_element_by_xpath('//div[text()="100%"]')
driver.find_element_by_xpath('//button[text()="Click Me"]').click()













