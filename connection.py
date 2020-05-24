# -*- coding: UTF-8 -*-
import nonebot
import config
from os import path


'''

nonebot封装的CQHTTP插件

'''


if __name__ == "__main__":
    nonebot.init(config)
    nonebot.load_builtin_plugins()
    nonebot.load_plugins(path.join(path.dirname(__file__), 'plugins'), 'plugins')
    nonebot.run(host='127.0.0.1', port = 8087)
