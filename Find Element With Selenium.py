Basic Steps to Find Element In a web page with Selenium, Pycharm and ChromeDriver
------------------------------------------------------------------------------------
from selenium import webdriver
import os

driverlocation = "C:\\Location\\chromedriver.exe"

os.environ["webdriver.chrome.driver"] = driverlocation

driver = webdriver.Chrome(driverlocation)
driver.get("https://letskodeit.teachable.com/p/practice")

Searchbycss = driver.find_element_by_css_selector("#bmwradio")
searchbyxpath = driver.find_element_by_xpath("//input[@id='bmwradio']")
searchbyid = driver.find_element_by_id("opentab")
searchbylink = driver.find_element_by_link_text("Login")
searchbypartial = driver.find_element_by_partial_link_text("Pra")
searchbyclassname = driver.find_element_by_class_name("btn-style")
searchbyclassname.send_keys("hi")
searchbytagname = driver.find_element_by_tag_name("div")

text = searchbytagname.text
text1 = searchbyxpath.text


if Searchbycss is not None:
    print("Successful")
if searchbyxpath is not None:
    print('You code it bro:- ', text1)
if searchbyid is not None:
    print("You are on the right way of learning.")
if searchbylink is not None:
    print("YUoOOOOP")
if searchbypartial is not None:
    print("YEsssssssssssssss We got It")
if searchbyclassname is not None:
    print("QQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
print()
if searchbytagname is not None:
    print("Yuuuuuuupppppp :", text)

driver.close()
print()
print('THE END')
