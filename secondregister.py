from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from csv import reader
from selenium.webdriver.support.ui import Select
import random


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("http://automationpractice.com/")
driver.maximize_window()


with open('secondregister.csv') as csvfile:
    csvreader = reader(csvfile, delimiter=',')
    for row in csvreader:

        assert driver.find_element_by_class_name("login").is_displayed()
        driver.find_element_by_class_name("login").click()

        driver.find_element_by_id("email_create").send_keys(str(random.randint(0,1000000))+row[0])

        driver.find_element_by_id("SubmitCreate").click()

        assert driver.title == "Login - My Store"

        driver.find_element_by_id("id_gender1").click()

        driver.find_element_by_id("customer_firstname").send_keys(row[1])

        driver.find_element_by_id("customer_lastname").send_keys(row[2])

        driver.find_element_by_id("passwd").send_keys(row[3])

        select = Select(driver.find_element_by_id("days"))
        select.select_by_value(row[4])

        select = Select(driver.find_element_by_id("months"))
        select.select_by_value(row[5])

        select = Select(driver.find_element_by_id("years"))
        select.select_by_value(row[6])

        driver.find_element_by_id("newsletter").click()

        driver.find_element_by_id("optin").click()

        driver.find_element_by_id("address1").send_keys(row[7])

        driver.find_element_by_id("city").send_keys(row[8])

        select = Select(driver.find_element_by_id("id_state"))
        select.select_by_visible_text(row[9])

        driver.find_element_by_id("postcode").send_keys(row[10])

        driver.find_element_by_id("phone_mobile").send_keys(row[11])

        driver.find_element_by_id("submitAccount").click()

        assert driver.title == "My account - My Store"

        driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div/nav/div[2]/a").click()

driver.quit()
        
        

       

        
