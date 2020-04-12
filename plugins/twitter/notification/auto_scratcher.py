import nonebot
from aiocqhttp.exceptions import Error as CQHttpError
import plugins.twitter.notification.tweetUtils as utils
from plugins.management.management import valid_group

@nonebot.scheduler.scheduled_job('interval', minutes = 15, replace_existing=True)
async def readUpdate():
    bot = nonebot.get_bot()
    updateTweetList, oldTweetList = utils.readProcess()
    if updateTweetList.tList:
        for t in updateTweetList.tList :
            await bot.send_group_msg(group_id = valid_group, message = str(t))
    pass