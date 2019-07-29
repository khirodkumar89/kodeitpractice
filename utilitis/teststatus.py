from base.selenium_driver import SeleniumDriver
import utilitis.customlogger as cl
import logging


class TestStatus(SeleniumDriver):
    log = cl.Customlogger(logging.DEBUG)
    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        self.resultlist = []
    def setresult(self, result, resultmessage):
        try:
            if result is not None:
                if result:
                    self.resultlist.append("PASS")
                    self.log.info("## verification successful " + resultmessage)
                else:
                    self.resultlist.append("FAIL")
                    self.log.info("## verification failed " + resultmessage)
                    self.screenshot(resultmessage)
            else:
                self.resultlist.append("FAIL")
                self.log.info("## verification failed " +resultmessage)
                self.screenshot(resultmessage)
        except:
            self.resultlist.append("FAIL")
            self.log.error("## exception occured")
            self.screenshot(resultmessage)

    def mark(self, result, resultmessage):
        self.setresult(result, resultmessage)

    def markfinal(self, testname, result, resultmessage):
        self.setresult(result, resultmessage)
        if 'FAIL' in self.resultlist:
            self.log.error("### test failed")
            self.resultlist.clear()
            assert True ==False
        else:
            self.log.error("### test successful")
            self.resultlist.clear()
            assert True == False





