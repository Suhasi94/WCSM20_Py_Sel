"""
Steps for dynamic xpath/dependent - independent xpath
1. Identify dependent and independent elements
2. write locator expression for independent element
3. Traverse backward from the independent element until the root/common parent of both
independent and dependent element is located
4. write xpath expression  for  dependent element

"""
from selenium import webdriver
import time
path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(path)
url = "file:///C:/Users/User/OneDrive/Desktop/selenium_/demo%20(1).html"
driver.get(url)
time.sleep(2)
driver.maximize_window()
"""
driver.find_element_by_xpath('//td[text()="Ruby"]/..//input[@type="checkbox"]').click()
driver.find_element_by_xpath('//td[text()="Java"]/..//input[@type="checkbox"]').click()
driver.find_element_by_xpath('//td[text()="Perl"]/..//input[@type="checkbox"]').click()
driver.find_element_by_xpath('//td[text()="Python"]/..//input[@type="checkbox"]').click()
driver.find_element_by_xpath('//td[text()="C#"]/..//input[@type="checkbox"]').click()
driver.find_element_by_xpath('//td[text()="JavaScript"]/..//input[@type="checkbox"]').click()

languages = ["Ruby","Java","Perl","Python","C#","JavaScript"]
for lang in languages[::-1]:
    driver.find_element_by_xpath(f'//td[text()="{lang}"]/..//input[@type="checkbox"]').click()
    time.sleep(2)
    
"""
driver.find_element_by_xpath("//td[text()='AAPL']/..//td[@class='price']").click()
#url1 = "https://www.python.org/downloads/"
#driver.get(url1)
#time.sleep(2)
#driver.maximize_window()
#driver.find_element_by_xpath("//a[text()='Python 3.11.0']/../..//a[text()='Release Notes']").click()
