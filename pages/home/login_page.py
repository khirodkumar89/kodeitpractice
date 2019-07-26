import time
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
class LoginPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    #LOCATERS
    _login_link = "//a[@class='navbar-link fedora-navbar-link']"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "//input[@name='commit']"
    _user_icon = "//img[@class='gravatar']"
    _logout_link = "//a[@href='/current_user/contact']"
    # def getloginlink(self):
    #     return self.driver.find_element(By.XPATH, self._login_link)
    # def getemailfield(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    # def getpasswordfield(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    # def getloginbutton(self):
    #     return self.driver.find_element(By.XPATH, self._login_button)
    # def getusericon(self):
    #     return self.driver.find_element(By.XPATH, self._user_icon)
    # def getlogoutlink(self):
    #     self.driver.find_element(By.XPATH, self._logout_link)
    def clickloginlink(self):
        self.elementclick(self._login_link, locatertype="xpath")
    def enteremailfield(self, email):
        self.sendkeys(email, self._email_field ,locatertype="id")
    def enterpasswordfield(self, password):
        self.sendkeys(password, self._password_field, locatertype="id")
    def clickloginbutton(self):
        self.elementclick(self._login_button, locatertype="xpath")
    def clickusericon(self):
        self.elementclick(self._user_icon, locatertype="xpath")
    def clicklogoutlink(self):
        self.elementclick(self._logout_link, locatertype="xpath")
    def login(self,email, password):
        self.clickloginlink()
        self.enteremailfield(email)
        self.enterpasswordfield(password)
        self.clickloginbutton()

    def logout(self):
        self.clickusericon()
        time.sleep(4)
        self.clicklogoutlink()
        time.sleep(4)
    def verifyloginsuccessful(self):
        result = self.isElementpresent("//a[@href='/sign_out']", locatertype="xpath")
        return result
    def verifyloginfailed(self):
        result = self.isElementpresent("//div[contains(text(),'Invalid email or password.')]", locatertype="xpath")
        return result
    def verifyTitle(self):
        if "Let's Kode It" in self.getTitle():
            return True
        else:
            return False
