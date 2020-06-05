import datetime
from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand
import asyncio
import nonebot
import json
import random
from plugins.config import general_config as conf
from template import pa_template
'''
静态自然语言回复模块

早安/晚安
爬

'''
@on_command('pa',only_to_me = False)
async def pa(session: CommandSession):
    # stripped_arg = session.current_arg_text.strip()
    #str = ['我爬']
    lib = pa_template
    index = random.randint(0,len(lib)-1)
    if type(lib[index]) == str:
        await asyncio.sleep(0.2)
        await session.send(lib[index])
    elif type(lib[index]) == list:
        for sentence in str[index]:
            await asyncio.sleep(0.2)
            await session.send(sentence)
    else:
        await session.send('发生错误')
    

@on_command('goodmorning',only_to_me= False)
async def morning(session: CommandSession):
    await asyncio.sleep(0.2)
    await session.send('早上了喵！')
    await asyncio.sleep(0.2)
    await session.send('起床了喵！')


@on_command('goodnight',only_to_me=False)
async def night(session: CommandSession):
    await asyncio.sleep(0.2)
    await session.send('晚安了喵！！！')
    await asyncio.sleep(0.2)
    await session.send('睡觉了喵！')
    pass

@on_natural_language(keywords={'爬','爪巴'})
async def _(session: NLPSession):
    msg = session.msg_text.strip()
    #count = 0
    await asyncio.sleep(0.2)
    if 'bot' in msg.lower():
        return IntentCommand(90.0,'pa')
    elif '!' or '！' in msg.lower():
        return IntentCommand(30.0,'pa')
    else:
        return IntentCommand(70.0,'pa')
    pass

@on_natural_language(keywords={'早安','早'})
async def _(session: NLPSession):
    #msg = session.msg_text.strip()
    #count = 0
    now = datetime.datetime.now().strftime('%H')
    if int(now) < 10:
        return IntentCommand(90.0,'goodmorning')
    else:
        return IntentCommand(50.0,'goodmorning')
    pass

@on_natural_language(keywords={'晚安','睡了'})
async def _(session: NLPSession):
    #msg = session.msg_text.strip()
    #count = 0
    now = datetime.datetime.now().strftime('%H')
    if int(now) < 5 or int(now) > 22:
        return IntentCommand(90.0,'goodnight')
    else:
        return IntentCommand(50.0,'goodnight')
    pass