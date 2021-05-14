from selenium.webdriver.common.by import By

locator = {
    "Registration":(By.CSS_SELECTOR,"#toggleNav > li:nth-child(6) > a"),
    "name": (By.XPATH, "/html/body/div[4]/div/div/div/div/div/form/fieldset[1]/input"),
    "phone":(By.CSS_SELECTOR,"#load_form > fieldset:nth-child(6) > input[type=tel]"),
    "email":(By.CSS_SELECTOR,"#load_form > fieldset:nth-child(7) > input[type=email]"),
    "country":(By.CSS_SELECTOR,"#load_form > fieldset:nth-child(8) > select"),
    "city":(By.CSS_SELECTOR,"#load_form > fieldset:nth-child(9) > input[type=text]"),
    "username":(By.CSS_SELECTOR,"#load_form > fieldset:nth-child(10) > input[type=text]"),
    "password":(By.CSS_SELECTOR,"#load_form > fieldset:nth-child(11) > input[type=password]"),
    "submit_Button": (By.CSS_SELECTOR, "#load_form > div:nth-child(12) > div.span_1_of_4 > input"),
    "Signin_link":(By.XPATH,"/html/body/div[4]/div/div/div/div/div/form/div[1]/div[1]/p/a"),
    "Username_login":(By.XPATH,"/html/body/div[4]/div/div/div/div/div/form/fieldset[1]/input"),
    "Password_login":(By.XPATH,"/html/body/div[4]/div/div/div/div/div/form/fieldset[2]/input"),
    "Submit_button":(By.CSS_SELECTOR,"#load_form > div:nth-child(7) > div.span_1_of_4 > input"),

}

