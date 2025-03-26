import allure
from allure_commons.types import AttachmentType

from PageObjects.Bankapp_CreateUser_PageObjects import SignUp_Page_Class
from PageObjects.Bankapp_Login_PageObjects import Login_Page_Class
from Utilities.logger import Log_Class
from Utilities.readProperties import ReadConfig


class Test_UserProfile:

    Login_Username = ReadConfig.GetUsername()
    Login_Password = ReadConfig.GetPassword()
    log = Log_Class.loggen()

    @allure.title("Bankapp Verify URL Test Case")
    def test_Verify_URL_001(self, setup):
        self.log.info("'test_Verify_URL_001' test case started")
        self.log.info("Opening browser")
        self.log.info("Maximizing window")
        self.log.info("Launching URL")
        self.driver = setup
        self.log.info("Validating URL launch on correct page or not")
        if self.driver.title == "Bank Application":
            self.log.info("URL launched on correct page")
            # Capturing Screenshot
            self.log.info("Capturing Screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_Verify_URL_001_Pass.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Verify_URL_001_Pass", attachment_type=AttachmentType.PNG)
            self.log.info("'test_Verify_URL_001' is passed")
            assert True
        else:
            self.log.info("URL launched on different page")
            self.log.info("Capturing Screenshot for failure")
            # Capturing Screenshot
            self.driver.save_screenshot(".\\Screenshots\\test_Verify_URL_001_Fail.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Verify_URL_001_Fail", attachment_type=AttachmentType.PNG)
            self.log.info("'test_Verify_URL_001' is failed\n")
            assert False
        self.log.info("'test_Verify_URL_001' is completed\n")

    @allure.title("Bankapp Create User Test Case")
    def test_CreateUser_002(self, setup):
        self.log.info("'test_CreateUser_002' test case is started")
        self.log.info("Opening browser")
        self.log.info("Launching URL")
        self.log.info("Maximizing window")
        self.driver = setup

        self.cu = SignUp_Page_Class(self.driver)
        self.cu.Click_SignUp_Link()
        self.log.info("Click on Sign Up link")

        Username = GenerateUsername()
        self.cu.Enter_Username(Username)
        self.log.info(f"Entering Username: {Username}")

        Password = GeneratePassword()
        self.cu.Enter_Password(Password)
        self.log.info(f"Entering Password: {Password}")

        # Email = GenerateEmail()
        self.cu.Enter_Email(Username+'@credence.in')
        self.log.info(f"Entering Email: {Username+'@credence.in'}")

        PhoneNo = GeneratePhone()
        self.cu.Enter_PhoneNumber(PhoneNo)
        self.log.info(f"Entering Phone Number: {PhoneNo}")
        self.cu.Click_CreateUser_Button()
        self.log.info("Click on create user button")
        self.log.info("Validating User Created or not")
        if self.cu.Validate_UserCreation() == "User created successfully":
            self.log.info("User created")
            # Capturing Screenshot
            self.log.info("Capturing Screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_CreateUser_002_Pass.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_CreateUser_002_Pass", attachment_type=AttachmentType.PNG)

            self.log.info("'test_CreateUser_002' is passed")
            assert True
        else:
            self.log.info("User not created")
            # Capturing Screenshot
            self.log.info("Capturing Screenshot for failure")
            self.driver.save_screenshot(".\\Screenshots\\test_CreateUser_002_Fail.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_CreateUser_002_Fail", attachment_type=AttachmentType.PNG)
            self.log.info("'test_CreateUser_002' is failed\n")
            assert False
        self.log.info("'test_CreateUser_002' is completed\n")


    @allure.title("Bankapp User Login Test Case")
    def test_UserLogin_003(self, setup):
        self.log.info("'test_UserLogin_003' test case started")
        self.log.info("Opening browser")
        self.log.info("Maximizing window")
        self.log.info("Launching URL")
        self.driver = setup

        self.lp = Login_Page_Class(self.driver)
        self.lp.Click_Login_Link()
        self.log.info("Click on login link")
        self.lp.Enter_Username(self.Login_Username)
        self.log.info(f"Enter Username:- {self.Login_Username}")
        self.lp.Enter_Password(self.Login_Password)
        self.log.info(f"Enter Password: {self.Login_Password}")
        self.lp.Click_Login_Button()
        self.log.info("Click on login button")
        self.log.info("Validating User login")
        if self.lp.Validating_UserLogin() == "Dashboard":
            self.log.info("User logged in")
            # Capturing Screenshot
            self.log.info("Capturing Screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_UserLogin_003_Pass.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_UserLogin_003_Pass", attachment_type=AttachmentType.PNG)
            self.log.info("'test_UserLogin_003' is passed")
            assert True
        else:
            self.log.info("User not logged in")
            # Capturing Screenshot
            self.log.info("Capturing Screenshot for failure")
            self.driver.save_screenshot(".\\Screenshots\\test_UserLogin_003_Fail.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_UserLogin_003_Fail", attachment_type=AttachmentType.PNG)
            self.log.info("'test_UserLogin_003' is Failed\n")
            assert False
        self.log.info("'test_UserLogin_003' is completed\n")






# Random data for Create User ie. test_CreateUser_002
import random
import string

def GenerateUsername(length=4):
    Username = 'User' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return Username

def GeneratePassword(end='@101'):
    Password = "User" + end
    return Password

def GenerateEmail(domain='credence.in'):
    Email = GenerateUsername() + '@' + domain
    return Email

def GeneratePhone(length=10):
    Phone_Number = ''.join(random.choices(string.digits, k=length))
    return Phone_Number
