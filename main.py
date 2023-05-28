"""
# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
"""
import os.path

from BeautifulReport.BeautifulReport import BeautifulReport

"""
生成测试报告，这里我们使用的是BeautifulReport模块，需要先安装该模块。pip install BeautifulReport
"""
# coding = utf-8
import unittest

from common.log import log_init

log_init()  # 初始化日志文件
'''整合所有测试用例'''
discover = unittest.defaultTestLoader.discover('test_cases', pattern='test_case_*.py', top_level_dir=None)
'''
runner = unittest.TextTestRunner()
runner.run(discover)
'''
'''
输出测试报告
'''
base_path = os.path.dirname(__file__)  # 获取当前文件路径的上上层路径E:\pycharmdata\ceshi01
report = os.path.join(base_path, 'report')  # 拼接report目录的绝对路径E:\pycharmdata\ceshi01\report
# filename = os.path.join(report, 'report.html')  # 拼接路径与文件名称
report01 = BeautifulReport(discover)  # 执行测试用例集合并进行测试报告的输出
'''
report01.report(description='学生成绩管理系统测试报告', filename='ceshi.html', report_dir=r'E:\pycharmdata\ceshi01\report', theme='theme_cyan')
'''
report01.report(description='学生成绩管理系统测试报告', filename='学生成绩管理系统测试报告.html', report_dir=report, theme='theme_cyan')


