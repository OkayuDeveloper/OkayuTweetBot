import threading
import tweetUtils as utils

#使用独立线程Timer进行延时
#请先执行本脚本再打开Connection
#Connection的获取定时使用ASP做的 不知道好不好用
#反正ASP定时获取 似乎不太行


#主运行函数
def timerMonitor():
    #主函数
    ifdone = utils.getProcess()
    #返回运行状态
    print("Done: ",ifdone)
    #循环调用Timer 当前时间:120s
    timer = threading.Timer(120,timerMonitor)
    #开始计时
    timer.start()

#脚本入口
timer = threading.Timer(1,timerMonitor)
print("StartLoop")
timer.start()
