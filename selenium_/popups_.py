from selenium import webdriver
import time
path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(path)
## Javascript alerts
"""
url = "https://demowebshop.tricentis.com/"
driver.get(url)
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath("//input[@value='Search']").click()
alert_obj = driver.switch_to.alert
print(alert_obj.text)
time.sleep(2)
alert_obj.accept()
"""

url1 = "file:///C:/Users/User/OneDrive/Desktop/selenium_/demo%20(1).html"
driver.get(url1)
driver.maximize_window()
time.sleep(2)

"""
driver.find_element_by_xpath("//button[text()='Delete']").click()
time.sleep(2)
alert_obj = driver.switch_to.alert
#alert_obj.dismiss()
alert_obj.accept()
"""

## file upload pop ups
path = r"C:\Users\User\Downloads\Suhasini.resume.docx"
time.sleep(2)
driver.find_element_by_xpath("//input[@type='file']").send_keys(path)
time.sleep(2)








