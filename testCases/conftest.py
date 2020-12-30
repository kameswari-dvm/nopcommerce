from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        # driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


# This will take arguments from the command line
def pytest_addoption(parser):
    parser.addoption("--browser")


# This will return the browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project Name'] = 'nop-commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'D.V.M.Kameswari'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
