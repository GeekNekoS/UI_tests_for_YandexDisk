import os
import time
import pyautogui
from locators import *
from Base_Page import BaseClass
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class LoginPage(BaseClass):
    # Log in
    def enter_login(self, login):
        return self.find_element(LoginLocators.LOGIN_INPUT, time=self.time).send_keys(login)

    def enter_password(self, password):
        return self.find_element(LoginLocators.PASSWORD_INPUT, time=self.time).send_keys(password)

    def click_on_the_login_button(self):
        return self.find_element(LoginLocators.LOGIN_BUTTON, time=self.time).click()

    # Log out
    def log_out(self):
        self.find_element(LoginLocators.LOG_OUT, time=self.time).click()
        return self.find_element(LoginLocators.LOG_OUT_BUTTON, time=self.time).click()


class DiskPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.window_handles = None

    def left_click_on_the_file(self):
        action = ActionChains(self.driver)
        button = self.find_element(DiskLocators.FILE, time=self.time)
        action.context_click(button).perform()

    def click_on_the_copy_button(self):
        return self.find_element(DiskLocators.COPY_BUTTON, time=self.time).click()

    def select_a_folder(self):
        return self.find_element(DiskLocators.FOLDER_SELECT, time=self.time).click()

    def click_copy(self):
        return self.find_element(DiskLocators.COPY_BUTTON_ON_POP_UP, time=self.time).click()

    def double_click_on_the_folder(self):
        action = ActionChains(self.driver)
        button = self.find_element(DiskLocators.FOLDER, time=self.time)
        action.double_click(button).perform()

    def delete_files(self):
        action = ActionChains(self.driver)
        files = self.find_elements(DiskLocators.FILES, time=self.time)
        copied_file = self.find_element(DiskLocators.COPIED_FILE, time=self.time)
        while copied_file not in files:
            files = self.find_elements(DiskLocators.FILES, time=self.time)

        for file in files:
            if file.get_attribute("aria-label") != "Файл для копирования.docx":
                action.context_click(file).perform()
                self.find_element(DiskLocators.DELETE, time=self.time).click()

    def checking_the_expected_result(self):
        return self.find_elements(DiskLocators.FILES, time=self.time)

    def create_a_new_folder(self):
        action = ActionChains(self.driver)
        screen = self.find_element(DiskLocators.SCREEN, time=self.time)
        action.context_click(screen).perform()

        self.find_element(DiskLocators.NEW_FOLDER, time=self.time).click()
        self.find_element(DiskLocators.INPUT_NEW_FOLDERS_NAME, time=self.time).send_keys(" для текстового файла")
        self.find_element(DiskLocators.NEW_FOLDERS_NAME, time=self.time).send_keys(Keys.RETURN)
        self.find_element(DiskLocators.THE_CROSS, time=self.time).click()

    def double_click_on_the_folder_for_txt_file(self):
        action = ActionChains(self.driver)
        button = self.find_element(DiskLocators.FOLDER_FOR_TXT, time=self.time)
        action.double_click(button).perform()

    def load_txt_file(self):
        action = ActionChains(self.driver)
        screen = self.find_element(DiskLocators.SCREEN, time=self.time)
        action.context_click(screen).perform()

        self.find_element(DiskLocators.FILE_UPLOAD, time=self.time).click()
        time.sleep(1)  # Для корректного открытия окна загрузки файлов
        pyautogui.write(os.getcwd() + "\My_file.txt", interval=0.005)
        pyautogui.press('return')
        time.sleep(3)  # Для ожидания загрузки файла

    def open_file(self):
        action = ActionChains(self.driver)
        screen = self.find_element(DiskLocators.MY_FILE, time=self.time)
        return action.double_click(screen).perform()

    def compare_files(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

        web_file = self.find_elements(DiskLocators.WEB_FILE_CONTENT, time=self.time)
        web_file_content = [line.text for line in web_file]

        with open("My_file.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            my_file_content = [line.rstrip() for line in lines]

        return web_file_content, my_file_content
