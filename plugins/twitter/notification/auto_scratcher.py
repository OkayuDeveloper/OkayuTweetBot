# -*- coding: UTF-8 -*-
from plugins.configure.configuration import *
import nonebot
from plugins.twitter.notification.tweetUtils import readProcess
#import pytz
from aiocqhttp.exceptions import Error as CQHttpError
import datetime

@nonebot.scheduler.scheduled_job('interval', seconds=300)
async def _():
    bot = nonebot.get_bot()
    #now = datetime.now(pytz.timezone('Asia/Shanghai'))
    updateTweetList, oldTweetList = readProcess()
    limit = 0
    try:
        if updateTweetList:
            for t in updateTweetList.tList:
                limit += 1
                get_tweet_time = datetime.datetime.strptime("{0} {1}".format(t.date,t.time),'%Y-%m-%d %H:%M:%S')
                get_current_time = datetime.datetime.now()
                gap = (get_current_time - get_tweet_time).seconds
                gap_minutes = gap // 60
                gap_seconds = gap - 60 * gap_minutes
                await bot.send_group_msg(group_id=valid_group, message="{0} 小粥在{1}分{2}秒前发布了新推特：".format(t.id, gap_minutes, gap_seconds)+"\n"+r"{0}".format(t.content)+"============\n原推特地址为：\n"+r"https://twitter.com/{0}/status/{1}".format(t.username[1:-1],t.address))
                if limit > 15:
                    await bot.send_group_msg(group_id=valid_group, message="==超出发送允许范围 运行中止==")
                    break
        else:
            pass
            # await bot.send_group_msg(group_id=valid_group, message="No Update")
    except CQHttpError:
        print("AUTO ERROR: ", CQHttpError.with_traceback())
