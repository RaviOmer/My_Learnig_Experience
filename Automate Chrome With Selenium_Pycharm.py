First step to automate a chrome browser by Selenium with Pycharm :------

from selenium import webdriver
import os

driverlocation = "C:\\Location\\chromedriver.exe"

os.environ["webdriver.chrome.driver"] = driverlocation

driver = webdriver.Chrome(driverlocation)
driver.get("https://www.yahoo.com")

print()
print('THE END')

