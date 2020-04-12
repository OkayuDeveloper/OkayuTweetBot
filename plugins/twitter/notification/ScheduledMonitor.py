from apscheduler.schedulers.background import BackgroundScheduler
import traceback
#from plugins.twitter.notification.tweetUtils import getProcess
import tweetUtils

#或者把它也声明为异步的呢...？
#不知道能不能正确管理（现在处于一个没有返回值的情况）
def scheduling():
    sch = BackgroundScheduler()
    sch.add_job(tweetUtils.getProcess, 'interval', minutes=15, id = 'gettingTweet')
    sch.start()
#添加Traceback
try:
    scheduling()
except:
    traceback.print_exc()
