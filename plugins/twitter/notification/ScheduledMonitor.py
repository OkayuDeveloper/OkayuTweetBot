from apscheduler.schedulers.background import BackgroundScheduler
#from plugins.twitter.notification.tweetUtils import getProcess
import plugins.twitter.notification.tweetUtils


def scheduling():
    sch = BackgroundScheduler()
    sch.add_job(plugins.twitter.notification.tweetUtils.getProcess, 'interval', minutes=15, id = 'gettingTweet')
    sch.start()
