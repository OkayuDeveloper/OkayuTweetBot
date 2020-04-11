#from nonebot import on_command, CommandSession,message
import nonebot
import plugins.twitter.notification.monitor as monitor
from plugins.management.management import valid_group



@nonebot.on_command('refresh', aliases = ('刷新',),only_to_me=False, privileged=True)
async def force_monitor(session: nonebot.CommandSession):
    bot = nonebot.get_bot()
    await session.send("===手动获取推文中，请稍候===")
    #updateTweet, oldTweet = monitor.main()
    # try:
    #     updateTweet, oldTweet = monitor.automation()
    # except BaseException:
    #     logger.debug(BaseException)
    #     await session.send("GETTER EXCEPTION")
    #monitor.getYesterday()
    newTwitter = monitor.get_old_twitter()
    length = len(newTwitter.tList)
    await session.send("共获取到{0}条新推特".format(length))
    await session.send(str(newTwitter.tList[0]))
    # await session.send("===已连接服务器===")
    # if updateTweet.tList:
    #     await bot.send_group_msg(group_id = valid_group,message= "UPDATE FOUND")
    #     for t in updateTweet.tList:
    #         await bot.send_group_msg(group_id = valid_group, message= "GET")
    #         await bot.send_group_msg(group_id = valid_group, message = t)
    #         #await session.send(message=str(t))
    #     await session.send("===获取新增推文完毕===")
    # else:
    #     await session.send("===未检测到新增推文===")