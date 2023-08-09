import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
