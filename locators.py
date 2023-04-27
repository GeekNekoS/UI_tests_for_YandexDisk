from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_INPUT = (By.XPATH, "//input[@placeholder='Логин или email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Введите пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[@id='passp:sign-in']")
    LOG_OUT = (By.XPATH, "//img[@class='user-pic__image']")
    LOG_OUT_BUTTON = (By.XPATH, "//*[text()='Выйти']")


class DiskLocators:
    # for test_copying_file.py
    FILE = (By.XPATH, "//div[@aria-label='Файл для копирования.docx']")
    COPY_BUTTON = (By.XPATH, "//span[text()='Копировать']")
    FOLDER_SELECT = (By.XPATH, "//div[text()='Скопировать файл сюда!']")
    COPY_BUTTON_ON_POP_UP = (By.XPATH, "//button[@class='Button2 Button2_view_action Button2_size_m confirmation-dialog__button confirmation-dialog__button_submit ']")  #
    FOLDER = (By.XPATH, "//div[@aria-label='Скопировать файл сюда!']")
    FILES = (By.XPATH, "//div[@class='listing-item__title listing-item__title_overflow_clamp']")
    COPIED_FILE = (By.XPATH, "//div[@class='listing__items']/.//div[@aria-label='Файл для копирования.docx']")
    DELETE = (By.XPATH, "//span[text()='Удалить']")

    # for test_with_a_mark.py
    SCREEN = (By.XPATH, "//div[@class='listing-item listing-item_theme_tile-empty listing-item_size_m']")
    NEW_FOLDER = (By.XPATH, "//span[text()='Новая папка']")
    INPUT_NEW_FOLDERS_NAME = (By.XPATH, "//input[@value='Новая папка']")
    NEW_FOLDERS_NAME = (By.XPATH, "//input[@value='Новая папка для текстового файла']")
    THE_CROSS = (By.XPATH, "//button[@aria-label='Отменить выделение']")
    FOLDER_FOR_TXT = (By.XPATH, "//div[@aria-label='Новая папка для текстового файла']")
    FILE_UPLOAD = (By.XPATH, "//span[text()='Загрузить файлы']")
    MY_FILE = (By.XPATH, "//div[@aria-label='My_file.txt']")
    WEB_FILE_CONTENT = (By.XPATH, "//div[@class='b1']/.//p/.")
