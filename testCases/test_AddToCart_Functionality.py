import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.AddToCart_Functionality import AddToCart
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen


class Test_AddToCart:
    """
    Test suite for the Add to Cart functionality on the OpenCart website.
    """
    baseURL = ReadConfig.getApplicationUrl()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = logGen.loggen()

    def test_add_to_cart(self, setup):
        """
        Tests the end-to-end add-to-cart workflow:
        1. Logs in a user.
        2. Searches for a product.
        3. Adds the product to the cart.
        4. Verifies the product is in the shopping cart.
        """
        self.logger.info("***** Starting Test_AddToCart Test *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.logger.info("** URL HIT SUCCESS **")

        # Login flow
        self.hp = HomePage(self.driver)
        self.hp.myAccount()
        self.hp.clickLogin()

        self.lgn = LoginPage(self.driver)
        self.lgn.login_email(self.email)
        self.lgn.login_pass(self.password)
        self.lgn.login_btn()

        # Re-navigate to the base URL after login to ensure a fresh page state
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)

        # Search and add to cart flow
        self.ac = AddToCart(self.driver)
        self.ac.search_input("iMac")
        self.ac.search_btn()

        if self.ac.search_result_verify():
            self.logger.info("** ITEM IS DISPLAYED SUCCESSFULLY **")
            if self.ac.search_result_verify_title() == 'iMac':
                self.logger.info("** SEARCHED ITEM MATCHES WITH THE PRODUCT LISTED **")
                self.ac.product_img_click()
                self.ac.click_add_to_cart()

                # Use a flexible wait for the success message to appear and then disappear.
                # The message might contain dynamic text, so a simple class-based locator is more reliable.
                try:
                    success_message_locator = (By.XPATH, "//div[contains(@class, 'alert-success')]")
                    WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located(success_message_locator)
                    )
                    self.logger.info("** ADD TO CART SUCCESS MESSAGE DISPLAYED **")

                    # Wait for the message to disappear before proceeding to click the shopping cart.
                    # This prevents the ElementNotInteractableException.
                    WebDriverWait(self.driver, 10).until(
                        EC.invisibility_of_element_located(success_message_locator)
                    )
                    self.logger.info("** ADD TO CART SUCCESS MESSAGE DISAPPEARED **")

                except Exception as e:
                    self.logger.error(f"Error while waiting for success message: {e}")
                    self.driver.save_screenshot(os.path.abspath(os.curdir + "\\screenshots\\Add_To_Cart_Error.png"))
                    assert False, "Failed to find or wait for success message."

                # Verify cart
                self.ac.check_shopping_cart()
                if self.ac.verify_items_after_add():
                    self.logger.info("** TEST PASSED: ITEM ADDED TO CART SUCCESSFULLY **")
                    assert True
                else:
                    self.logger.info("** TEST FAILED: ITEM NOT FOUND IN CART **")
                    self.driver.save_screenshot(
                        os.path.abspath(os.curdir + "\\screenshots\\Add_To_Cart_Verification_Failed.png"))
                    assert False
            else:
                self.logger.info("** TEST FAILED: THE SEARCH RESULT DOESN'T MATCH **")
                self.driver.save_screenshot(os.path.abspath(os.curdir + "\\screenshots\\Search_Mismatch.png"))
                assert False
        else:
            self.logger.info("** TEST FAILED: ITEM NOT DISPLAYED AFTER SEARCH **")
            self.driver.save_screenshot(os.path.abspath(os.curdir + "\\screenshots\\Search_Failed.png"))
            assert False