from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url


    def open_page(self):
        self.driver.get(self.url)


    def element_is_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))


    def elements_are_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))


    def element_is_present(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))


    def elements_are_presents(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))


    def text_presents_in_element(self, locators, text, timeout=10):
        return wait(self.driver, timeout).until(EC.text_to_be_present_in_element(locators, text))


    def element_is_clickable(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))


    def double_click(self, locator):
        action = ActionChains(self.driver)
        action.double_click(locator)
        action.perform()


    def right_click(self, locator):
        action = ActionChains(self.driver)
        action.context_click(locator)
        action.perform()


    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        # self.driver.execute_script("document.getElementsById('close-fixedban').remove();")
