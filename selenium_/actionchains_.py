from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(path)
url = "https://www.meesho.com/"
driver.get(url)
driver.maximize_window()
ac_obj = ActionChains(driver)

# driver.refresh()
ac_obj.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(1)
ac_obj.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(2)
ac_obj.send_keys(Keys.PAGE_UP).perform()
time.sleep(2)

kids_wear = driver.find_element_by_xpath("//span[text()='Kids']")
time.sleep(2)
ac_obj.move_to_element(kids_wear).perform()

time.sleep(2)
#women_ethnic = driver.find_element_by_xpath("//span[text()='Women Ethnic']")
#ac_obj.move_to_element(women_ethnic).perform()
#time.sleep(2)

#Double clicking
"""

url = "file:///C:/Users/User/OneDrive/Desktop/selenium_/demo%20(1).html"
driver.get(url)
driver.maximize_window()
# creating an instance for ActionChains Class
ac_obj = ActionChains(driver)
time.sleep(2)
button = driver.find_element_by_xpath("//button[@id='double-click']")
time.sleep(2)
ac_obj.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(2)
ac_obj.double_click(button).perform()
time.sleep(2)
ac_obj.send_keys(Keys.PAGE_UP).perform()
"""