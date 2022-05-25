import pytest
from Web.Base.base import *
from Web.Pages.Login_Page import LoginPage
import allure
from allure_commons.types import AttachmentType


@pytest.mark.usefixtures('set_up')
class TestLogin(Base):

    @pytest.mark.sanity
    def test_login_success(self):
        driver = self.driver
        login = LoginPage(driver)
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,login.login_button))).click()
        login.click_login_button()
        login.enter_email("tsiona@gmail.com")
        login.enter_password('123456')
        login.click_singIn()

        value = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'log out')]"))).get_attribute("innerText")
        try:
            assert value == "log out"
        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(),name="Error screenshot",attachment_type=AttachmentType.PNG)

    @pytest.mark.sanity
    def test_invalid_login_when_password_incorrect(self):
        driver = self.driver
        login = LoginPage(driver)
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,login.login_button))).click()
        login.click_login_button()
        login.enter_email("tsiona@gmail.com")
        login.enter_password("123")
        login.click_singIn()

        value = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h4[contains(text(),'incorrect Password/Email')]"))).get_attribute("innerText")
        try:
            assert value == "incorrect Password/Email"
        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(),name="Error screenshot",attachment_type=AttachmentType.PNG)
            # allure.attach(driver.get_screenshot_as_png(),driver.save_screenshot("..//Results/screensot.png"), attachment_type=AttachmentType.PNG)

    @pytest.mark.regression
    def test_invalid_login_when_passwordField_is_null(self):
        driver = self.driver
        login = LoginPage(driver)
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,login.login_button))).click()
        login.click_login_button()
        login.enter_email("tsiona@gmail.com")
        login.enter_password("")
        login.click_singIn()

        buttonSingIN = driver.find_element(By.XPATH, "//div[1]/form[1]/input[3]").is_enabled()
        try:
            assert buttonSingIN == False
        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(),name="Error screenshot",attachment_type=AttachmentType.PNG)

    @pytest.mark.regression
    def test_invalid_login_when_emailField_is_null(self):
        driver = self.driver
        login = LoginPage(driver)
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,login.login_button))).click()
        login.click_login_button()
        login.enter_email("")
        login.enter_password("123456")
        login.click_singIn()

        buttonSingIN = driver.find_element(By.XPATH, "//div[1]/form[1]/input[3]").is_enabled()
        try:
            assert buttonSingIN == False
        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(),name="Error screenshot",attachment_type=AttachmentType.PNG)

    @pytest.mark.regression
    def test_invalid_login_when_all_fields_are_null(self):
        driver = self.driver
        login = LoginPage(driver)
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,login.login_button))).click()
        login.click_login_button()
        login.enter_email("")
        login.enter_password("")
        login.click_singIn()

        buttonSingIN = driver.find_element(By.XPATH, "//div[1]/form[1]/input[3]").is_enabled()
        try:
            assert buttonSingIN == False
        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(),name="Error screenshot",attachment_type=AttachmentType.PNG)

