import pytest
from selenium import webdriver


desiredCapabilities={
"browserName":"chrome"
}

@pytest.fixture()
def driver():
    driver = webdriver.Remote(command_executor='http://192.168.0.107:4444/wd/hub', desired_capabilities = desiredCapabilities)
    driver.maximize_window()
    yield driver
    driver.quit()

