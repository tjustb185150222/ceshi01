import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base_page import BasePage

'''
    核心元素：点击菜单栏学生列表，姓名输入框中输入查询条件，班级从下拉框中选择
    核心业务：实现菜单栏学生列表中的搜索功能
'''


class StudentSouSuo(BasePage):
    # 核心元素
    url = 'http://localhost:8090/system/index'
    name_0 = (By.XPATH, '//*[@id="nav"]/div[1]/div[2]/ul/li/div/a/span[2]')
    frame = (By.XPATH, '//*[@id="tabs"]/div[2]/div[2]/div/iframe')  # 切换iframe窗口
    # 通过Xpath定位输入路径，适用于教师和管理员
    name_1 = (By.XPATH, '//*[@id="toolbar"]/div[6]/span/input[1]')
    # 通过Xpath定位输入路径，适用于学生
    name_2 = (By.XPATH, '//*[@id="toolbar"]/div[3]/span/input[1]')
    kick_0 = (By.XPATH, '//*[@id="toolbar"]/div[7]/span/span/a')
    kick_1 = (By.ID, '_easyui_combobox_i3_0')
    button = (By.XPATH, '//*[@id="search-btn"]/span')
    text_0 = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[4]')

    # 核心业务
    def __init__(self, driver):
        super().__init__(driver)

    # 搜索功能的页面对象
    def SouSuo(self, name):
        self.visit(self.url)  # 初始化地址
        time.sleep(2)
        self.click(self.name_0)
        time.sleep(2)
        self.iframe(self.frame)
        self.input_(self.name_1, name)
        self.click(self.kick_0)
        self.click(self.kick_1)
        self.click(self.button)
        text_01 = self.tt(self.text_0)
        if name == text_01:
            print(name, '搜索功能成功')
        else:
            print('查询无果')


'''
if __name__ == '__main__':
    driver = webdriver.Chrome()
    sousuo = StudentSouSuo(driver)
    sousuo.SouSuo('测试3')
'''
