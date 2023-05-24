'''
    StudentLogin类,专门用于实现登录页面对象的文件
    主题内容包括：1、核心的页面元素：账号，密码，登录角色，登录按钮
               2、核心的业务源：用户的登录行为
'''
import time
from base.base_page import BasePage
from page_locators.login_page_locator import LoginPageLocator as login_page  # 导入该模块下的登录类，并通过 as 进行重命名进行引用


class StudentLogin(BasePage):
    '''核心业务'''

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password, type):
        # self.driver.maximize_window()
        self.visit(login_page.url)
        self.input_(login_page.username, username)
        self.input_(login_page.password, password)
        # 类型为1是管理员
        if type == 1:
            self.click(login_page.type_1)
        # 类型为2是学生
        if type == 2:
            self.click(login_page.type_3)
        # 类型为3是教师
        if type == 3:
            self.click(login_page.type_2)
        # self.click(self.type)
        self.click(login_page.button)
        time.sleep(1.5)

        getUrl = self.get_url()
        # print(getUrl)
        if getUrl == 'http://localhost:8090/system/index':
            text03 = self.tt(login_page.text01)
            # print(text03)
            # self.assertEqual(username, text03)
            if text03 == 'admin':
                # print("登陆成功")
                self.save_img('E:\pycharmdata\ceshi01\img\学生管理系统登录功能成功.png')
        if getUrl != 'http://localhost:8090/system/index':
            text04 = self.tt(login_page.text02)
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
