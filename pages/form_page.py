from time import sleep
from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.forms_locators import FillFormLocators



class FillFormPage(BasePage):

    locators = FillFormLocators()


    def fill_student_registration_form(self):
        self.remove_footer()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys('John')
        self.element_is_visible(self.locators.LAST_NAME).send_keys('Doe')
        self.element_is_visible(self.locators.EMAIL).send_keys('test_test@test.com')
        self.element_is_present(self.locators.RADIO_BUTTON_MALE).click()
        self.element_is_visible(self.locators.MOBILE_NUMBER).send_keys('8888888888')
        # self.element_is_visible(self.locators.BIRTHDAY).click()
        subject = self.element_is_present(self.locators.SUBJECTS)
        subject.click()
        subject.send_keys('Maths')
        subject.send_keys(Keys.ENTER)
        self.element_is_visible(self.locators.SPORT_CHECKBOX).click()
        self.element_is_visible(self.locators.MUSIC_CHECKBOX).click()
        path = r'F:\My Projects\DemoQA\requirements.txt'
        self.element_is_visible(self.locators.UPLOAD_FILE).send_keys(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('Some current address where i live')
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.ENTER)
        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.ENTER)
        self.element_is_present(self.locators.SUBMIT_BUTTON).click()
        self.element_is_visible(self.locators.CLOSE_BUTTON).click()

