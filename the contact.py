from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from csv import reader
from selenium.webdriver.support.ui import Select
import random

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)

with open('contact.csv') as csvfile:
    csvreader = reader(csvfile, delimiter=',')
    for row in csvreader:

        driver.get("http://automationpractice.com/index.php?controller=contact")
        driver.maximize_window()

        assert driver.title == "Contact us - My Store"

        select = Select(driver.find_element_id("id_contact"))
        select.select_by_value(row[0])

        driver.find_element_css_selector("#email").send_keys(row[0])

        driver.find_element_css_selector("#center_column > form > fieldset > div.clearfix > div.col-xs-12.col-md-3 > div:nth-child(6) > div > select").send_keys(row[0])

        driver.find_element_id("message").send_keys(row[0])
