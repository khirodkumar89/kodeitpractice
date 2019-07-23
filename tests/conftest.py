from selenium import webdriver
from base.webdriverfactory import Webdriverfactory
import pytest


@pytest.yield_fixture()
def setup():
    print("method level setup")
    yield
    print("method level tear down")

@pytest.yield_fixture(scope="class")
def onetimesetup(request, browser):
    print("one time setup")
    wdf = Webdriverfactory(browser)
    driver = wdf.getwedriverfactory()
    # if browser == 'chrome':
    #     baseurl = "https://learn.letskodeit.com/"
    #     driver = webdriver.Chrome(
    #         executable_path="C:\\Users\\khirod\\PycharmProjects\\kodeitpractice\\driver\\chromedriver.exe")
    #     driver.maximize_window()
    #     driver.implicitly_wait(20)
    #     driver.get(baseurl)
    #     print("running test on chrome")
    # else:
    #     baseurl = "https://learn.letskodeit.com/"
    #     driver = webdriver.Firefox(
    #         executable_path="C:\\Users\\khirod\\PycharmProjects\\kodeitpractice\\driver\\geckodriver.exe")
    #     driver.maximize_window()
    #     driver.implicitly_wait(20)
    #     driver.get(baseurl)
    #     print("running test on firefox")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("one time teardown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--ostype")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def ostype(request):
    return request.config.getoption("--ostype")
