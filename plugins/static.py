from nonebot import on_command, CommandSession
import asyncio
import json
import random
from config import general_config as conf
# on_command 装饰器将函数声明为一个命令处理器
@on_command('爪巴',aliases=['爬'],only_to_me = False)
async def pa(session: CommandSession):
    # stripped_arg = session.current_arg_text.strip()
    await asyncio.sleep(0.2)
    str = conf['pa_template']
    index = random.randint(0,len(str)-1)
    await session.send(str[index])
    

@on_command('早',aliases=['早安'],only_to_me= False)
async def morning(session: CommandSession):
    await asyncio.sleep(0.2)
    await session.send('早上了喵！')
    await asyncio.sleep(0.2)
    await session.send('起床了喵！')

@on_command('晚安',aliases=['晚安'],only_to_me=False)
async def night(session: CommandSession):
    await asyncio.sleep(0.2)
    await session.send('晚安了喵！！！')
    await asyncio.sleep(0.2)
    await session.send('睡觉了喵！')
    pass