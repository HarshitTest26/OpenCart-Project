from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class AddToCart:
    txt_name_search = 'search'
    btn_xpath_search = "//button[@class='btn btn-default btn-lg']"
    img_xpath_SearchResult = "//div[@class='image']//img[@title='iMac']"
    btn_xpath_addToCart = "//div[@class='form-group']//button[text()='Add to Cart']"
    alert_xpath_ConfirmMsg = "//div[@class='alert alert-success alert-dismissible']"
    menu_xpath_shoppingCart = "//span[normalize-space()='Shopping Cart']"
    table_xpath_itemsAfterAdd = "//div[@class='table-responsive']"

    def __init__(self, driver):
        self.driver = driver

    def search_input(self, sinput):
        self.driver.find_element(By.NAME, self.txt_name_search).send_keys(sinput)

    def search_btn(self):
        self.driver.find_element(By.XPATH, self.btn_xpath_search).click()

    def search_result_verify(self):
        try:
            element = self.driver.find_element(By.XPATH, self.img_xpath_SearchResult)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def search_result_verify_title(self):
        title_element = self.driver.find_element(By.XPATH,self.img_xpath_SearchResult)
        return title_element.get_attribute('title')

    def product_img_click(self):
        self.driver.find_element(By.XPATH, self.img_xpath_SearchResult).click()

    def click_add_to_cart(self):
        self.driver.find_element(By.XPATH,self.btn_xpath_addToCart).click()

    def verify_add_to_cart_message(self):
        try:
            pop_up_element = self.driver.find_element(By.XPATH,self.alert_xpath_ConfirmMsg)
            return pop_up_element.is_displayed()
        except NoSuchElementException:
            return False

    def check_shopping_cart(self):
        self.driver.find_element(By.XPATH,self.menu_xpath_shoppingCart).click()

    def verify_items_after_add(self):
        try:
            items = self.driver.find_element(By.XPATH,self.table_xpath_itemsAfterAdd)
            return items.is_displayed()
        except NoSuchElementException:
            return False



