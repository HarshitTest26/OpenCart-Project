import pytest
import time
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccount
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
from utilities import XLUtils
import os


class Test_login_dTT:
    baseURL = ReadConfig.getApplicationUrl()
    log = logGen.loggen()
    log.info("** LOGGING STARTED **")

    file = os.path.abspath(os.curdir)+"\\testData\\OpenCart_TestData.xlsx"

    @pytest.hookimpl(tryfirst=True)
    def test_login_DTT(self,setup):
        self.log.info("** STARTING DATA DRIVEN LOGIN TEST **")
        self.rows = XLUtils.rows_Count(self.file, sheetKaNaam='Sheet1')
        lst_status =[]

        self.driver = setup
        self.driver.get(self.baseURL)
        self.log.info("** URL HIT SUCCESSFUL")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = HomePage(self.driver)
        self.lg = LoginPage(self.driver)
        self.ma = MyAccount(self.driver)

        for r in range(2, self.rows+1):
            self.hp.myAccount()
            self.hp.clickLogin()

            self.email = XLUtils.read_data(self.file, 'Sheet1',rowno=r,colno=1)
            self.password = XLUtils.read_data(self.file, 'Sheet1',rowno=r,colno=2)
            self.exp_res = XLUtils.read_data(self.file,'Sheet1',r,3)

            self.lg.login_email(loginemail=self.email)
            self.lg.login_pass(loginpass=self.password)
            self.lg.login_btn()
            time.sleep(5)
            self.act = self.lg.login_confirm()

            if self.exp_res == 'Valid':
                if self.act:
                    lst_status.append("PASS")
                    self.ma.myaccountclk()
                    self.ma.logoutclk()
                else:
                    lst_status.append("FAIL")

            elif self.exp_res == 'Invalid':
                if self.act:
                    lst_status.append("FAIL")
                    self.ma.myaccountclk()
                    self.ma.logoutclk()
                else:
                    lst_status.append("PASS")

        self.driver.close()

        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.log.info("** END OF DATA DRIVEN TEST **")