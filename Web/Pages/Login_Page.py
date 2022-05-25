import allure
from Web.Locators.Login_Locators import LoginLocators
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.login_button = LoginLocators.login_button
        self.email_txtbox_xpath = LoginLocators.email_txtbox_xpath
        self.pass_txtbox_xpath = LoginLocators.pass_txtbox_xpath
        self.signIn_btn_xpath = LoginLocators.signIn_btn_xpath

    @allure.step
    def click_login_button(self):
        self.driver.find_element(By.XPATH,self.login_button).click()

    @allure.step
    def enter_email(self, email):
        self.driver.find_element(By.XPATH,self.email_txtbox_xpath).send_keys(email)

    @allure.step
    def enter_password(self, password):
        self.driver.find_element(By.XPATH,self.pass_txtbox_xpath).send_keys(password)

    @allure.step
    def click_singIn(self):
        self.driver.find_element(By.XPATH,self.signIn_btn_xpath).click()