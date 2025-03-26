from selenium.webdriver.common.by import By


class SearchUser_Class:

    Click_UserManagement_Link_XPATH = "//a[normalize-space()='User Management']"
    Text_Username_XPATH = "//input[@id='username']"
    Click_SearchUser_Btn_XPATH = "//button[normalize-space()='Search User']"
    Click_Dashboard_Link_XPATH = "//a[normalize-space()='Dashboard']"
    Validate_UserSearch_XPATH = "//h2[normalize-space()='Edit User']"


    def __init__(self, driver):
        self.driver = driver

    def Click_UserManagement(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element(By.XPATH, self.Click_UserManagement_Link_XPATH).click()

    def Enter_Username(self, username):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element(By.XPATH, self.Text_Username_XPATH).send_keys(username)

    def Click_SearchUser_Button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element(By.XPATH, self.Click_SearchUser_Btn_XPATH).click()

    def Click_Dashboard(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element(By.XPATH, self.Click_Dashboard_Link_XPATH).click()

    def Validate_UserSearch(self):
        try:
            success_msg = self.driver.find_element(By.XPATH, self.Validate_UserSearch_XPATH).text
            return success_msg
        except:
            pass