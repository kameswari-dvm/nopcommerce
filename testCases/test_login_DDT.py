from utilities import ExcelUtils
from utilities.readConfigProperties import get_login_info
from pageobjects.LoginPage import Login
from utilities.customLogger import LogGen
import time


class Test_Login_DDT:
    path = ".\\testdata\\employee_data.xlsx"
    base_url = get_login_info.get_base_url()

    def test_verify_login_DDT(self, setup):
        self.logger = LogGen.loggen()
        # column = ExcelUtils.get_columns_count(self.path)
        row = ExcelUtils.get_rows_count(self.path)
        self.logger.info("test_verify_login_DDT testcase has started")
        self.driver = setup
        self.lp = Login(self.driver)
        list_result = []
        for i in range(2, row + 1):
            username = ExcelUtils.read_excel_file_data(self.path, i, 1)
            password = ExcelUtils.read_excel_file_data(self.path, i, 2)
            expected_result = ExcelUtils.read_excel_file_data(self.path, i, 3)
            self.driver.get(self.base_url)
            self.lp.set_username(username)
            self.lp.set_password(password)
            self.lp.click_login()
            time.sleep(2)
            if self.driver.title == 'Dashboard / nopCommerce administration':
                if expected_result == 'Pass':
                    self.logger.info("Passed")
                    list_result.append('Pass')
                    assert True
                elif expected_result == 'Fail':
                    self.logger.info("Failed")
                    list_result.append('Fail')
                    assert True
            elif self.driver.title != 'Dashboard / nopCommerce administration':
                if expected_result == 'Pass':
                    self.logger.info("Failed")
                    list_result.append('Fail')
                    assert False
                elif expected_result == 'Fail':
                    self.logger.info("Passed")
                    list_result.append('Pass')
                    assert True
        try:
            if 'Fail' not in list_result:
                self.logger.info("TEST CASE PASSED")
            else:
                self.logger.info("TEST CASE FAILED")
        finally:
            self.driver.close()
        self.logger.info("***********Test case test_verify_login_DDT has completed********")
