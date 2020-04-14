# -*- coding: UTF-8 -*-
from nonebot import on_command, CommandSession
import random

@on_command('草',only_to_me=False)
async def kusa(session: CommandSession):
    await session.send("草")


@on_command('爬',aliases=("爪巴",),only_to_me=False)
async def pa(session: CommandSession):
    await session.send("我爬 我现在就爬")
