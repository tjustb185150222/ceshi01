from selenium.webdriver.common.by import By


class DeleteStudentPageLocator():
    # 核心元素
    url = 'http://localhost:8090/system/index#'
    click_0 = (By.XPATH, '//*[@id="nav"]/div[1]/div[2]/ul/li/div/a')  # 定位学生列表的菜单
    frame = (By.XPATH, '//*[@id="tabs"]/div[2]/div[2]/div/iframe')  # 定位iframe
    click_1 = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[1]/div/input')  # 定位选择第一条数据
    name = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[4]/div')  # 定位第一条数据的姓名的位置
    text = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[4]/div')  # 定位第一条数据的姓名的位置
    delete_button = (By.XPATH, '//*[@id="delete"]/span/span[1]')  # 定位删除按钮  将删除与学生相关的所有数据(包括成绩)，确认继续？
    text_0 = (By.XPATH, '/html/body/div[13]/div[2]/div[2]')  # 定位消息提醒信息位置
    Ok = (By.XPATH, '/html/body/div[13]/div[2]/div[4]/a[1]')  # 定位消息提醒的OK按钮
    text_1 = (By.XPATH, '/html/body/div[13]/div[2]/div[2]')  # 定位再次确认删除的消息提醒内容信息的位置
    Ok_0 = (By.XPATH, '/html/body/div[13]/div[2]/div[4]/a')  # 定位消息提醒的Ok按钮的位置