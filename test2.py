from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from locators import locator
from csv import reader
from selenium.webdriver.support.ui import Select
import random
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

with open('logindata.csv') as csvfile:
    csvreader = reader(csvfile, delimiter=',')
    for row in csvreader:

        driver.get("http://way2automation.com/way2auto_jquery/index.php")
        driver.maximize_window()

        assert driver.title == "Welcome to the Test Site"

        driver.find_element(*locator["Signin_link"]).click()

        assert driver.title == "Welcome to the Test Site"

        driver.find_element(*locator["Username_login"]).send_keys(row[0])

        driver.find_element(*locator["Password_login"]).send_keys(row[1])
  
        driver.find_element(*locator["Submit_button"]).click()

        time.sleep(1)

#driver.quit()

     

     
