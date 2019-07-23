from selenium import webdriver

class Webdriverfactory():
    def __init__(self, browser):
        self.browser = browser

    def getwedriverfactory(self):
        baseurl = "https://learn.letskodeit.com/"
        if self.browser == 'chrome':
            driver = webdriver.Chrome(executable_path=
                                      "C:\\Users\\khirod\\PycharmProjects\\kodeitpractice\\driver\\chromedriver.exe")
        elif self.browser == 'firefox':
            driver = webdriver.Firefox(executable_path=
                                        "C:\\Users\\khirod\\PycharmProjects\\kodeitpractice\\driver\\geckodriver.exe")
        else:
            driver = webdriver.Chrome(executable_path=
                                      "C:\\Users\\khirod\\PycharmProjects\\kodeitpractice\\driver\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get(baseurl)
        return driver
