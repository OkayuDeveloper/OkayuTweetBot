from apscheduler.schedulers.background import BackgroundScheduler
from plugins.twitter.notification.tweetUtils import getProcess

def scheduling():
    sch = BackgroundScheduler()
    sch.add_job(getProcess, 'interval', minutes=15, id = 'gettingTweet')
    sch.start()
