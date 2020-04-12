import threading
import tweetUtils as utils
import time
#import CQHTTP
import traceback
import request
import nonebot
from plugins.management.management import valid_group
#使用独立线程Timer进行延时
#请先执行本脚本再打开Connection
#Connection的获取定时使用ASP做的 不知道好不好用
#反正ASP定时获取 似乎不太行


#主运行函数
def timerMonitor():
    #主函数
    bot = nonebot.get_bot()
    #ifdone = utils.getProcess()
    update, old = utils.automation()
    #返回运行状态
    #print("Done: ",ifdone)
    if updateList.tList:
        try:
            for item in updateList.tList:
                bot.send_group_msg(group_id = valid_group, message = str(item))
        except:
            traceback.print_exc()
    #循环调用Timer 当前时间:120s
    timer = threading.Timer(3000,timerMonitor)
    #开始计时
    timer.start()

#脚本入口
timer = threading.Timer(1,timerMonitor)
print("StartLoop")
timer.start()
