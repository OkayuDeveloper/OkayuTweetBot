import os
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
import plugins.twitter.notification.monitor_auto as auto
import nonebot
from plugins.management.management import valid_group
valid_group = 1094163087

@nonebot.scheduler.scheduled_job('interval', minutes = 15, replace_existing=True)
async def autorun_monitor():
    bot = nonebot.get_bot()
    updateTweet, oldTweet = auto.main()
    if updateTweet.tList:
        for t in updateTweet.tList :
            await bot.send_group_msg(group_id = valid_group, message = str(t))
    else:
        await bot.send_group_msg(group_id = valid_group, message = "15-min Autorun Done.")
