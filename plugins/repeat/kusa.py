# -*- coding: UTF-8 -*-

from nonebot import on_command, CommandSession
import random

'''

本模块用于指定一些响应词，用于虐待bot(划掉)测试服务部署情况
在config.py中若指定命令前缀为空字符，则本模块中全部内容将100%被复读
推荐本模块采取简单会话响应的编写原则，尽量不添加复杂的逻辑

'''


#对于草的响应 后同 不再另行注释
@on_command('草',only_to_me=False)
async def kusa(session: CommandSession):
    await session.send("草")


@on_command('爬',aliases=("爪巴",),only_to_me=False)
async def pa(session: CommandSession):
    await session.send("我爬 我现在就爬")


@on_command('半夏',aliases=("半夏行为",),only_to_me=False)
async def half(session: CommandSession):
    await session.send("。。")
    await session.send("害")
