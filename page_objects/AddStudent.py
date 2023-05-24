import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage
from page_locators.addstudent_page_locator import AddStudentPageLocator as addStudentLocator


class AddStudent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def addSudent(self, username, password, phone, qq):
        self.visit(addStudentLocator.url)
        self.click(addStudentLocator.name_1)
        self.iframe(addStudentLocator.frame)
        self.click(addStudentLocator.add)
        self.click(addStudentLocator.name_2)  #先将默认的username清除
        self.input_(addStudentLocator.name_2, username)
        self.input_(addStudentLocator.password, password)
        self.click(addStudentLocator.click_0)
        self.click(addStudentLocator.click_1)
        self.input_(addStudentLocator.phone, phone)
        self.input_(addStudentLocator.qq, qq)
        self.click(addStudentLocator.click_2)
        self.click(addStudentLocator.click_3)
        self.input_(addStudentLocator.file, 'E:\pycharmdata\ceshi01\img\学生管理系统登录功能成功.png')
        self.click(addStudentLocator.add_button)
        text = self.tt(addStudentLocator.success)
        time.sleep(2)
        self.click(addStudentLocator.Ok)
        return text



