from selenium import webdriver
from Page_Object import DiskPage
from Page_Object import LoginPage
from settings import *
import logging
import pytest
import time


LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()

    LOGGER.info('The browser opens on the main page')
    yandex_main_page = LoginPage(driver)

    LOGGER.info('The auth page opens')
    yandex_main_page.go_to_auth_page()

    # Установить параметр входа по почте

    LOGGER.info('Login entered')
    yandex_main_page.enter_login(os.environ["LOGIN"])

    LOGGER.info('The login button is pressed')
    yandex_main_page.click_on_the_login_button()

    LOGGER.info('Password entered')
    yandex_main_page.enter_password(os.environ["PASSWORD"])

    LOGGER.info('The login button is pressed')
    yandex_main_page.click_on_the_login_button()

    LOGGER.info('Authorization upload')
    time.sleep(3)

    LOGGER.info('Running autotests')
    yield driver

    LOGGER.info('Logging out of my account')
    yandex_main_page.log_out()

    LOGGER.info('Closing the browser')
    driver.quit()
