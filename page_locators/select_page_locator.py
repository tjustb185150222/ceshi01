from selenium.webdriver.common.by import By


class SelectStudentPageLocator():
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