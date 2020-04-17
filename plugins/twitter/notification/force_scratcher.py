# -*- coding: UTF-8 -*-
import nonebot
import plugins.twitter.notification.tweetUtils as utils
from plugins.configure.configuration import *



@nonebot.on_command('load', aliases = ('加载','推特列表'),only_to_me=False, privileged=True)
async def getOld(session: nonebot.CommandSession):
    limit = 0
    oldTwitter = utils.get_old_twitter()
    length = len(oldTwitter.tList)
    if length >= 30:
        list = "列表共找到{0}条推特\n==============\n".format(length) + " ".join(t.id for t in oldTwitter.tList)
    else :
        list = "列表共找到{0}条推特\n==============\n".format(length) + "\n".join(t.id for t in oldTwitter.tList)

    # for t in oldTwitter.tList:
    #     limit += 1
    #     await session.send(str(t))
    #     if limit >= 15:
    #         await session.send("超额推特 请检查缓存及网络情况（初始化后首次请忽略本信息）")
            #break

@nonebot.on_command('update', aliases=("刷新","refresh",),only_to_me=False,privileged=True)
async def getUpdate(session: nonebot.CommandSession):
    limit = 0
    updateTwitter = utils.get_update_twitter()
    length = len(updateTwitter.tList)
    await session.send("共找到{0}条新推特".format(length))
    for t in updateTwitter.tList:
        limit += 1
        await session.send(str(t))
        if limit >= 15:
            await session.send("超额推特 请检查缓存及网络情况（初始化后首次启动请忽略本信息）")
            #可以加首次启动的限制来着...？
            break
    pass
