import logging
import random
import time
import unittest

from ddt import ddt, file_data, data, unpack
from selenium import webdriver
from page_objects.AddStudent import AddStudent
from page_objects.Delete_Student import DeleteStudent
from page_objects.Student_SouSuo import StudentSouSuo
from page_objects.Student_login import StudentLogin
from page_objects.Update_Student import UpdateStudent


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
        cls.deleteStudent = DeleteStudent(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 登陆功能测试用例执行
    @file_data('../data/user.yaml')
    def test_1_login(self, username, password, type):
        """
        学生成绩管理系统--登录功能
        :param username: 用户名
        :param password: 密码
        :param type: 用户类型（1为管理员，2为学生，3为教师）
        """
        log = logging.getLogger('main.test_case')
        log.info('输入用户名{}，密码{}，管理人员类型{}'.format(username, password, type))
        self.login.login(username, password, type)
        time.sleep(3)
        # self.sousuo.SouSuo('测试3')

    # 学生信息管理-学生列表-搜索功能测试用例执行
    @data('测试')
    def test_2_sousuo(self, txt):
        """
        学生成绩管理系统-学生信息管理-学生列表-搜索功能（搜索条件是姓名、班级（此处默认班级是软件一班））
         :param txt 搜索数据
        """
        log = logging.getLogger('main.test_cases')
        self.sousuo.SouSuo(txt)
        try:
            self.assertIn(txt, '测试', '搜索功能成功')
            log.info('搜索条件姓名输入框中输入{}'.format(txt))
        except Exception as e:
            # print('搜索功能失败，输出错误信息', e)
            log.info('输出错误信息{}'.format(e))
        time.sleep(5)

    # 学生信息管理-学生列表-添加功能测试用例执行
    def test_3_addStudent(self):
        """
        学生成绩管理系统-学生信息管理-学生列表-添加功能（输入姓名，密码，性别（默认男），电话，QQ号码，学生头像））
        """
        username = '测试添加' + str(random.randint(1, 100))
        password = 123456
        phone = 15235689564
        qq = 2558465236
        text = self.addStudent.addSudent(username, password, phone, qq)
        try:
            self.assertEqual('保存成功', text)
        except ZeroDivisionError as e:
            print("学生信息管理-学生列表-添加功能错误信息：", e)
        time.sleep(2)

    # 学生信息管理-学生列表-修改功能测试用例执行
    @data('测试修改')
    def test_4_updateStudent(self,username):
        """
        学生成绩管理系统-学生信息管理-学生列表-修改功能（修改姓名）
        :param username:修改姓名数据
        """
        username_ = username + str(random.randint(1, 100))  # 字符串拼接（+），random.randint(a,b):生成a到b之间的一个整数
        text_1 = self.updateStudent.updateStudent(username_, 18523454563, 2558546356)
        try:
            self.assertEqual('修改成功', text_1)
            print('修改功能成功')
        except ZeroDivisionError as e:
            print("学生信息管理-学生列表-修改功能错误信息：", e)
        time.sleep(5)

    # 学生信息管理-学生列表-删除功能测试用例执行
    def test_5_deleteStudent(self):
        """
        学生成绩管理系统-学生信息管理-学生列表-删除功能（删除第一条数据）
        """
        log = logging.getLogger('main.Delete_Student')
        text, text_1 = self.deleteStudent.deleteStudent()
        try:
            self.assertEqual("全部删除成功", text_1)
            log.info('删除姓名为{}的数据'.format(text))
        except Exception as e:
            log.info('输出错误信息{}'.format(e))
        time.sleep(5)


'''
if __name__ == '__main__':
    unittest.main()
'''

