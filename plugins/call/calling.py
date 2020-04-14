# -*- coding: UTF-8 -*-
import nonebot
import os
import sys

@nonebot.on_command("callmember",aliases = ("艾特",), only_to_me = False, permission = nonebot.permission.SUPERUSER)
async def callMember(session: nonebot.CommandSession):
    pass

@nonebot.on_command("call",aliases = ("来",), only_to_me = False, permission = nonebot.permission.SUPERUSER)
async def callJob(session: nonebot.CommandSession):
    pass

#可以加单call 不过感觉没必要.jpg
