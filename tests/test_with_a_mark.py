from Page_Object import DiskPage
import logging
import pytest


LOGGER = logging.getLogger(__name__)


# @pytest.mark.usefixtures("auth")
def test_with_a_mark(driver):
    # Authorization
    LOGGER.info('Precondition - authorization')
    yandex_main_page = DiskPage(driver)

    # Work with Yandex disk
    LOGGER.info('The yandex disk page opens')
    yandex_main_page.go_to_yandex_disk_page()

    LOGGER.info('Creating a folder and a name for this folder')
    yandex_main_page.create_a_new_folder()

    LOGGER.info('Opening a new folder')
    yandex_main_page.double_click_on_the_folder_for_txt_file()

    LOGGER.info('Downloading a txt file from the project directory')
    yandex_main_page.load_txt_file()

    LOGGER.info('Opening an inserted text file')
    yandex_main_page.open_file()

    web_file_content, my_file_content = yandex_main_page.compare_files()
    assert web_file_content == my_file_content

    LOGGER.info('Go back to the page where you can log out of your profile')
    yandex_main_page.go_to_yandex_disk_page()
