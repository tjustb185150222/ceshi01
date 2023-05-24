import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from page_locators.update_page_locator import UpdateStudentPageLocator as updateStudent


class UpdateStudent(BasePage):

    def updateStudent(self, username, phone, qq):
        self.visit(updateStudent.url)
        self.click(updateStudent.click_0)
        self.iframe(updateStudent.frame)
        self.click(updateStudent.click_1)
        self.click(updateStudent.update)
        self.clear(updateStudent.update_name)
        self.input_(updateStudent.update_name, username)
        self.click(updateStudent.click_2)
        self.click(updateStudent.click_3)
        self.clear(updateStudent.phone)
        self.input_(updateStudent.phone, phone)
        self.clear(updateStudent.qq)
        self.input_(updateStudent.qq, qq)
        self.click(updateStudent.click_4)
        self.click(updateStudent.click_5)
        self.click(updateStudent.update_tijiao)
        text = self.tt(updateStudent.success)
        self.click(updateStudent.Ok)
        time.sleep(5)
        return text


