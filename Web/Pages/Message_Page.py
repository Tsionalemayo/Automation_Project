from Web.Locators.Messages_Locators import MessagesLocators
from selenium.webdriver.common.by import By


class MessagesPage:

    def __init__(self, driver):
        self.driver = driver
        self.messagePage_xpath = MessagesLocators.messagePage_xpath
        self.phone_field_xpath = MessagesLocators.phone_field_xpath
        self.name_field_xpath = MessagesLocators.name_field_xpath
        self.message_field_xpath = MessagesLocators.message_field_xpath
        self.send_message_button= MessagesLocators.send_message_button

    def click_messagesPage(self):
        self.driver.find_element(By.XPATH, self.messagePage_xpath).click()

    def enter_phone(self,phone):
        self.driver.find_element(By.XPATH,self.phone_field_xpath).send_keys(phone)

    def enter_name(self,name):
        self.driver.find_element(By.XPATH,self.name_field_xpath).send_keys(name)

    def enter_message(self,contentMessage):
        self.driver.find_element(By.XPATH,self.message_field_xpath).send_keys(contentMessage)

    def click_send_message(self):
        self.driver.find_element(By.XPATH,self.send_message_button).click()

