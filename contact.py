from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from csv import reader
from selenium.webdriver.support.ui import Select
import random
import time

driver = webdriver.Chrome(ChromeDriverManager().install())


with open('contact.csv') as csvfile:
    csvreader = reader(csvfile, delimiter=',')
    for row in csvreader:

        driver.get("http://automationpractice.com/index.php?controller=contact")
        driver.maximize_window()


        assert driver.title == "Contact us - My Store"

        ele_select = driver.find_element_by_id("id_contact")

        Select(ele_select).select_by_value("2")

        driver.find_element_by_css_selector("#email").send_keys(row[1])

        driver.find_element_by_id("id_order").send_keys(row[2])

        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div/form/fieldset/div[1]/div[2]/div/textarea").send_keys(row[3])

        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div/form/fieldset/div[2]/button/span").click()

        assert driver.title ==  "Contact us - My Store"
