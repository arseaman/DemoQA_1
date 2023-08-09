from selenium.webdriver.common.by import By

class TextBoxLocators:
    FULL_NAME_INPUT = (By.CSS_SELECTOR, 'input[id=userName]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id=userEmail]')
    CURRENT_ADRESS_INPUT = (By.CSS_SELECTOR, 'textarea[id=currentAddress]')
    PERMAMENT_ADRESS_INPUT = (By.CSS_SELECTOR, 'textarea[id=permanentAddress]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id=submit]')

class CheckBoxLocators:
    FIRST_DOWN_ARROW = (By.CSS_SELECTOR, "button[title='Toggle']")
    DOCUMENTS_CHECKBOX = (By.XPATH, "//span[@class='rct-title'and text()='Documents']")
    COLLAPSE_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Collapse all']")
    ASSERT = (By.XPATH, "//*[text()='documents']")

class RadioButtonLocators:
    YES = (By.CSS_SELECTOR, ' label[for=yesRadio]')
    DISPLAY_YES = (By.CSS_SELECTOR, "span[class=text-success]")
    IMPRESSIVE = (By.CSS_SELECTOR, 'label[for=impressiveRadio]')
    DISPLAY_IMPRESSIVE = (By.CSS_SELECTOR, 'span[class=text-success]')

class WebTablesLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id=addNewRecordButton]")
    FORM_FIRST_NAME = (By.CSS_SELECTOR, "input[id=firstName]")
    FORM_LAST_NAME = (By.CSS_SELECTOR, "input[id=lastName]")
    FORM_EMAIL = (By.CSS_SELECTOR, "input[id=userEmail]")
    FORM_AGE = (By.CSS_SELECTOR, "input[id=age]")
    FORM_SALARY = (By.CSS_SELECTOR, "input[id=salary]")
    FORM_DEPARTMENT = (By.CSS_SELECTOR, "input[id=department]")
    FORM_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id=submit]")

class ButtonsClickLocators:
    DOUBLE_CLICK_ME = (By.CSS_SELECTOR, 'button[id=doubleClickBtn]')
    RIGHT_CLICK_ME = (By.CSS_SELECTOR, 'button[id=rightClickBtn]')
    CLICK_ME = (By.XPATH, "//*[text()='Click Me']")
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id=doubleClickMessage]')
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id=rightClickMessage]')
    CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id=dynamicClickMessage]')

class LinksLocators:
    HOME_LINK = (By.CSS_SELECTOR, 'a[id=simpleLink]')
    LOAD_LOCATOR = (By.CSS_SELECTOR, 'div[class=category-cards]')

class LinksResponseLocators:
    CREATED_LINK = (By.CSS_SELECTOR, "a[id=created]")
    CREATED_STATUS = (By.XPATH, "//*[@id='linkResponse']/child::b[1]")
    CREATED_TEXT = (By.XPATH, "//*[@id='linkResponse']/child::b[2]")
    NO_CONTENT_LINK = (By.CSS_SELECTOR, "a[id=no-content]")
    NO_CONTENT_STATUS = (By.XPATH, "//*[@id='linkResponse']/child::b[1]")
    NO_CONTENT_TEXT = (By.XPATH, "//*[@id='linkResponse']/child::b[2]")
    MOVED_LINK = (By.CSS_SELECTOR, "a[id=moved]")
    MOVED_STATUS = (By.XPATH, "//*[@id='linkResponse']/child::b[1]")
    MOVED_TEXT = (By.XPATH, "//*[@id='linkResponse']/child::b[2]")
    BAD_REQUEST_LINK = (By.CSS_SELECTOR, "a[id=bad-request]")
    BAD_REQUEST_STATUS = (By.XPATH, "//*[@id='linkResponse']/child::b[1]")
    BAD_REQUEST_TEXT = (By.XPATH, "//*[@id='linkResponse']/child::b[2]")
    UNAUTHORIZED_LINK = (By.CSS_SELECTOR, "a[id=unauthorized]")
    UNAUTHORIZED_STATUS = (By.XPATH, "//*[@id='linkResponse']/child::b[1]")
    UNAUTHORIZED_TEXT = (By.XPATH, "//*[@id='linkResponse']/child::b[2]")
    FORBIDDEN_LINK = (By.CSS_SELECTOR, "a[id=forbidden]")
    FORBIDDEN_STATUS = (By.XPATH, "//*[@id='linkResponse']/child::b[1]")
    FORBIDDEN_TEXT = (By.XPATH, "//*[@id='linkResponse']/child::b[2]")
    NOT_FOUND_LINK = (By.CSS_SELECTOR, "a[id=invalid-url]")
    NOT_FOUND_STATUS = (By.XPATH, "//*[@id='linkResponse']/child::b[1]")
    NOT_FOUND_TEXT = (By.XPATH, "//*[@id='linkResponse']/child::b[2]")

class UpDownloadLocators:
    UPLOAD_FILE = (By.CSS_SELECTOR, 'input[id=uploadFile]')
    UPLOAD_MESSAGE = (By.CSS_SELECTOR, 'p[id=uploadedFilePath]')
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, 'a[id=downloadButton]')

class DynamicPropertiesLocators:
    WILL_ENABLE = (By.CSS_SELECTOR, 'button[id=enableAfter]')
    COLOR_CHANGE = (By.CSS_SELECTOR, 'button[id=colorChange]')
    VISIBLE_AFTER = (By.CSS_SELECTOR, 'button[id=visibleAfter]')










