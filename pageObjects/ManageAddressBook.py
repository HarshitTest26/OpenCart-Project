from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException


class Add_address:
    # only mandatory fields and steps
    drp_MyAccount_xpath = "//span[normalize-space()='My Account']"
    drpEle_MyAccount_xpath = "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='My Account']"
    lnk_ModifyAddress_xpath = "//a[text()='Modify your address book entries']"
    btn_NewAddress_xpath = "//a[text()='New Address']"
    txt_FirstName_id = 'input-firstname'
    txt_LastName_id = "input-lastname"
    txt_Address_1_id = 'input-address-1'
    txt_City_id = 'input-city'
    txt_PostalCode_id = "input-postcode"
    drp_Country_id = 'input-country'
    drp_Region_State_id = 'input-zone'
    radBtn_DefaultAddress_name = 'default'
    btn_Continue_xpath = "//input[@value='Continue']"
    alert_CnfMessage_xpath = "//div[@class='alert alert-success alert-dismissible']"

    def __init__(self, driver):
        self.driver = driver

    def go_to_MyAccount(self):
        self.driver.find_element(By.XPATH, self.drp_MyAccount_xpath).click()
        self.driver.find_element(By.XPATH, self.drpEle_MyAccount_xpath).click()

    def add_address_lnk(self):
        self.driver.find_element(By.XPATH, self.lnk_ModifyAddress_xpath).click()

    def new_address_btn(self):
        self.driver.find_element(By.XPATH, self.btn_NewAddress_xpath).click()

    def first_name(self, fname):
        self.driver.find_element(By.ID, self.txt_FirstName_id).send_keys(fname)

    def last_name(self, lname):
        self.driver.find_element(By.ID, self.txt_LastName_id).send_keys(lname)

    def Address1(self, address_1):
        self.driver.find_element(By.ID, self.txt_Address_1_id).send_keys(address_1)

    def City(self, city):
        self.driver.find_element(By.ID, self.txt_City_id).send_keys(city)

    def PostalCode(self, code):
        self.driver.find_element(By.ID, self.txt_PostalCode_id).send_keys(code)

    def Country(self, country):
        country_ele = self.driver.find_element(By.ID, self.drp_Country_id)
        sel = Select(country_ele)
        sel.select_by_visible_text(country)

    # Since, this is not a bootstrapped dropdown we will use Select and Option class from Webdriver
    def Region(self, region):
        region_ele = self.driver.find_element(By.ID, self.drp_Region_State_id)
        # making object for Select class
        sel = Select(region_ele)
        sel.select_by_visible_text(region)

    def radBtn_setDefault(self):
        self.driver.find_element(By.NAME, self.radBtn_DefaultAddress_name).click()

    def continue_btn(self):
        self.driver.find_element(By.XPATH, self.btn_Continue_xpath).click()

    # Below are the methods for assertion
    @property
    def message_text(self):
        try:
            Cnf_msg = self.driver.find_element(By.XPATH, self.alert_CnfMessage_xpath).text
            if Cnf_msg == "Your address has been successfully added":
                return True
            else:
                return False
        except NoSuchElementException:
            return False
