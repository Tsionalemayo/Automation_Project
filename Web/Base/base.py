
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Web.Pages.Login_Page import LoginPage
from webdriver_manager.chrome import ChromeDriverManager

class Base:

    @pytest.fixture(autouse=True)
    def set_up(self,):
        print("Initiating Chrome driver")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(10)
        self.driver.get("https://wondemagen-barbershop.herokuapp.com/")
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()


    @pytest.fixture()
    def login(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]"))).click()
        login = LoginPage(driver)
        login.enter_email("tsiona@gmail.com")
        login.enter_password('123456')
        login.click_singIn()

    #     yield self.driver
