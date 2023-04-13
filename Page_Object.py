import os
import time
import pyautogui
from Base_Page import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import logging


LOGGER = logging.getLogger(__name__)


class Locators:
    LOGIN_SETTINGS = (By.XPATH, "//span[text()='Почта']")
    LOGIN_INPUT = (By.XPATH, "//input[@placeholder='Логин или email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Введите пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[@id='passp:sign-in']")
    FILE = (By.XPATH, "//div[@aria-label='Файл для копирования.docx']")
    COPY_BUTTON = (By.XPATH, "//span[text()='Копировать']")
    FOLDER_SELECT = (By.XPATH, "//div[text()='Скопировать файл сюда!']")
    COPY_BUTTON_ON_POP_UP = (By.XPATH, "//button[@class='Button2 Button2_view_action Button2_size_m confirmation-dialog__button confirmation-dialog__button_submit ']")  #
    FOLDER = (By.XPATH, "//div[@aria-label='Скопировать файл сюда!']")
    FILES = (By.XPATH, "//div[@class='listing-item__title listing-item__title_overflow_clamp']")
    COPIED_FILE = (By.XPATH, "//div[@class='listing__items']/.//div[@aria-label='Файл для копирования.docx']")
    DELETE = (By.XPATH, "//span[text()='Удалить']")
    LOG_OUT = (By.XPATH, "//img[@class='user-pic__image']")
    #
    LOG_OUT_BUTTON = (By.XPATH, "//*[text()='Выйти']")  # //*[text()='Выйти']  # //span[text()='Выйти']

    SCREEN = (By.XPATH, "//div[@class='listing-item listing-item_theme_tile-empty listing-item_size_m']")
    NEW_FOLDER = (By.XPATH, "//span[text()='Новая папка']")
    INPUT_NEW_FOLDERS_NAME = (By.XPATH, "//input[@value='Новая папка']")
    NEW_FOLDERS_NAME = (By.XPATH, "//input[@value='Новая папка для текстового файла']")
    THE_CROSS = (By.XPATH, "//button[@aria-label='Отменить выделение']")
    FOLDER_FOR_TXT = (By.XPATH, "//div[@aria-label='Новая папка для текстового файла']")
    FILE_UPLOAD = (By.XPATH, "//span[text()='Загрузить файлы']")
    MY_FILE = (By.XPATH, "//div[@aria-label='My_file.txt']")
    WEB_FILE_CONTENT = (By.XPATH, "//div[@class='b1']/.//p/.")


class YandexDisk(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.window_handles = None

    def enter_login(self, login):
        return self.find_element(Locators.LOGIN_INPUT, time=self.time).send_keys(login)

    def enter_password(self, password):
        return self.find_element(Locators.PASSWORD_INPUT, time=self.time).send_keys(password)

    def click_on_the_login_button(self):
        return self.find_element(Locators.LOGIN_BUTTON, time=self.time).click()

    def left_click_on_the_file(self):
        action = ActionChains(self.driver)
        button = self.find_element(Locators.FILE, time=self.time)
        action.context_click(button).perform()

    def click_on_the_copy_button(self):
        return self.find_element(Locators.COPY_BUTTON, time=self.time).click()

    def select_a_folder(self):
        return self.find_element(Locators.FOLDER_SELECT, time=self.time).click()

    def click_copy(self):
        return self.find_element(Locators.COPY_BUTTON_ON_POP_UP, time=self.time).click()

    def double_click_on_the_folder(self):
        action = ActionChains(self.driver)
        button = self.find_element(Locators.FOLDER, time=self.time)
        action.double_click(button).perform()

    def delete_files(self):
        action = ActionChains(self.driver)
        files = self.find_elements(Locators.FILES, time=self.time)
        copied_file = self.find_element(Locators.COPIED_FILE, time=self.time)
        while copied_file not in files:
            files = self.find_elements(Locators.FILES, time=self.time)

        for file in files:
            if file.get_attribute("aria-label") != "Файл для копирования.docx":
                action.context_click(file).perform()
                self.find_element(Locators.DELETE, time=self.time).click()

    def checking_the_expected_result(self):
        return self.find_elements(Locators.FILES, time=self.time)

    def log_out(self):
        self.find_element(Locators.LOG_OUT, time=self.time).click()
        return self.find_element(Locators.LOG_OUT_BUTTON, time=self.time).click()

    def create_a_new_folder(self):
        action = ActionChains(self.driver)
        screen = self.find_element(Locators.SCREEN, time=self.time)
        action.context_click(screen).perform()

        self.find_element(Locators.NEW_FOLDER, time=self.time).click()
        self.find_element(Locators.INPUT_NEW_FOLDERS_NAME, time=self.time).send_keys(" для текстового файла")
        self.find_element(Locators.NEW_FOLDERS_NAME, time=self.time).send_keys(Keys.RETURN)
        self.find_element(Locators.THE_CROSS, time=self.time).click()

    def double_click_on_the_folder_for_txt_file(self):
        action = ActionChains(self.driver)
        button = self.find_element(Locators.FOLDER_FOR_TXT, time=self.time)
        action.double_click(button).perform()

    def load_txt_file(self):
        action = ActionChains(self.driver)
        screen = self.find_element(Locators.SCREEN, time=self.time)
        action.context_click(screen).perform()

        self.find_element(Locators.FILE_UPLOAD, time=self.time).click()
        time.sleep(1)  # Для корректного открытия окна для загрузки файлов
        pyautogui.write(os.getcwd() + "\My_file.txt", interval=0.005)
        pyautogui.press('return')
        time.sleep(3)  # Для ожидания загрузки файла

    def open_file(self):
        action = ActionChains(self.driver)
        screen = self.find_element(Locators.MY_FILE, time=self.time)
        return action.double_click(screen).perform()

        # time.sleep(3)  # Для прогрузки файла

    def compare_files(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

        web_file = self.find_elements(Locators.WEB_FILE_CONTENT, time=self.time)
        web_file_content = [line.text for line in web_file]

        with open("My_file.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            my_file_content = [line.rstrip() for line in lines]

        return web_file_content, my_file_content
