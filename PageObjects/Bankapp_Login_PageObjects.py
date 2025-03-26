from selenium.webdriver.common.by import By


class Login_Page_Class:

    Link_Login_XPATH = "//a[normalize-space()='Login']"
    Text_Username_XPATH = "//input[@id='username']"
    Text_Password_XPATH = "//input[@id='password']"
    Click_Login_Button_XPATH = "//button[normalize-space()='Login']"
    Validate_UserLogin_XPATH = "//h2[normalize-space()='Dashboard']"    # Dashboard


    def __init__(self, driver):
        self.driver = driver

    def Click_Login_Link(self):
        self.driver.find_element(By.XPATH, self.Link_Login_XPATH).click()

    def Enter_Username(self, username):
        self.driver.find_element(By.XPATH, self.Text_Username_XPATH).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(By.XPATH, self.Text_Password_XPATH).send_keys(password)

    def Click_Login_Button(self):
        self.driver.find_element(By.XPATH, self.Click_Login_Button_XPATH).click()

    def Validating_UserLogin(self):
        try:
            success_Msg = self.driver.find_element(By.XPATH, self.Validate_UserLogin_XPATH).text
            return success_Msg
        except:
            pass


