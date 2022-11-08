# locators
# 1. id
# 2. name
# 3. class name
# 4. tag name
# 5. link text
# 6.partial link text
# 7. Css selector
# 8.xpath


# find_element - it is a method which help in locating ur web element
####locating thr element using id locator
# search_bar = driver.find_element_by_id("small-searchterms").send_keys("books")
## locating the ele using id

from selenium import webdriver
import time
path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver_obj = webdriver.Chrome(path)
url = "https://demowebshop.tricentis.com/"
driver_obj.get(url)
driver_obj.maximize_window()
time.sleep(2)
"""
web_ele_variable = driver_obj.find_element_by_id("small-searchterms")
print(web_ele)
web_ele_variable.click()
web_ele_variable.send_keys("books")
"""

#locating using name
#driver_obj.find_element_by_name("q").send_keys("books") # search bar

#locating using class name
#driver_obj.find_element_by_class_name("ico-register").click()


#locating using link text

#driver_obj.find_element_by_link_text("Register").click()

# locating using partial link text
#driver_obj.find_element_by_partial_link_text("Reg").click()
#time.sleep(1)
# registering using id,name locator
"""
driver_obj.find_element_by_id("gender-female").click()
time.sleep(1)
driver_obj.find_element_by_name("FirstName").send_keys("suhasi")
time.sleep(1)
driver_obj.find_element_by_name("LastName").send_keys("k")
time.sleep(1)
driver_obj.find_element_by_id("Email").send_keys("suhasi7330@gmail.com")
time.sleep(1)
driver_obj.find_element_by_name("Password").send_keys("Su@12345")
time.sleep(1)
driver_obj.find_element_by_name("ConfirmPassword").send_keys("Su@12345")
time.sleep(1)
driver_obj.find_element_by_id("register-button").click()
time.sleep(1)

"""

#driver_obj.find_element_by_link_text("Log in").click()

### 1. CSS Selector - syntax --- tagname[attributname=attributevalue]

#driver_obj.find_element_by_css_selector('input[id=Email]').send_keys("suhasi7330@gmail.com")
#driver_obj.find_element_by_css_selector("input[type=password]").send_keys("Su@12345")
#driver_obj.find_element_by_css_selector('input[value="Log in"]').click()

##### 2. css selector , tag and ID syntax tagname#idvalue
##### 3. css selector , tag and class syntax tagname.classnamevalue


#driver_obj.find_element_by_css_selector("input#small-searchterms").send_keys("books")
#driver_obj.find_element_by_css_selector("a.ico-register").click()


"""
Drawbacks of css selector:

1. if the attributes are not present,then it is difficult to write css selector expression
2. css selector does not have text attribute (no elements can be located using its text in css selector )
3. indexing is not supported in css selector

# xpath
xpath is defined as xml path, it is a syntax or language for finding
any element on the webpage using xml path expression

1. Absolute xpath - full path - starts from the root till the destination - /
2. Relative xpath - 1. syntax using attribute - //tagname[@attributename='attributrevalue']

/ - immediate child
// - any child
     if you text, even if the attributes are there or not there u can write xpath -
    2. syntxt using text  - //tagname[text()="text"]

driver_obj.find_element_by_xpath('//a[text()="Register"]').click()
time.sleep(2)
driver_obj.find_element_by_xpath('//a[@class="ico-login"]').click()

"""

###   Xpath - 2 methods, contains(),index()

 #  syntax 3 using contains
# 1. attribute -->  //tagname[contains(@attributename,attributevalue)  #remember "attr_value"
# 2. text --> //tagname[contains(text(),attributevalue)]

 # index - Group indexing
 #  (//tagname[contains(@attributename,attributevalue)])[index_number]

"""
#driver_obj.find_element_by_xpath('//a[text()="Register"]').click()
for i in range(1,6):
    driver_obj.find_element_by_xpath(f'(//a[contains(@class,"ico")])[{i}]').click()
    time.sleep(2)
"""









