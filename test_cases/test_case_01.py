import random
import time
import unittest

from ddt import ddt, file_data, data, unpack
from selenium import webdriver

from page_object.AddStudent import AddStudent
from page_object.Student_SouSuo import StudentSouSuo
from page_object.Student_login import StudentLogin
from page_object.Update_Student import UpdateStudent


# 登录测试用例的设计



@ddt
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.login = StudentLogin(cls.driver)
        cls.sousuo = StudentSouSuo(cls.driver)
        cls.addStudent = AddStudent(cls.driver)
        cls.updateStudent = UpdateStudent(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 登陆功能测试用例执行
    @file_data('../data/user.yaml')
    def test_1_login(self, username, password, type):
        self.login.login(username, password, type)
        time.sleep(3)
        # self.sousuo.SouSuo('测试3')

    # 学生信息管理-学生列表-搜索功能测试用例执行
    @data('测试3', '张一泽', '张三纷')
    def test_2_sousuo(self, txt):
        self.sousuo.SouSuo(txt)
        time.sleep(5)

    # 学生信息管理-学生列表-添加功能测试用例执行
    def test_3_addStudent(self):
        username = '测试添加' + str(random.randint(1, 100))
        password = 123456
        phone = 15235689564
        qq = 2558465236
        text =self.addStudent.addSudent(username, password, phone, qq)
        try:
            self.assertEqual('保存成功', text)
            print("添加成功")
        except ZeroDivisionError as e:
            print("学生信息管理-学生列表-添加功能错误信息：", e)
        time.sleep(2)

    # 学生信息管理-学生列表-修改功能测试用例执行
    def test_4_updateStudent(self):
        username = '测试修改' + str(random.randint(1, 100))  # 字符串拼接（+），random.randint(a,b):生成a到b之间的一个整数
        text_1 = self.updateStudent.updateStudent(username, 18523454563, 2558546356)
        try:
            self.assertEqual('修改成功', text_1)
            print('修改功能成功')
        except ZeroDivisionError as e:
            print("学生信息管理-学生列表-修改功能错误信息：", e)
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
