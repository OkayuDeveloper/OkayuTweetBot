# -*- coding: UTF-8 -*-

from nonebot import on_command, CommandSession
from plugins.example.utils import *

 #@on_command('daily', aliases=('每日一句',))

@on_command('daily',aliases=('每日一句',),only_to_me=False)
async def daily(session: CommandSession):
    daily_send = await get_daily()
    await session.send(daily_send[0])
    await session.send(daily_send[1])

async def get_daily():
    daily_sentence = get_content()
    return daily_sentence
