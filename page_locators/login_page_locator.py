from selenium.webdriver.common.by import By

#  存放登录功能页面元素位置定位信息
#  对应的登录功能页面对象通过导入该模块下的类，并进行重命名
#
'''
创建login_page_locator.py模块定义login页面的定位信息为类属性
'''


class LoginPageLocator():
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
