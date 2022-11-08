from selenium import webdriver
import time
path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(path)
#to launch  google on chromebrowser
url = "https://www.google.com/"
driver.get(url)
#maximize and minimize the windom
driver.maximize_window()
time.sleep(2)
driver.minimize_window()
driver.maximize_window()
print(driver.title)
print(driver.current_url)
#driver.close()# close only the active webpage
#driver.quit() # close the entire browser
