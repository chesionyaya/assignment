from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from csv import reader
from selenium.webdriver.support.ui import Select
import random

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
driver.maximize_window()

driver.find_element_by_id("email").send_keys("123@qq.com")

driver.find_element_by_id("passwd").send_keys("12345")

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div/div/div[2]/form/div/p[2]/button/span").click()

driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div[2]/ul/li/a/span").click()

with open('mywishlists.csv') as csvfile:
    csvreader = reader(csvfile, delimiter=',')
    for row in csvreader:

        driver.find_element_by_css_selector("#name").send_keys(row[0])
 
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[2]/div/form/fieldset/p/button/span").click()

        assert driver.title == "My Store"




