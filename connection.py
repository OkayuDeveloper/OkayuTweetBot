# -*- coding: UTF-8 -*-
import nonebot
from os import path
#配置
import config
#日志输出
from helper import getlogger
logger = getlogger('START')

'''

nonebot封装的CQHTTP插件

'''

if __name__ == "__main__":
    logger.info('启动nonebot...')
    nonebot.init(config)
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'plugins'),
        'plugins'
    )
    nonebot.run()
