import time

def save_creen():
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))  # 获取当前时间
    pic_path = "../img" + now + '_screen.png'
