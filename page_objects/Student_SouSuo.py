import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from page_locators.select_page_locator import SelectStudentPageLocator as selectStudent

'''
    核心元素：点击菜单栏学生列表，姓名输入框中输入查询条件，班级从下拉框中选择
    核心业务：实现菜单栏学生列表中的搜索功能
'''


class StudentSouSuo(BasePage):

    # 核心业务
    def __init__(self, driver):
        super().__init__(driver)

    # 搜索功能的页面对象
    def SouSuo(self, name):
        self.visit(selectStudent.url)  # 初始化地址
        time.sleep(2)
        self.click(selectStudent.name_0)
        time.sleep(2)
        self.iframe(selectStudent.frame)
        self.input_(selectStudent.name_1, name)
        self.click(selectStudent.kick_0)
        self.click(selectStudent.kick_1)
        self.click(selectStudent.button)
        time.sleep(2)
        text_01 = self.tt(selectStudent.text_0)
        return  text_01
        '''
        if name == text_01:
            print(name, '搜索功能成功')
        else:
            print('查询无果')
        '''




'''
if __name__ == '__main__':
    driver = webdriver.Chrome()
    sousuo = StudentSouSuo(driver)
    sousuo.SouSuo('测试3')
'''
