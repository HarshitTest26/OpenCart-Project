from selenium.webdriver.common.by import By
import time


class AccountRegistrationPage:
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = 'email'
    txt_telephone_name = 'telephone'
    txt_password_name = 'password'
    txt_confirmPassword_name = 'confirm'
    chk_policy_xpath = "//input[@name='agree']"
    btn_continue_xpath = "//input[@value='Continue']"
    msg_pagetitle_Xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self,driver):
        self.driver=driver

    def setFirstname(self,fname):
        self.driver.find_element(By.NAME, self.txt_firstname_name).send_keys(fname)

    def setLastname(self,lname):
        self.driver.find_element(By.NAME, self.txt_lastname_name).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.NAME, self.txt_email_name).send_keys(email)

    def setTelephone(self, telephone):
        self.driver.find_element(By.NAME, self.txt_telephone_name).send_keys(telephone)

    def setPassword(self,password):
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(password)

    def setConfirmPassword(self,confirmPassword):
        self.driver.find_element(By.NAME, self.txt_confirmPassword_name).send_keys(confirmPassword)

    def selPolicy(self):
        self.driver.find_element(By.XPATH, self.chk_policy_xpath).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()

    def addingWait(self):
        self.driver.implicitly_wait(10)

    def getPageTitle(self):
        try:
             return self.driver.find_element(By.XPATH, self.msg_pagetitle_Xpath).text
        
        except:
             None


