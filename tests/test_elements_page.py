from time import sleep
from pages.elements_page import ElementsPage


class TestElementsPage:


    def test_text_box(self, driver):
        text_box = ElementsPage(driver, 'https://demoqa.com/text-box')
        text_box.open_page()
        text_box.text_box_page()
        driver.quit()


    def test_check_box(self, driver):
        check_box = ElementsPage(driver, 'https://demoqa.com/checkbox')
        check_box.open_page()
        check_box.check_box_page()
        driver.quit()


    def test_radio_button(self, driver):
        radio_button = ElementsPage(driver, 'https://demoqa.com/radio-button')
        radio_button.open_page()
        radio_button.radio_button_page()
        driver.quit()


    def test_web_tables(self, driver):
        web_tables = ElementsPage(driver, 'https://demoqa.com/webtables')
        web_tables.open_page()
        web_tables.web_tables_page()
        driver.quit()


    def test_buttons_click(self, driver):
        buttons_click = ElementsPage(driver, 'https://demoqa.com/buttons')
        buttons_click.open_page()
        buttons_click.buttons_click_page()
        driver.quit()


    def test_links(self, driver):
        links = ElementsPage(driver, 'https://demoqa.com/links')
        links.open_page()
        links.links_page()
        driver.quit()


    def test_links_response(self, driver):
        links = ElementsPage(driver, 'https://demoqa.com/links')
        links.open_page()
        links.response_links_page()
        driver.quit()


    def test_upload_file(self, driver):
        upload_file = ElementsPage(driver, 'https://demoqa.com/upload-download')
        upload_file.open_page()
        upload_file.up_down_load_file_page()
        driver.quit()


    def test_dynamic_properties(self, driver):
        dynamic_properties = ElementsPage(driver, 'https://demoqa.com/dynamic-properties')
        dynamic_properties.open_page()
        dynamic_properties.dynamic_properties_page()
        driver.quit()




















