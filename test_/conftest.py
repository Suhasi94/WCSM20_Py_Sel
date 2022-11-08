# pip freeze >requirements.txt ---(to c all the pip install u have done for the project)
#cross browsing - pip install webdriver-manager


import pytest
from selenium import webdriver
#path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.options import Options
path1 = r"C:\Users\User\OneDrive\Desktop\driver_file\geckodriver.exe"


@pytest.fixture(params=["Chrome","Firefox","Edge"])
def _driver(request):
    if request.param == "Chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())

    elif request.param == "Firefox":
        option = Options()
        option.binary_location = r'c:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=path1,options=option)
        #driver = webdriver.Firefox(GeckoDriverManager().install(),option=options)

    elif request.param == "Edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())


    driver.get("https://demo.actitime.com/login.do")
    driver.maximize_window()
    yield driver