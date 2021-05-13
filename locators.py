from selenium.webdriver.common.by import By

locator = {
    "Registration":(By.CSS_SELECTOR,"#toggleNav > li:nth-child(6) > a"),
    "name":(By.CSS_SELECTOR,"#load_form > fieldset:nth-child(5) > input[type=text]"),
    "phone":(By.CSS_SELECTOR,"#load_form > fieldset:nth-child(6) > input[type=tel]"),
    "email":(By.CSS_SELECTOR,"#load_form > fieldset:nth-child(7) > input[type=email]"),
    "country":(By.CSS_SELECTOR,"#load_form > fieldset:nth-child(8) > select"),
    "city":(By.CSS_SELECTOR,"#load_form > fieldset:nth-child(9) > input[type=text]"),
    "username":(By.CSS_SELECTOR,"#load_form > fieldset:nth-child(10) > input[type=text]"),
    "password":(By.CSS_SELECTOR,"#load_form > fieldset:nth-child(11) > input[type=password]"),
    "submit_Button":(By.CLASS_NAME,"button")

}
