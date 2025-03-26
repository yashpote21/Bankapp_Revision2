import allure
import pytest
from allure_commons.types import AttachmentType

from PageObjects.Bankapp_Login_PageObjects import Login_Page_Class
from PageObjects.Bankapp_SearchUser_PageObjects import SearchUser_Class
from Utilities import XLUtils
from Utilities.logger import Log_Class
from Utilities.readProperties import ReadConfig


class Test_SearchUser_Class:
    Username = ReadConfig.GetUsername()
    Password = ReadConfig.GetPassword()
    Search_Username = ReadConfig.GetSearchUsername()

    log = Log_Class.loggen()

    Excel_File_Path = "TestCases/TestData/Revision2_Excel_DDT.xlsx"


    @pytest.mark.skip(reason="Too much confusion while providing wrong data in excel test case failed, test case can't handle it")
    def test_SearchUser_Excel_DDT_006(self, setup):
        self.log.info("'test_SearchUser_Excel_DDT_006' is started")
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

        self.RowCount =XLUtils.RowCount(self.Excel_File_Path, 'Excel_SearchUser')
        print(f"Total number of rows:-> {self.RowCount}")


        for r in range(2, self.RowCount+1):
            self.Search_Username = XLUtils.ReadData(self.Excel_File_Path, 'Excel_SearchUser', r, 2)
            self.Expected_Result= XLUtils.ReadData(self.Excel_File_Path, 'Excel_SearchUser', r, 3)

            self.Username = self.Search_Username
            self.su.Enter_Username(self.Username)
            # self.log.info(f"Enter Username: {self.Username}")
            self.su.Click_SearchUser_Button()
            self.log.info("Click on Search User button")
            self.log.info("Validate user found or not")
            if self.su.Validate_UserSearch() == "Edit User" and self.Expected_Result == 'pass':
                User_Name =XLUtils.WriteData(self.Excel_File_Path, 'Excel_SearchUser', r, 4, 'pass')
                Status =XLUtils.WriteData(self.Excel_File_Path, 'Excel_SearchUser', r, 5, 'pass')

                self.log.info("user found")
                # Capturing Screenshot
                self.log.info("Capturing Screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_SearchUser_Excel_DDT_006_Pass.png")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_SearchUser_Excel_DDT_006_Pass", attachment_type=AttachmentType.PNG)
                self.log.info("'test_SearchUser_Excel_DDT_006' is passed")
                assert True
            elif self.su.Validate_UserSearch() == "Edit User" and self.Expected_Result == 'fail':
                User_Name =XLUtils.WriteData(self.Excel_File_Path, 'Excel_SearchUser', r, 4, 'pass')
                Status =XLUtils.WriteData(self.Excel_File_Path, 'Excel_SearchUser', r, 5, 'fail')

                self.log.info("user not found")
                # Capturing Screenshot
                self.log.info("Capturing Screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_SearchUser_Excel_DDT_006_Fail.png")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_SearchUser_Excel_DDT_006_Fail", attachment_type=AttachmentType.PNG)
                self.log.info("'test_SearchUser_Excel_DDT_006' is failed")
                assert False
            elif self.su.Validate_UserSearch() != "Edit User" and self.Expected_Result == 'pass':
                User_Name =XLUtils.WriteData(self.Excel_File_Path, 'Excel_SearchUser', r, 4, 'fail')
                Status =XLUtils.WriteData(self.Excel_File_Path, 'Excel_SearchUser', r, 5, 'fail')

                self.log.info("user not found")
                # Capturing Screenshot
                self.log.info("Capturing Screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_SearchUser_Excel_DDT_006_Fail.png")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_SearchUser_Excel_DDT_006_Fail", attachment_type=AttachmentType.PNG)
                self.log.info("'test_SearchUser_Excel_DDT_006' is failed")
                assert False
            elif self.su.Validate_UserSearch() != "Edit User" and self.Expected_Result == 'fail':
                User_Name =XLUtils.WriteData(self.Excel_File_Path, 'Excel_SearchUser', r, 4, 'fail')
                Status =XLUtils.WriteData(self.Excel_File_Path, 'Excel_SearchUser', r, 5, 'pass')

                self.log.info("user found")
                # Capturing Screenshot
                self.log.info("Capturing Screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_SearchUser_Excel_DDT_006_Pass.png")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_SearchUser_Excel_DDT_006_Pass", attachment_type=AttachmentType.PNG)
                self.log.info("'test_SearchUser_Excel_DDT_006' is passed")
                assert True
            self.su.Click_Dashboard()
            self.su.Click_UserManagement()
        self.log.info("'test_SearchUser_Excel_DDT_006' is completed\n")
