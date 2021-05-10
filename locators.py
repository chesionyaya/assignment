from selenium.webdriver.common.by import By
locator={
    "login_link": (By.CLASS_NAME, "1v1-0 sign-in btn btn-white-outline open"),
    "username":(By.id,"inputEmail"),
    "password":(By.id,"inputPassword"),
    "Login_button":(By.id,"login"),
    "Register_button":(By.XPATH,'//*[@id="header"]/div/ul/li[3]/a'),
    "fristname"(By.id,"inputFirstName"),
    "lastname"(By.id,"inputLastName"),
    "email"(By.id,"inputEmail"),
    "phonenumber"(By.id,"inputPhone"),
    "companyname"(By.id,"inputCompanyName"),
    "address1"(By.id,"inputAddress1"),
    "address2"(By.id,"inputAddress2"),
    "city"(By.id,"inputCity"),
    "state"(By.id,"stateinput"),
    "postcode"(By.id,"inputPostcode"),
    "country"(By.id,"inputCountry"),
    "customfield[1]"(By.id,("customfield1"),
    "customfield[2]"(By.id,("customfield2"),
    "password"(By.id,("inputNewpassword1"),
    "password"(By.id,("inputNewPassword2"),
    "Logout_button"(By.CLASS_NAME,("btn"),
                      
                    
    
    }
