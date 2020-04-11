#from nonebot import on_command, CommandSession,message
import nonebot
import plugins.twitter.notification.monitor as monitor
from plugins.management.management import valid_group



@nonebot.on_command('refresh', aliases = ('刷新',),only_to_me=False, privileged=True)
async def force_monitor(session: nonebot.CommandSession):
    bot = nonebot.get_bot()
    await session.send("===手动获取推文中，请稍候===")
    updateTweet, oldTweet = monitor.main()
    if updateTweet.tList:
        for t in updateTweet.tList :
            await bot.send_group_msg(group_id = valid_group, message = str(t))
            #await session.send(message=str(t))
        await("===获取新增推文完毕===")
    else:
        session.send("===未检测到新增推文===")