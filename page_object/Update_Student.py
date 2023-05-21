import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from page_object.AddStudent import AddStudent


class UpdateStudent(BasePage):
    url = 'http://localhost:8090/system/index#'
    click_0 = (By.XPATH, '//*[@id="nav"]/div[1]/div[2]/ul/li/div/a')  # 定位学生列表的菜单
    frame = (By.XPATH, '//*[@id="tabs"]/div[2]/div[2]/div/iframe')  # 定位iframe
    click_1 = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[1]/div/input')  # 定位选择第一条数据
    update = (By.XPATH, '//*[@id="edit"]/span')  # 定位修改按钮
    update_name = (By.XPATH, '//*[@id="editForm"]/table/tbody/tr[1]/td[2]/span/input[1]')  # 定位修改姓名的位置
    click_2 = (By.XPATH, '//*[@id="editForm"]/table/tbody/tr[2]/td[2]/span/span/a')  # 定位性别下拉框的下拉按钮
    click_3 = (By.XPATH, '//*[@id="_easyui_combobox_i2_0"]')  # 定位下拉框中数据：i2_0为男，i2_1为女
    phone = (By.XPATH, '//*[@id="editForm"]/table/tbody/tr[3]/td[2]/span/input[1]')  # 定位输入手机号码的位置
    qq = (By.XPATH, '//*[@id="editForm"]/table/tbody/tr[4]/td[2]/span/input[1]')  # 定位输入qq号码的位置
    click_4 = (By.XPATH, '//*[@id="editForm"]/table/tbody/tr[5]/td[2]/span/span/a')  # 定位班级下拉框数据的下拉按钮
    click_5 = (By.XPATH, '//*[@id="_easyui_combobox_i7_1"]')  # 定位下拉框中的数据，此处为“数学一班”
    update_tijiao = (By.XPATH, '/html/body/div[10]/div[3]/a[1]/span')  # 定位提交按钮
    success = (By.XPATH, '/html/body/div[13]/div[2]/div[2]')  # 定位“修改成功”信息内容的位置
    Ok = (By.XPATH, '/html/body/div[13]/div[2]/div[4]/a')  # 定Ok点击按钮的位置

    def updateStudent(self, username, phone, qq):
        self.visit(self.url)
        self.click(self.click_0)
        self.iframe(self.frame)
        self.click(self.click_1)
        self.click(self.update)
        self.clear(self.update_name)
        self.input_(self.update_name, username)
        self.click(self.click_2)
        self.click(self.click_3)
        self.clear(self.phone)
        self.input_(self.phone, phone)
        self.clear(self.qq)
        self.input_(self.qq, qq)
        self.click(self.click_4)
        self.click(self.click_5)
        self.click(self.update_tijiao)
        text = self.tt(self.success)
        self.click(self.Ok)
        time.sleep(5)
        return text


