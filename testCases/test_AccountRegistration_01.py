from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.HomePage import HomePage
from utilities import randomString
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
import time


class Test_AccountRegistration_01:
    baseURL = ReadConfig.getApplicationUrl()
    logger = logGen.loggen()
    logger.info("Logger initialized successfully")

    def test_account_reg(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("*** URL HIT SUCCESSFUL ***")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = HomePage(self.driver)
        self.logger.info("*** CLICKING ON MY ACCOUNT --> REGISTER ***")
        self.hp.myAccount()
        self.hp.clickRegister()

        self.arp = AccountRegistrationPage(self.driver)
        self.logger.info("*** PROVIDING FORM DETAILS ***")
        self.arp.setFirstname("John")
        self.arp.setLastname("Carter")

        self.email = randomString.random_string_generator() + '@gmail.com'
        self.arp.setEmail(self.email)

        self.arp.setTelephone("984346678")
        self.arp.setPassword("Password@123")
        self.arp.setConfirmPassword("Password@123")
        self.logger.info("*** FORM DETAILS PROVIDED SUCCESSFULLY ***")

        self.logger.info("*** STARTING ACTIONS  ***")
        self.arp.selPolicy()
        self.arp.clickContinue()
        self.arp.addingWait()
        self.gpt = self.arp.getPageTitle()
        self.logger.info("*** ASSERTION STARTED ***")
        if self.gpt == "Your Account Has Been Created!":
            self.logger.info("*** ACCOUNT --> REGISTER --> PASSED***")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir+"\\screenshots\\account_reg1.png"))
            self.logger.error("*** ACCOUNT --> REGISTER --> FAILED ***")
            self.driver.close()
            assert False


