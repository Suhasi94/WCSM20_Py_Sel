# 3 entities -- data - excel sheet,pom - main logic i.e, the AUT script,
#  library- generic code which will be interconnected with pom,(test_,conftest.py)
#from selenium import webdriver
from Data import reading_objects


#path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
#driver = webdriver.Chrome(path)
#driver.get("https://demo.actitime.com/login.do")
#driver.maximize_window()

login_objects = reading_objects.read_locators()
#print(login_objects)

class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    def enter_username(self):
        #driver.find_element("id","username").send_keys("admin")
        self.driver.find_element(*login_objects["txt_username"]).send_keys("admin")


    def enter_pwd(self):
        #driver.find_element("name","pwd").send_keys("manager")
        self.driver.find_element(*login_objects["txt_password"]).send_keys("manager")


    def click_login(self):
        #driver.find_element("xpath", "//div[text()='Login ']").click()
        self.driver.find_element(*login_objects["btn_login"]).click()

#lp = LoginPage()
#lp.enter_username()
#lp.enter_pwd()
#lp.click_login()