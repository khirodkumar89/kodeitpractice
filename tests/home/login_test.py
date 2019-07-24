from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
from utilitis.teststatus import TestStatus
import unittest
import pytest
import time

@pytest.mark.usefixtures("onetimesetup", "setup")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classsetup(self, onetimesetup):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order=2)
    def test_validlogin(self):
        self.lp.login("test@email.com", "abcabc")
        self.lp.logout()
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "title not correct")
        result2 = self.lp.verifyloginsuccessful()
        self.ts.markfinal("test_validlogin", result2, "login succussful")
    @pytest.mark.run(order=1)
    def test_invalidlogin(self):
        self.lp.login("test@email.com", "abcabccc")
        result = self.lp.verifyloginfailed()
        assert result == True


