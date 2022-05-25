import pytest

from Web.Base.base import Base
from Web.Pages.Message_Page import *
from Web.Locators.Messages_Locators import MessagesLocators


@pytest.mark.usefixtures('set_up')
@pytest.mark.usefixtures('login')
class TestMessage(Base):

    def test_send_message_correctly(self):
        driver= self.driver
        message = MessagesPage(driver)
        message = MessagesPage(driver)
        message.click_messagesPage()
        message.enter_phone(MessagesLocators.phoneNum)
        message.enter_name(MessagesLocators.fullName)
        message.enter_message(MessagesLocators.contentMessage)
        message.click_send_message()

        popUpMesagge = driver.switchTo().alert().getText()

        assert popUpMesagge == "the message was sent successfully"

                                                                                                                       # # האם הכפתור לחיץ





