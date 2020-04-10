from utils import *
import os
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from monitor import *
import nonebot
#from management import valid_group
valid_group = 1094163087
bot = nonebot.get_bot()
@bot.on_command('refresh')
async def force_monitor(session: CommandSession):
    bot = nonebot.get_bot()
    await session.send("===手动获取推文中，请稍候===")
    updateTweet, oldTweet = monitor.main()
    if updateTweet.tList:
        for t in updateTweet.tList :
            await bot.send_group_msg(group_id = valid_group, message = str(t))
        await("===获取新增推文完毕===")
    else:
        session.send("===未检测到新增推文===")

@nonebot.scheduler.scheduled_jog('interval', minutes = 15)
async def monitor():
    #bot = nonebot.get_bot()
    updateTweet, oldTweet = monitor.main()
    if updateTweet.tList:
        for t in updateTweet.tList :
            await bot.send_group_msg(group_id = valid_group, message = str(t))
