import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage


class AddStudent(BasePage):
    url = 'http://localhost:8090/system/index'
    name_1 = (By.XPATH, '//*[@id="nav"]/div[1]/div[2]/ul/li/div/a/span[2]')  # 定位学生列表的菜单
    frame = (By.XPATH, '//*[@id="tabs"]/div[2]/div[2]/div/iframe')  # 定位iframe
    add = (By.XPATH, '//*[@id="add"]/span/span[1]')  # 定位添加按钮
    name_2 = (By.XPATH, '//*[@id="addForm"]/table/tbody/tr[1]/td[2]/span/input[1]')  # 定位姓名输入框位置
    password = (By.XPATH, '//*[@id="addForm"]/table/tbody/tr[2]/td[2]/span/input[1]')  # 定位密码输入框位置
    click_0 = (By.XPATH, '//*[@id="addForm"]/table/tbody/tr[3]/td[2]/span/span/a')  # 定位点击下拉框的下拉按钮
    click_1 = (By.XPATH, '//*[@id="_easyui_combobox_i1_0"]')  # 定位下拉框数据：i1_0为男，i1_1为女
    phone = (By.XPATH, '//*[@id="addForm"]/table/tbody/tr[4]/td[2]/span/input[1]')  # 定位手机号码输入框的位置
    qq = (By.XPATH ,'//*[@id="addForm"]/table/tbody/tr[5]/td[2]/span/input[1]')  # 定位qq输入框的位置
    click_2 = (By.XPATH, '//*[@id="addForm"]/table/tbody/tr[6]/td[2]/span/span/a')  # 定位班级下拉框数据的下拉按钮的位置
    click_3 = (By.XPATH, '//*[@id="_easyui_combobox_i6_0"]')  # 定位下拉框数据，此处数据为：软件一班
    file = (By.XPATH, '//*[@id="addForm"]/table/tbody/tr[7]/td[2]/input')  # 定位上传头像图片的位置
    add_button = (By.XPATH, '/html/body/div[7]/div[3]/a[1]/span')  # 定位添加按钮的位置
    success = (By.XPATH, '/html/body/div[13]/div[2]/div[2]')  # 定位“保存成功”的信息内容
    Ok = (By.XPATH, '/html/body/div[13]/div[2]/div[4]/a')  # 定位弹出保存成功的Ok按钮的位置

    def __init__(self, driver):
        super().__init__(driver)

    def addSudent(self, username, password, phone, qq):
        self.visit(self.url)
        self.click(self.name_1)
        self.iframe(self.frame)
        self.click(self.add)
        self.click(self.name_2)  #先将默认的username清除
        self.input_(self.name_2, username)
        self.input_(self.password, password)
        self.click(self.click_0)
        self.click(self.click_1)
        self.input_(self.phone, phone)
        self.input_(self.qq, qq)
        self.click(self.click_2)
        self.click(self.click_3)
        self.input_(self.file, 'E:\pycharmdata\ceshi01\img\学生管理系统登录功能成功.png')
        self.click(self.add_button)
        text = self.tt(self.success)
        time.sleep(2)
        self.click(self.Ok)
        return text



