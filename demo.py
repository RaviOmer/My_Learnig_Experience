First step to automate a chrome browser by Selenium with Pycharm :------

from selenium import webdriver
import os

driverlocation = "C:\\Users\\Ravi\\PycharmProjects\\chromedriver.exe"

os.environ["webdriver.chrome.driver"] = driverlocation

driver = webdriver.Chrome(driverlocation)
driver.get("https://letskodeit.teachable.com/p/practice")
Searchbyclass = driver.find_element_by_css_selector("#bmwradio")
searchbycs = driver.find_element_by_xpath("//input[@id='bmwradio']")
searchby = driver.find_element_by_id("opentab")

if Searchbyclass is not None:
    print("Successful")
if searchbycs is not None:
    print('You code it bro')
if searchby is not None:
    print("You are on the right way of learning")
driver.close()
print()
print('THE END')

