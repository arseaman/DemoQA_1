import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture()
def driver():
    options = ChromeOptions()
    options.browser_version = '119.0.6045.160'
    options.platform_name = 'Ubuntu'
    cloud_options = {
        'build': 'my_test_build',
        'name': 'my_test_name'
    }
    options.add_experimental_option('w3c', True)
    options.add_experimental_option('cloud:options', cloud_options)
    cloud_url = 'http://54.174.220.59:4444/wd/hub'
    driver = webdriver.Remote(cloud_url, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

