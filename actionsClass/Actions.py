from selenium import webdriver
from selenium.webdriver.common.by import By


class ActionsClass:

    @staticmethod
    def get_driver(self):
        self.driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return self.driver

    @staticmethod
    def get_web_elements(self, driver, by, by_value):
        return driver.find_elements(by, by_value)

    @staticmethod
    def js_click(driver, ele1):
        driver.execute_script("arguments[0].click();", ele1)

    @staticmethod
    def click(self, driver, by, by_value):
        ele = self.get_web_element(driver, by, by_value)
        ele.click()

    @staticmethod
    def get_web_element(self, driver, by, by_value):
        driver.find_element(By.ID, )
        return driver.find_element(by, by_value)

    @staticmethod
    def send_keys(self, driver, by, by_value, data):
        ele = self.get_web_element(driver, by, by_value)
        ele.clear()
        ele.send_keys(data)
