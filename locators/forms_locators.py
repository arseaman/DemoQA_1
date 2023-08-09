from selenium.webdriver.common.by import By


class FillFormLocators:
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id=firstName]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id=lastName]')
    EMAIL = (By.CSS_SELECTOR, 'input[ID=userEmail]')
    RADIO_BUTTON_MALE = (By.CSS_SELECTOR, 'label[for=gender-radio-1]')
    MOBILE_NUMBER = (By.CSS_SELECTOR, 'input[id=userNumber]')
    BIRTHDAY = (By.CSS_SELECTOR, 'input[id=dateOfBirthInput]')
    SUBJECTS = (By.CSS_SELECTOR, 'input[id=subjectsInput]')
    SPORT_CHECKBOX = (By.CSS_SELECTOR, 'label[for=hobbies-checkbox-1]')
    MUSIC_CHECKBOX = (By.CSS_SELECTOR, 'label[for=hobbies-checkbox-3]')
    UPLOAD_FILE = (By.CSS_SELECTOR, 'input[id=uploadPicture]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id=currentAddress]')
    SELECT_STATE = (By.CSS_SELECTOR, "div[id=state]")
    STATE_INPUT = (By.CSS_SELECTOR, "input[id=react-select-3-input]")
    SELECT_CITY = (By.CSS_SELECTOR, "div[id=city]")
    CITY_INPUT = (By.CSS_SELECTOR, "input[id=react-select-4-input]")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id=submit]')
    CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[id=closeLargeModal]')