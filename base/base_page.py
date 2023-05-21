'''
    BasePage类是POM中的基类，主要用于提供常用的函数，微页面对象进行操作服务
    Selenium常用函数
    元素定位
    输入
    点击
    访问url
    刷新
    等待
    跳转新页面窗口的定位
    弹出弹框的定位
    获取文本
    打印当前地址
    截图
    警告框中点击确定
    警告框中点击取消
    警告框中输入值
    下拉框中选择选项
    关闭
'''
from selenium.webdriver.support.select import Select


class BasePage:
    # 虚构driver对象

    # 构造函数
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    # 访问url
    def visit(self, url):
        self.driver.get(url)

    # 元素定位
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def input_(self, loc, txt):
        self.locator(loc).send_keys(txt)

    # 点击
    def click(self, loc):
        self.locator(loc).click()

    # 等待
    def wait_time(self, times):
        self.driver.implicitly_wait(times)

    # 定位新弹出的页面/窗口
    def window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    # 定位弹框
    def iframe(self, loc):
        self.driver.switch_to.frame(self.locator(loc))

    # 获取文本
    def tt(self, loc):
        return self.locator(loc).text

    # 打印当前地址
    def get_url(self):
        return self.driver.current_url

    # 截图
    def save_img(self, path):
        self.driver.get_screenshot_as_file(path)

    # 警告框中点击确定
    def alert_acc(self):
        self.driver.switch_to.alert.accept()

    # 警告框中点击取消
    def alert_dismiss(self):
        self.driver.switch_to.alert.dismiss()

    # 警告框中输入值
    def alert_input(self, value):
        self.driver.switch_to.send_keys(value)

    # 下拉框中选择选项（select）
    def select_option(self, value, loc):
        ele = self.locator(loc)
        if ele:
            Select(ele).select_by_value(value)


'''
 # 打印当前地址
    def timeUrl(self):
        self.driver.current_url
'''
