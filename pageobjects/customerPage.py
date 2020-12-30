import time
from selenium.webdriver.common.by import By


class Customer:
    menu_customers_xpath = "//li[contains(@class,'treeview')][3]"
    sub_menu_customers_xpath = "//li[contains(@class,'treeview')][3]//ul/li[1]"
    button_add_new_customer_xpath = "//a[@class='btn bg-blue']"
    text_email_id = "Email"
    text_password_id = "Password"
    text_firstname_id = "FirstName"
    text_lastname_id = "LastName"
    rd_gender_male_id = "Gender_Male"
    rd_gender_female_id = "Gender_Female"
    text_date_of_birth_id = "DateOfBirth"
    text_company_id = "Company"
    ch_box_is_tax_exempt_id = "IsTaxExempt"
    dropdown_customer_roles = "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    listbox_customer_role_xpath = "//div[contains(@class,'k-widget k-multiselect k-multiselect-clearable " \
                                  "k-state-hover')] "
    dropdown_guest_role = "//ul[@id='SelectedCustomerRoleIds_listbox']/li[text()='Guests']"
    dropdown_registered_role = "//ul[@id='SelectedCustomerRoleIds_listbox']/li[text()='Registered']"
    button_close = "//span[@title='delete']"
    select_multiple_customer_roles_id = "SelectedCustomerRoleIds"
    button_save_xpath = "//button[@type='submit'][@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_customer_menu(self):
        self.driver.find_element(By.XPATH, self.menu_customers_xpath).click()

    def click_on_customer_sub_menu(self):
        self.driver.find_element(By.XPATH, self.sub_menu_customers_xpath).click()

    def click_on_add_new_customer(self):
        self.driver.find_element(By.XPATH, self.button_add_new_customer_xpath).click()

    def set_email(self, email):
        self.driver.find_element(By.ID, self.text_email_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def set_first_name(self, firstName):
        self.driver.find_element(By.ID, self.text_firstname_id).send_keys(firstName)

    def set_last_name(self, lastName):
        self.driver.find_element(By.ID, self.text_lastname_id).send_keys(lastName)

    def set_gender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rd_gender_male_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rd_gender_female_id).click()
        else:
            self.driver.find_element(By.ID, self.rd_gender_female_id).click()

    def set_date_of_birth(self, date_of_birth):
        self.driver.find_element(By.ID, self.text_date_of_birth_id).send_keys(date_of_birth)

    def select_tax_exempt(self, status):
        if status:
            self.driver.find_element(By.ID, self.ch_box_is_tax_exempt_id).click()

    def set_customer_role(self):
        self.driver.find_element(By.XPATH, self.dropdown_customer_roles).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.button_close).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.dropdown_customer_roles).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.dropdown_guest_role).click()

    def click_save_button(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()
