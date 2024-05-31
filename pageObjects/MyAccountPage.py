from selenium.webdriver.common.by import By


class MyAccount:
    btn_Xpath_myAcc = "//span[normalize-space()='My Account']//ancestor::a[@class = 'dropdown-toggle']"
    btn_Xpath_logout = "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver = driver

    def myaccountclk(self):
        self.driver.find_element(By.XPATH,self.btn_Xpath_myAcc).click()

    def logoutclk(self):
        self.driver.find_element(By.XPATH,self.btn_Xpath_logout).click()