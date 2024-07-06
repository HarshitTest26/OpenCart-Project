from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
from pageObjects.ManageAddressBook import Add_address
from utilities import XLUtils
import os


class Test_add_Address:
    baseURL = ReadConfig.getApplicationUrl()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger = logGen.loggen()
    file = os.path.abspath(os.curdir)+"\\testData\\Add_Address_Data.xlsx"

    lst_status = []

    def test_add_NewAddress(self, setup):
        self.rows = XLUtils.rows_Count(file=self.file, sheetKaNaam='Sheet1')
        self.logger.info("** Add_Address_TestCase **")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = HomePage(self.driver)
        self.hp.myAccount()
        self.hp.clickLogin()

        self.lg = LoginPage(self.driver)
        self.lg.login_email(self.email)
        self.lg.login_pass(self.password)
        self.lg.login_btn()

        self.Ma = Add_address(self.driver)
        self.Ma.go_to_MyAccount()
        self.Ma.add_address_lnk()
        self.Ma.new_address_btn()
        self.logger.info("** STARTING READING DATA FROM EXCEL **")

        for r in range(2, self.rows+1):
            self.Ma.first_name(XLUtils.read_data(file=self.file,sheetName='Sheet1',rowno=r,colno=1))
            self.Ma.last_name(XLUtils.read_data(file=self.file,sheetName='Sheet1',rowno=r,colno=2))
            self.Ma.Address1(XLUtils.read_data(file=self.file,sheetName='Sheet1',rowno=r,colno=3))
            self.Ma.City(XLUtils.read_data(file=self.file,sheetName='Sheet1',rowno=r,colno=4))
            self.Ma.PostalCode(XLUtils.read_data(file=self.file,sheetName='Sheet1',rowno=r,colno=5))
            self.Ma.Country(XLUtils.read_data(file=self.file,sheetName='Sheet1',rowno=r,colno=6))
            self.Ma.Region(XLUtils.read_data(file=self.file,sheetName='Sheet1',rowno=r,colno=7))

            self.Ma.radBtn_setDefault()

            self.Ma.continue_btn()
# capture successful message and append the same in the list, and then assert and then again repeat new address
            if self.Ma.message_text:
                self.lst_status.append("Pass")
                self.Ma.new_address_btn()
            else:
                self.lst_status.append("Fail")
                self.driver.save_screenshot(os.path.abspath(os.curdir + "\\screenshots\\Add_AddressError.png"))
                self.driver.close()

        self.driver.close()

        if "Fail" not in self.lst_status:
            assert True
        else:
            assert False
        self.logger.info("** END OF ADD ADDRESS TEST CASE **")