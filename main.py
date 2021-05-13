from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from locators import locator
from csv import reader
from selenium.webdriver.support.ui import Select
import random

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("http://www.way2automation.com/demo.html")
driver.maximize_window()

with open('data.csv') as csvfile:
    csvreader = reader(csvfile, delimiter=',')
    for row in csvreader:
        assert driver.find_element(*locator["Registration"]).is_displayed()
        driver.find_element(*locator["Registration"]).click()

        assert driver.title == "Welcome"

        driver.find_element(*locator["name"]).send_keys(row[0])

        driver.find_element(*locator["phone"]).send_keys(row[1])

        driver.find_element(*locator["email"]).send_keys(str(random.randint(0,1000000))+row[2])

        select = Select(driver.find_element(*locator["country"]))
        select.select_by_value(row[3])

        driver.find_element(*locator["city"]).send_keys(row[4])

        driver.find_element(*locator["username"]).send_keys(row[5])

        driver.find_element(*locator["password"]).send_keys(row[6])

        driver.find_element(*locator["submit_Button"]).click()

driver.quit()
        
