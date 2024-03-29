from Page_Object import DiskPage
import logging
import pytest


LOGGER = logging.getLogger(__name__)


# @pytest.mark.usefixtures("auth")
def test_copying_files(driver):
    # Authorization
    LOGGER.info('Precondition - authorization')
    yandex_main_page = DiskPage(driver)

    # Work with Yandex disk
    LOGGER.info('The yandex disk page opens')
    yandex_main_page.go_to_yandex_disk_page()

    LOGGER.info('Left-click on the file to copy')
    yandex_main_page.left_click_on_the_file()

    LOGGER.info('Click on the "copy" method')
    yandex_main_page.click_on_the_copy_button()

    LOGGER.info('The necessary folder for copying has been selected')
    yandex_main_page.select_a_folder()

    LOGGER.info('Copied to the selected file')
    yandex_main_page.click_copy()

    LOGGER.info('Double tap to open the file')
    yandex_main_page.double_click_on_the_folder()

    LOGGER.info('Getting web elements of files to delete')
    yandex_main_page.delete_files()

    expected_result = yandex_main_page.checking_the_expected_result()
    assert len(expected_result) == 1
    assert expected_result[0].get_attribute("aria-label") == "Файл для копирования.docx"
