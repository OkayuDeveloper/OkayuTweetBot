# -*- coding: UTF-8 -*-
import nonebot
from plugins.configure.configuration import *


'''

供全体成员使用的呼叫管理员模块


'''

#TODO 延时呼叫

@nonebot.on_command("夕云",aliases = ("夕雲","yuugumo","xiyun",),only_to_me = False)
async def yuugumo(session: nonebot.CommandSession):
    #id = nonebot.session.user_id
    #Need check api how to get user_id from session
    session.send("夕云[CQ:at,qq={0}]".format(qq_yuugumo))
    pass
#TODO
@nonebot.on_command("咖啡",aliases = ("Coffee","coffee","kafei",),only_to_me = False)
async def coffee(session: nonebot.CommandSession):
    pass
#TODO
@nonebot.on_command("hibiki", aliases = ("响佬", "响爷", "响前辈",),only_to_me = False)
async def hibiki(session: nonebot.CommandSession):
    pass
#TODO
@nonebot.on_command("haiyu", aliases = ("海鱼","海藻","海草","海带","海鱼鱼",),only_to_me = False)
async def haiyu(session:nonebot.CommandSession):
    pass
