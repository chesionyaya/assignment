from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from csv import reader
from selenium.webdriver.support.ui import Select
import random

driver = webdriver.Chrome(ChromeDriverManager().install())


with open('search.csv') as csvfile:
    csvreader = reader(csvfile, delimiter=',')
    for row in csvreader:

        driver.get("http://automationpractice.com/index.php")
        driver.maximize_window()

        assert driver.title == "My Store"

        driver.find_element_by_id("search_query_top").send_keys(row[0])

        driver.find_element_by_css_selector("#searchbox > button").click()

        assert driver.title == "Search - My Store"
        


        
        
