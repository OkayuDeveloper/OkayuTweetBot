#from nonebot import on_command, CommandSession,message
import nonebot
import plugins.twitter.notification.tweetUtils as utils
from plugins.management.management import valid_group



@nonebot.on_command('loadtwitterlist', aliases = ('加载','推特列表'),only_to_me=False, privileged=True)
async def getOld(session: nonebot.CommandSession):
    #bot = nonebot.get_bot()
    await session.send("===手动获取当前推文列表中 请稍候===")
    oldTwitter = utils.get_old_twitter()
    length = len(oldTwitter.tList)
    await session.send("列表共找到{0}条推特".format(length))
    for t in oldTwitter.tList:
        await session.send(str(t))

@nonebot.on_command('update', aliases=("刷新","refresh",),only_to_me=False,privileged=True)
async def getUpdate(session: nonebot.CommandSession):
    #bot = nonebot.get_bot()
    await session.send("===查询更新中===")
    updateTwitter = utils.get_update_twitter()
    length = len(updateTwitter.tList)
    await session.send("共找到{0}条新推特".format(length))
    for t in updateTwitter.tList:
        await session.send(str(t))
    pass