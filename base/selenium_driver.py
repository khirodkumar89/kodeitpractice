from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.common.exceptions import *
import utilitis.customlogger as cl
import logging
from selenium.webdriver.common.by import By
class SeleniumDriver():
    log = cl.Customlogger(logging.DEBUG)
    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def getBytype(self, locatertype):
        locatertype = locatertype.lower()
        if locatertype == "id":
            return By.ID
        elif locatertype == "name":
            return By.NAME
        elif locatertype == "xpath":
            return By.XPATH
        elif locatertype == "css":
            return By.CSS_SELECTOR
        elif locatertype == "class":
            return By.CLASS_NAME
        elif locatertype == "link":
            return By.LINK_TEXT
        else:
            self.log.info("locater type not supported")

    def getElement(self, locater, locatertype="id"):
        element = None
        try:
            bytype = self.getBytype(locatertype)
            element = self.driver.find_element(bytype, locater)
            self.log.info("found an element with locater :" + locater + " and locatertype " + locatertype)
        except:
            self.log.info("element not found with locater :" + locater + " and locatertype " + locatertype)
        return element

    def elementclick(self, locater, locatertype):
        try:
            element = self.getElement(locater, locatertype)
            element.click()
            self.log.info("clicked on the element with locater :" + locater + " and locatertype " + locatertype)
        except:
            self.log.info("cann't click on the element with locater :" + locater + " and locatertype " + locatertype)

    def sendkeys(self, data, locater, locatertype):
        locatertype = locatertype.lower()
        try:
            element = self.getElement(locater, locatertype)
            element.clear()
            element.send_keys(data)
            self.log.info("sent keys with locater :" + locater + " and locatertype " + locatertype)
        except:
            self.log.info("cann't send keys with locater :" + locater + " and locatertype " + locatertype)

    def isElementpresent(self, locater, locatertype):
        try:
            locatertype = locatertype.lower()
            element = self.getElement(locater, locatertype)
            if element is not None:
                self.log.info("found an element with locater :" + locater + " and locatertype " + locatertype)
                return True
            else:
                return False
        except:
            self.log.info("cann't find element with locater :" + locater + " and locatertype " + locatertype)

    def elementlistpresent(self, locater, locatertype):
        try:
            elementlist = self.driver.find_elements(locater, locatertype)
            if len(elementlist) > 0:
                self.log.info("found an element list with locater :" + locater + " and locatertype " + locatertype)
                return True
            else:
                return False
        except:
            self.log.info("cann't find element list with locater :" + locater + " and locatertype " + locatertype)
            return False
    def Waitforelement(self,locater, locatertype="id", timeout=100, pollfrequency=0.5):
        element = None
        try:
            bytype = self.getBytype(locatertype)
            wait = WebDriverWait(self.driver, timeout=100, poll_frequency=0.5, ignored_exceptions=
                                                                   [NoSuchElementException,
                                                                    ElementNotSelectableException,
                                                                    ElementNotVisibleException])
            element = wait.until(Ec.element_to_be_clickable((bytype, "//a[@href='/sign_out']")))
            self.log.info("element appeard on the webpage with locater :" + locater + " and locatertype " + locatertype)
        except:
            self.log.info("element doesn't appeared on the webpage with locater :" + locater + " and locatertype " + locatertype)
        return element