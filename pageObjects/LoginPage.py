from selenium.webdriver.common.by import By


class LoginPage:
    # lnk_login_Xpath = "//ul[@class='dropdown-menu dropdown-menu-right']/descendant::a[text()='Login']"
    txt_email_Xpath = "//input[@id='input-email']"
    txt_pass_Xpath = "//input[@id='input-password']"
    btn_ctn_Xpath = "//input[@value='Login']"
    ele_text_Xpath = "//h2[normalize-space()='My Account']"

    def __init__(self, driver):
        self.driver = driver

    # def login_lnk(self):
    #     self.driver.find_element(By.XPATH,self.lnk_login_Xpath).click()

    def login_email(self, loginemail):
        self.driver.find_element(By.XPATH, self.txt_email_Xpath).send_keys(loginemail)

    def login_pass(self, loginpass):
        self.driver.find_element(By.XPATH, self.txt_pass_Xpath).send_keys(loginpass)

    def login_btn(self):
        self.driver.find_element(By.XPATH, self.btn_ctn_Xpath).click()

    def login_confirm(self):
        try:
            return self.driver.find_element(By.XPATH, self.ele_text_Xpath).text
        except:
            var = None
