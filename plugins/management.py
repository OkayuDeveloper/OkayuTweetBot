# -*- coding: UTF-8 -*-
import nonebot
#import config
from aiocqhttp import *
import nonebot.permission as perm
from plugins.config import general_config
from template import welcome_template as wt
import asyncio
'''

欢迎
成员管理
死亡笔记

'''


#### 欢迎群成员 ####

@nonebot.on_notice("group_increase")
async def welcome(session: nonebot.NoticeSession):
    # bot = nonebot.get_bot()
    #newass = session.user_id
    newman = session.event['user_id']
    await asyncio.sleep(0.2)
    await session.send(wt.format(new=newman))

@nonebot.on_command("welcome", aliases = ("欢迎",),only_to_me=False)
async def force_welcome(session: nonebot.CommandSession):
    message = session.current_arg_text.strip()
    session.send(wt.replace('{new}',message))
    


#### 成员管理 ####




