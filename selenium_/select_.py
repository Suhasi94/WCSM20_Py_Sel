"""
Select
1. all the list box related methods are implemented inside the class "Select"
3 different methods available
1. select_by_visible_text
2.select_by_index
3.select_by_value

"""
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(path)
url = "file:///C:/Users/User/OneDrive/Desktop/selenium_/demo%20(1).html"
driver.get(url)
driver.maximize_window()

#locating the standard listbox using xpath and id
#element = driver.find_element_by_xpath('//select[@id="standard_cars"]')
#select_obj = Select(element)
#select_obj.select_by_visible_text("Audi")
#select_obj.select_by_visible_text("BMW")
#time.sleep(2)
#select_obj.select_by_value("jgr")
#time.sleep(2)
#select_obj.select_by_value("lr")
#time.sleep(2)

#select by index
#select_obj.select_by_index(1)

#print(select_obj.is_multiple)


# all the options in select tag
#all_options = select_obj.options
#print(all_options)
#for option in all_options:
    #var = option.text
    #select_obj.select_by_visible_text(var)

#for index in range(len(all_options)):
    #select_obj.select_by_index(index)

#for index,element in enumerate(all_options):
    #select_obj.select_by_index(index)


## multiselect list box

mul_ele = driver.find_element_by_id("multiple_cars")
s_obj = Select(mul_ele)

#select by visible text
s_obj.select_by_visible_text("Jaguar")
time.sleep(2)
s_obj.select_by_value("bmw")
time.sleep(2)
s_obj.select_by_index(3)
s_obj.select_by_index(4)
s_obj.select_by_index(1)
print(s_obj.is_multiple)

all_options = s_obj.options
print(all_options)
selected_options = s_obj.all_selected_options
for option in selected_options:
    print(option.text)

f_sel_option = s_obj.first_selected_option
print(f_sel_option.text)

# Deselect
#1. deselect_by_visible_text, 2 deslect_by_value 3. deselect_by_index, 4.deselect_all
s_obj.deselect_by_visible_text("Jaguar")
time.sleep(2)
s_obj.deselect_by_value("bmw")
time.sleep(2)
s_obj.deselect_by_index(1)
time.sleep(2)

s_obj.deselect_all()