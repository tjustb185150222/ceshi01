import os
import logging
from config.Config import log_cfg
from logging.handlers import TimedRotatingFileHandler

'''
引入logging库，把项目的根路径取出来，把config.ini中的日志配置取过来，最后拼接好日志文件存放的绝对路径
'''
# 获取指定文件的完整路径、os.path.dirname获取当前文件的上上层文件夹的路径
_BaseHome = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# 将读取到的日志级别通过eval()函数转化为logging对象
_log_level = eval(log_cfg['log_level']) # 读取日志级别
_log_path = log_cfg['log_path']         # 读取保存的日志文件
_log_format = log_cfg['log_format']     # 读取其他相应信息

# os.path.join()函数用于路径拼接文件路径，可以传入多个路径
_log_file = os.path.join(_BaseHome, _log_path, 'log.txt')

'''
配置日志，引入TimedRotatingFileHandler，实现滚动日志
'''


def log_init():
    logger = logging.getLogger('main')
    logger.setLevel(level=_log_level)
    formatter = logging.Formatter(_log_format)

    handler = TimedRotatingFileHandler(filename=_log_file, when="D", interval=1, backupCount=7)
    handler.setLevel(_log_level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    console = logging.StreamHandler()
    console.setLevel(_log_level)
    console.setFormatter(formatter)
    logger.addHandler(console)


'''
其它文件使用日志：

先在main.py里面引入这个log_init()，在最开始的时候初始化一下，日志就配置好了。

再在各个要使用日志的文件中，直接按下面这种方式使用：
import logging
logger = logging.getLogger('main.jd')
注意各个模块自己getLogger的时候，直接main后面加上“.模块名”，就能使用同一个logger区分模块了。
'''
'''
# 验证一下日志效果
log_init()
logger = logging.getLogger('main')
logger.info('Log test----------')
'''
