# there are 3 ways we can pass driver control to frame
# 1. driver.switch_to.frame("name_value/id_value")
#2.driver.switch_to.frame(Index)
#3 driver.switch_to.frame(wedelementt object)
# in order to give the control back to the main page
#1. driver.switch_to.parent_frame()
#2.driver.switch_to.default_content()


from selenium import webdriver
import time
path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(path)
url = "file:///C:/Users/User/OneDrive/Desktop/selenium_/iframe%20(1).html"
driver.get(url)
driver.maximize_window()

# switching using name attribute
#driver.switch_to.frame("frame1")
#switching using id attribute
#driver.switch_to.frame("FR1")
#switching using index
#driver.switch_to.frame(0)
#switching using webelement
frame_ele = driver.find_element_by_xpath("//iframe[@name='frame1']")
driver.switch_to.frame(frame_ele)
driver.find_element_by_id("small-searchterms").send_keys("books")
time.sleep(2)
# Before switchging to the frame2 or anyother frame take the control back to parent
# and than switch

# to switch back the control to parent or main frame

driver.switch_to.default_content()

# switching to 2nd frame
driver.switch_to.frame("FR2")
time.sleep(2)
driver.find_element_by_id("search_form").send_keys("abc")