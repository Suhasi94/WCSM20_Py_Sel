from selenium import webdriver
import time
path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(path)
url = "https://demowebshop.tricentis.com/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(30)
time.sleep(2)
driver.find_element_by_link_text("Twitter").click()
time.sleep(2)
handles =driver.window_handles
print(handles)
driver.switch_to.window(handles[1])
time.sleep(2)
driver.find_element_by_xpath('//span[text()="Follow"]').click()
driver.switch_to.window(handles[0])
time.sleep(2)
driver.find_element_by_link_text("Register").click()