from pageobjects.LoginPage import Login
from utilities.customLogger import LogGen
from utilities.readConfigProperties import get_login_info


class Test_Login:
    base_url = get_login_info.get_base_url()
    username = get_login_info.get_username()
    password = get_login_info.get_password()
    logger = LogGen.loggen()

    def test_verify_login(self, setup):
        self.logger.info("Test case : Verifying login with valid credentials")
        self.logger.info("Test case name: test_verify_login")
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_obj = Login(self.driver)
        self.login_obj.set_username(self.username)
        self.login_obj.set_password(self.password)
        self.login_obj.click_login()
        if self.driver.title == "Dashboard / nopCommerce administration":
            self.logger.info("Test case PASSED")
            assert True
        else:
            self.driver.save_screenshot(".//screenshots//" + "Test_Login.png")
            self.logger.info("Test case FAILED")
            assert False
        self.logger.info("*****************************************")
        self.driver.close()

    def test_verify_home_page_title(self, setup):
        self.logger.info("Test case : Verifying title of the home page")
        self.logger.info("Test case name: verify_home_page_title")
        self.driver = setup
        self.driver.get(self.base_url)
        current_page_title = 'Your store. Login'
        if self.driver.title == current_page_title:
            self.logger.info("Test case PASSED")
            assert True
        else:
            self.driver.save_screenshot(".//screenshots//" + "Home_page_title.png")
            self.logger.info("Test case FAILED")
            assert False
        self.driver.close()
