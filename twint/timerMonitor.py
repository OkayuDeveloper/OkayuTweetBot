# -*- coding: UTF-8 -*-

import threading
import time
#import CQHTTP
import traceback
#import request
#import nonebot
import sys
from os import path
d = path.dirname(__file__)
parent_path = path.dirname(d)
print(sys.path)
sys.path.append(parent_path)

from plugins.management.management import valid_group
import plugins.twitter.notification.tweetUtils as utils
#使用独立线程Timer进行延时
#请先执行本脚本再打开Connection
#Connection的获取定时使用ASP做的 不知道好不好用
#反正ASP定时获取 似乎不太行


#主运行函数
def timerMonitor():
    #主函数
    ifget = utils.getProcess()
    #返回运行状态
    print("Done: ",ifget)
    #循环调用Timer 当前时间:120s
    timer = threading.Timer(750,timerMonitor)
    #开始计时
    timer.start()

#脚本入口
timer = threading.Timer(1,timerMonitor)
print("StartLoop")
timer.start()
