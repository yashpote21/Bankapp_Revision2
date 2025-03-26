import allure
from allure_commons.types import AttachmentType

from PageObjects.Bankapp_Login_PageObjects import Login_Page_Class
from PageObjects.Bankapp_SearchUser_PageObjects import SearchUser_Class
from Utilities.logger import Log_Class
from Utilities.readProperties import ReadConfig


class Test_SearchUser_Class:
    Username = ReadConfig.GetUsername()
    Password = ReadConfig.GetPassword()
    Search_Username = ReadConfig.GetSearchUsername()

    log = Log_Class.loggen()

    def test_SearchUser_004(self, setup):
        self.log.info("'test_SearchUser_004' is started")
        self.log.info("Opening browser")
        self.log.info("Maximizing window")
        self.log.info("Launching URL")
        self.driver = setup

        self.lp = Login_Page_Class(self.driver)
        self.lp.Click_Login_Link()
        self.log.info("Click on login link")
        self.lp.Enter_Username(self.Username)
        self.log.info(f"Enter Username: {self.Username}")
        self.lp.Enter_Password(self.Password)
        self.log.info(f"Enter Password: {self.Password}")
        self.lp.Click_Login_Button()
        self.log.info("Click on login button")
        self.log.info("Validating User landed on correct page or not")
        if self.lp.Validating_UserLogin() == "Dashboard":
            self.log.info("User landed on correct page")
            assert True
        else:
            self.log.info("User landed on different page")
            assert False

        self.su = SearchUser_Class(self.driver)
        self.su.Click_UserManagement()
        self.log.info("Click on User Management link")
        self.su.Enter_Username(self.Search_Username)
        self.log.info(f"Enter Username: {self.Search_Username}")
        self.su.Click_SearchUser_Button()
        self.log.info("Click on Search User button")
        self.log.info("Validate user found or not")
        if self.su.Validate_UserSearch() == "Edit User":
            self.log.info("user found")
            # Capturing Screenshot
            self.log.info("Capturing Screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_SearchUser_004_Pass.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_SearchUser_004_Pass", attachment_type=AttachmentType.PNG)
            self.log.info("'test_SearchUser_004' is passed")
            assert True
        else:
            self.log.info("user not found")
            # Capturing Screenshot
            self.log.info("Capturing Screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_SearchUser_004_Fail.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_SearchUser_004_Fail", attachment_type=AttachmentType.PNG)
            self.log.info("'test_SearchUser_004' is failed\n")
            assert False
        self.log.info("'test_SearchUser_004' is completed\n")

