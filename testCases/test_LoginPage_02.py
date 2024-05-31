import time

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import logGen
from utilities.readProperties import ReadConfig
import os

class Test_login():
    base_url = ReadConfig.getApplicationUrl()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = logGen.loggen()
    logger.info("Logger initialized successfully")

    def test_login1(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("*** LOGIN URL HIT SUCCESSFUL ***")
        self.driver.implicitly_wait(10)

        self.hp = HomePage(self.driver)
        self.hp.myAccount()
        time.sleep(3)
        self.hp.clickLogin()

        self.lg = LoginPage(self.driver)
        # self.lg.login_lnk()
        self.lg.login_email(self.email)
        self.lg.login_pass(self.password)
        self.lg.login_btn()
        self.cnf = self.lg.login_confirm()
        self.logger.info("*** ASSERTION STARTED ***")
        if self.cnf == "My Account":
            assert True
            self.logger.info("*** ACCOUNT --> LOGIN --> PASSED***")
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir + "\\screenshots\\Login_Page.png"))
            self.driver.close()
            assert False


