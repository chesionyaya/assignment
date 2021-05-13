from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from locators import locator
from csv import reader
from selenium.webdriver.support.ui import Select
import random

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

with open('data.csv') as csvfile:
    csvreader = reader(csvfile, delimiter=',')
    for row in csvreader:

        driver.get("http://way2automation.com/way2auto_jquery/index.php")
        driver.maximize_window()
        
        assert driver.title == "Welcome to the Test Site"

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
        
