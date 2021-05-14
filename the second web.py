from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from csv import reader
from selenium.webdriver.support.ui import Select
import random

driver = webdriver.Chrome(ChromeDriverManager().install())


with open('login.csv') as csvfile:
    csvreader = reader(csvfile, delimiter=',')
    for row in csvreader:

        driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        driver.maximize_window()

        assert driver.title == "Login - My Store"

        driver.find_element_by_id("email").send_keys(row[0])

        driver.find_element_by_id("passwd").send_keys(row[1])

        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div/div/div[2]/form/div/p[2]/button/span").click()

        assert driver.title == "My account - My Store"

        driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/div/div/nav/div[2]/a").click()

        driver.find_element_by_id("search_query_top").click()


        assert driver.title == "My account - My Store"



driver.quit()

       

       
        
        
