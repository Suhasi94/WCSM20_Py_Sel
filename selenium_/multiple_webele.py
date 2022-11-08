from selenium import webdriver
import time
path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(path)
url = "https://demowebshop.tricentis.com/"
url1 = "file:///C:/Users/User/OneDrive/Desktop/selenium_/demo%20(1).html"
driver.get(url1)
time.sleep(2)
driver.maximize_window()
#web_ele_list = driver.find_elements_by_xpath('//div[@class="block block-category-navigation"]//a')
#print(web_ele_list)
#for web_ele in web_ele_list:
    #print(web_ele.text) # text of the webelement
    #web_ele.click()
    #driver.back() # you need to go back to category box bcz it will be in book page after the 1st click
#web_elements = driver.find_elements_by_xpath("//div[@class='footer-menu-wrapper']//a")
#for web_element in web_elements:
    #print(web_element.text)
"""


web_elems = driver.find_elements_by_xpath('//input[@name="download"]')
for web_ele in web_elems:
    web_ele.click()
    time.sleep(2)
    
1.count the number of input tags in demo.html
2.print all the link texts present in the webpage

"""


res = driver.find_elements_by_tag_name("input")
print(len(res))

links = driver.find_elements_by_tag_name("a")
for link in links:
    print(link.text)
driver.close()

