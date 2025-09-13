from pageObjects.AddToCart_Functionality import AddToCart
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
import os


class Test_AddToCart:
    baseURL = ReadConfig.getApplicationUrl()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = logGen.loggen()
    logger.info("** LOGGER INITIALIZED **")

    def test_add_to_cart(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.logger.info("** URL HIT SUCCESS **")

        self.hp = HomePage(self.driver)
        self.hp.myAccount()
        self.hp.clickLogin()

        self.lgn = LoginPage(self.driver)
        self.lgn.login_email(self.email)
        self.lgn.login_pass(self.password)
        self.lgn.login_btn()

        self.ac = AddToCart(self.driver)
        self.driver.get(self.baseURL)
        self.ac.search_input("iMac")
        self.driver.implicitly_wait(10)
        self.ac.search_btn()
        if self.ac.search_result_verify():
            self.logger.info("** ITEM IS DISPLAYED SUCCESSFULLY **")
            if self.ac.search_result_verify_title() == 'iMac':
                self.logger.info("** SEARCHED ITEM MATCHES WITH THE PRODUCT LISTED **")
                self.ac.product_img_click()
                self.ac.click_add_to_cart()
                self.message = self.ac.verify_add_to_cart_message()
            else:
                self.logger.info("** THE SEARCH RESULT DOESN'T MATCH **")

        if self.message:
            self.logger.info("** ITEM ADDED TO CART MESSAGE DISPLAYED SUCCESSFULLY **")
            self.ac.check_shopping_cart()
            if self.ac.verify_items_after_add():
                self.logger.info("** TEST PASSED **")
                assert True
                self.driver.close()
        else:
            self.logger.info("** TEST FAILED **")
            self.driver.save_screenshot(os.path.abspath(os.curdir + "\\screenshots\\Add_To_Cart.png"))
            assert False
