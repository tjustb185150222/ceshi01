import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage
from page_objects.Update_Student import UpdateStudent
from page_locators.delete_page_locator import DeleteStudentPageLocator as deleteStudent


class DeleteStudent(BasePage):

    def deleteStudent(self):

        self.visit(deleteStudent.url)
        self.click(deleteStudent.click_0)
        self.iframe(deleteStudent.frame)
        self.click(deleteStudent.click_1)
        text = self.tt(deleteStudent.name)
        self.click(deleteStudent.delete_button)
        self.click(deleteStudent.Ok)
        text_2 = self.tt(deleteStudent.text_1)
        time.sleep(2)
        self.click(deleteStudent.Ok_0)

        return text_2


