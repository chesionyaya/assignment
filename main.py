from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from locators import locator
from csv import reader
from selenium.webdriver.support.ui import Select
import random

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://phptravels.com/demo/")
driver.maximize_window()

with open('login.csv') as csvfile:
    csvreader = reader(csvfile, delimiter=',')
    for row in csvreader:

     assert driver.find_element(*locator["login_link"]).is_displayed
        driver.find_element(*locator["login_link"]).click()
        driver.find_element(*locator["username"]).send_keys(row[1])
        driver.find_element(*locator["password"]).send_keys(row[2])
        driver.find_element(*locator["login_button"]).click()
 with open('register.csv') as csvfile:
    csvreader = reader(csvfile, delimiter=',')
    for row in csvreader:                 
       assert driver.find_element(*locator["Register_button"]).click()
        driver.find_element(*locator["firstname"]).send_keys(row[1])
        driver.find_element(*locator["lastname"]).send_keys(row[2])
        driver.find_element(*locator["email"]).send_keys(str(random.randint(0,1000000))+row[0])
        driver.find_element(*locator["phonenumber"]).send_keys(row[4])
        driver.find_element(*locator["companynumber"]).send_keys(row[5])
        driver.find_element(*locator["address1"]).send_keys(row[6])
        driver.find_element(*lcoator["address2"]).send_keys(row[7])
        driver.find_element(*lcoator["city"]).send_keys(row[8])
        driver.find_element(*lcoator["state"]).send_keys(row[9])
        driver.find_element(*lcoator["postcode"]).send_keys(row[10])
        driver.find_element(*lcoator["country"]).send_keys(row[11])
        driver.find_element(*lcoator["customfield[1]"]).send_keys(row[12])
        driver.find_element(*lcoator["customfield[2]"]).send_keys(row[13])
        driver.find_element(*lcoator["password"]).send_keys(row[14])
        driver.find_element(*lcoator["password"]).send_keys(row[15])
        driver.find_element(*lcoator["Logout_button"]).click()
driver.quit()
