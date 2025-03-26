from selenium.webdriver.common.by import By


class SignUp_Page_Class:

    Link_SignUp_XPATH = "//a[normalize-space()='Sign Up']"
    Text_Username_XPATH = "//input[@id='username']"
    Text_Password_XPATH = "//input[@id='password']"
    Text_Email_XPATH = "//input[@id='email']"
    Text_Phone_XPATH = "//input[@id='phone']"
    Click_CreateUser_Button_XPATH = "//button[@type='submit']"
    Validate_Success_Message_XPATH = "//div[@id='successMessage']"


    def __init__(self, driver):
        self.driver = driver

    def Click_SignUp_Link(self):
        self.driver.find_element(By.XPATH, self.Link_SignUp_XPATH).click()

    def Enter_Username(self, username):
        self.driver.find_element(By.XPATH, self.Text_Username_XPATH).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(By.XPATH, self.Text_Password_XPATH).send_keys(password)

    def Enter_Email(self, email):
        self.driver.find_element(By.XPATH, self.Text_Email_XPATH).send_keys(email)

    def Enter_PhoneNumber(self, phoneNo):
        self.driver.find_element(By.XPATH, self.Text_Phone_XPATH).send_keys(phoneNo)

    def Click_CreateUser_Button(self):
        self.driver.find_element(By.XPATH, self.Click_CreateUser_Button_XPATH).click()

    def Validate_UserCreation(self):
        try:
            success_msg = self.driver.find_element(By.XPATH, self.Validate_Success_Message_XPATH).text
            return success_msg      # User created successfully
        except:
            pass
