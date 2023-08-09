from time import sleep
import requests
from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxLocators, CheckBoxLocators, RadioButtonLocators, WebTablesLocators,\
    ButtonsClickLocators, LinksLocators, LinksResponseLocators, UpDownloadLocators,DynamicPropertiesLocators



class ElementsPage(BasePage):

    tb_locators = TextBoxLocators()
    cb_locators = CheckBoxLocators()
    rb_locators = RadioButtonLocators()
    wt_locators = WebTablesLocators()
    b_locators = ButtonsClickLocators()
    l_locators = LinksLocators()
    lr_locators = LinksResponseLocators()
    up_locators = UpDownloadLocators()
    dp_locators = DynamicPropertiesLocators()

    def text_box_page(self):
        self.element_is_visible(self.tb_locators.FULL_NAME_INPUT).send_keys('John Doe')
        self.element_is_visible(self.tb_locators.EMAIL_INPUT).send_keys('john_doe@test.com')
        self.element_is_visible(self.tb_locators.CURRENT_ADRESS_INPUT).send_keys('Baker st. 223B')
        self.element_is_visible(self.tb_locators.PERMAMENT_ADRESS_INPUT).send_keys('Baker st. 222B')
        self.element_is_visible(self.tb_locators.SUBMIT_BUTTON).click()


    def check_box_page(self):
        self.element_is_visible(self.cb_locators.FIRST_DOWN_ARROW).click()
        self.element_is_visible(self.cb_locators.DOCUMENTS_CHECKBOX).click()
        self.element_is_visible(self.cb_locators.COLLAPSE_ALL_BUTTON).click()
        assert_choise = self.element_is_visible(self.cb_locators.ASSERT)
        assert assert_choise == assert_choise, 'Documents not click'


    def radio_button_page(self):
        self.element_is_visible(self.rb_locators.YES).click()
        self.text_presents_in_element(self.rb_locators.DISPLAY_YES, 'Yes')
        self.element_is_visible(self.rb_locators.IMPRESSIVE).click()
        self.text_presents_in_element(self.rb_locators.DISPLAY_IMPRESSIVE, 'Impressive')


    def web_tables_page(self):
        self.element_is_visible(self.wt_locators.ADD_BUTTON).click()
        self.element_is_visible(self.wt_locators.FORM_FIRST_NAME).send_keys('John')
        self.element_is_visible(self.wt_locators.FORM_LAST_NAME).send_keys('Doe')
        self.element_is_visible(self.wt_locators.FORM_EMAIL).send_keys('test_test@test.com')
        self.element_is_visible(self.wt_locators.FORM_AGE).send_keys('99')
        self.element_is_visible(self.wt_locators.FORM_SALARY).send_keys('1.000.000')
        self.element_is_visible(self.wt_locators.FORM_DEPARTMENT).send_keys('Killer')
        self.element_is_visible(self.wt_locators.FORM_SUBMIT_BUTTON).click()


    def buttons_click_page(self):
        self.double_click(self.element_is_visible(self.b_locators.DOUBLE_CLICK_ME))
        self.text_presents_in_element(self.b_locators.DOUBLE_CLICK_MESSAGE, 'You have done a double click')
        self.right_click(self.element_is_visible(self.b_locators.RIGHT_CLICK_ME))
        self.text_presents_in_element(self.b_locators.RIGHT_CLICK_MESSAGE, 'You have done a right click')
        self.element_is_visible(self.b_locators.CLICK_ME).click()
        self.text_presents_in_element(self.b_locators.CLICK_MESSAGE, 'You have done a dynamic click')


    def links_page(self):
        self.element_is_visible(self.l_locators.HOME_LINK).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.element_is_visible(self.l_locators.LOAD_LOCATOR)
        self.driver.close()


    def response_links_page(self):
        self.element_is_visible(self.lr_locators.CREATED_LINK).click()
        self.text_presents_in_element(self.lr_locators.CREATED_STATUS, '201')
        self.text_presents_in_element(self.lr_locators.CREATED_TEXT, 'Created')
        self.element_is_visible(self.lr_locators.NO_CONTENT_LINK).click()
        self.text_presents_in_element(self.lr_locators.NO_CONTENT_STATUS, '204')
        self.text_presents_in_element(self.lr_locators.NO_CONTENT_TEXT, 'No Content')
        self.element_is_visible(self.lr_locators.MOVED_LINK).click()
        self.text_presents_in_element(self.lr_locators.MOVED_STATUS, '301')
        self.text_presents_in_element(self.lr_locators.MOVED_TEXT, 'Moved Permanently')
        self.element_is_visible(self.lr_locators.BAD_REQUEST_LINK).click()
        self.text_presents_in_element(self.lr_locators.BAD_REQUEST_STATUS, '400')
        self.text_presents_in_element(self.lr_locators.BAD_REQUEST_TEXT, 'Bad Request')
        self.element_is_visible(self.lr_locators.UNAUTHORIZED_LINK).click()
        self.text_presents_in_element(self.lr_locators.UNAUTHORIZED_STATUS, '401')
        self.text_presents_in_element(self.lr_locators.UNAUTHORIZED_TEXT, 'Unauthorized')
        self.element_is_visible(self.lr_locators.FORBIDDEN_LINK).click()
        self.text_presents_in_element(self.lr_locators.FORBIDDEN_STATUS, '403')
        self.text_presents_in_element(self.lr_locators.FORBIDDEN_TEXT, 'Forbidden')
        self.element_is_visible(self.lr_locators.NOT_FOUND_LINK).click()
        self.text_presents_in_element(self.lr_locators.NOT_FOUND_STATUS, '403')
        self.text_presents_in_element(self.lr_locators.NOT_FOUND_TEXT, 'Not Found')


    def up_down_load_file_page(self):
        path = r'F:\My Projects\DemoQA\requirements.txt'
        self.element_is_present(self.up_locators.UPLOAD_FILE).send_keys(path)
        self.element_is_visible(self.up_locators.UPLOAD_MESSAGE)
        self.element_is_visible(self.up_locators.DOWNLOAD_BUTTON).click()


    def dynamic_properties_page(self):
        self.element_is_clickable(self.dp_locators.WILL_ENABLE).click()
        self.element_is_present(self.dp_locators.COLOR_CHANGE).click()
        self.element_is_visible(self.dp_locators.VISIBLE_AFTER).click()
