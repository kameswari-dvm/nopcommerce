import time
from selenium.webdriver.common.by import By


class Login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//input[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        ele = self.driver.find_element(By.ID, self.textbox_username_id)
        ele.clear()
        time.sleep(1)
        ele.send_keys(username)

    def set_password(self, password):
        ele = self.driver.find_element(By.ID, self.textbox_password_id)
        ele.clear()
        time.sleep(1)
        ele.send_keys(password)

    def click_login(self):
        ele = self.driver.find_element(By.XPATH, self.button_login_xpath)
        ele.click()
        time.sleep(1)
