from pageobjects.customerPage import Customer
from pageobjects.LoginPage import Login
from utilities.readConfigProperties import get_login_info
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
import time


class Test_add_new_customer:
    base_url = get_login_info.get_base_url()
    username = get_login_info.get_username()
    password = get_login_info.get_password()
    logger = LogGen.loggen()

    def test_add_new_customer(self, setup):
        self.logger.info("Test case : Verifying login with valid credentials")
        self.logger.info("Test case name: test_verify_login")
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_obj = Login(self.driver)
        self.login_obj.set_username(self.username)
        self.login_obj.set_password(self.password)
        self.login_obj.click_login()
        time.sleep(1)
        self.cp = Customer(self.driver)
        self.cp.click_on_customer_menu()
        time.sleep(1)
        self.cp.click_on_customer_sub_menu()
        time.sleep(1)
        self.cp.click_on_add_new_customer()
        time.sleep(1)
        self.cp.set_email("will@tipeurope.com")
        self.cp.set_password("tipeurope")
        self.cp.set_first_name("william")
        self.cp.set_last_name("Harry")
        self.cp.set_gender("Female")
        self.cp.set_date_of_birth("02-04-1981")
        self.cp.select_tax_exempt(True)
        self.cp.set_customer_role()
        self.cp.click_save_button()
        time.sleep(5)
        msg = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']").text
        if msg == "The new customer has been added successfully.":
            self.logger.info("Test_add_new_customer test case passed")
            assert True
        else:
            self.logger.info("Test_add_new_customer test case failed")
