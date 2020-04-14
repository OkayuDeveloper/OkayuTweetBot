# -*- coding: UTF-8 -*-
from plugins.management.management import valid_group
import nonebot
from plugins.twitter.notification.tweetUtils import readProcess
#import pytz
from aiocqhttp.exceptions import Error as CQHttpError


@nonebot.scheduler.scheduled_job('interval', seconds=750)
async def _():
    bot = nonebot.get_bot()
    #now = datetime.now(pytz.timezone('Asia/Shanghai'))
    updateTweetList, oldTweetList = readProcess()
    try:
        if updateTweetList:
            for t in updateTweetList.tList:
                await bot.send_group_msg(group_id=valid_group, message=str(t))
        else:
            # await bot.send_group_msg(group_id=valid_group, message="No Update")
    except CQHttpError:
        print("AUTO ERROR: ", CQHttpError.with_traceback())
