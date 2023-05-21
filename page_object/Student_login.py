'''
    StudentLogin类,专门用于实现登录页面对象的文件
    主题内容包括：1、核心的页面元素：账号，密码，登录角色，登录按钮
               2、核心的业务源：用户的登录行为
'''
import time
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class StudentLogin(BasePage):

    '''核心元素'''
    url = 'http://localhost:8090/'
    username = (By.ID, 'username')
    password = (By.ID, 'password')
    # 通过点击选择角色为管理员登录定位type=1
    type_1 = (By.CSS_SELECTOR, '#form > div.mt-20.skin-minimal > div:nth-child(3) > div > ins')
    # 通过点击选择角色为老师登录定位type=3
    type_2 = (By.CSS_SELECTOR, '#form > div.mt-20.skin-minimal > div:nth-child(2) > div > ins')
    # 通过点击选择角色为学生登录定位type=2
    type_3 = (By.CSS_SELECTOR, '#form > div.mt-20.skin-minimal > div:nth-child(1) > div > ins')
    # 确定按钮的ID
    button = (By.ID, 'submitBtn')
    # 登陆成功后对文本admin进行定位
    text01 = (By.XPATH, '//*[@id="tabs"]/div[2]/div/div/p[1]')
    # 登陆失败后对失败信息内容进行定位
    text02 = (By.XPATH, "/html/body/div[4]/div[2]/div[2]")

    '''核心业务'''

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password, type):
        # self.driver.maximize_window()
        self.visit(self.url)
        self.input_(self.username, username)
        self.input_(self.password, password)
        # 类型为1是管理员
        if type == 1:
            self.click(self.type_1)
        # 类型为2是学生
        if type == 2:
            self.click(self.type_3)
        # 类型为3是教师
        if type == 3:
            self.click(self.type_2)
        # self.click(self.type)
        self.click(self.button)
        time.sleep(1.5)

        getUrl = self.get_url()
        # print(getUrl)
        if getUrl =='http://localhost:8090/system/index':
            text03 = self.tt(self.text01)
            # print(text03)
            # self.assertEqual(username, text03)
            if text03 == 'admin':
                # print("登陆成功")
                self.save_img('E:\pycharmdata\ceshi01\img\学生管理系统登录功能成功.png')
        if getUrl != 'http://localhost:8090/system/index':
            text04 = self.tt(self.text02)
            if text04 == '用户名或密码错误':
                # print("登陆失败")
                self.save_img('E:\pycharmdata\ceshi01\img\学生管理系统登录功能失败.png')





'''调试代码'''
'''
if __name__ == '__main__':
    driver = webdriver.Chrome()
    login = StudentLogin(driver)
    login.login("admin", 123455)
'''


