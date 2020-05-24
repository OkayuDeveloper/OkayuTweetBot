import datetime
from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand
import asyncio
import json
import random
#from config import general_config as conf
#from template import pa_template
# on_command 装饰器将函数声明为一个命令处理器
@on_command('爪巴',aliases=['爬'],only_to_me = False)
async def pa(session: CommandSession):
    # stripped_arg = session.current_arg_text.strip()
    str = ['我爬']
    #str = pa_template
    index = random.randint(0,len(str)-1)
    if type(str[index]) == 'string':
        await asyncio.sleep(0.2)
        await session.send(str[index])
    elif type(str[index]) == 'list':
        for sentence in str[index]:
            await asyncio.sleep(0.2)
            await session.send(sentence)
    else:
        await session.send('发生错误')
    

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

@on_natural_language(keywords={'爬','爪巴'})
async def _(session: NLPSession):
    msg = session.msg_text.strip()
    #count = 0
    if 'bot' in msg.lower():
        return IntentCommand(90.0,'爪巴')
    else:
        await asyncio.sleep(0.2)
        await session.send('msg')
    pass

@on_natural_language(keywords={'早安','早'})
async def _(session: NLPSession):
    #msg = session.msg_text.strip()
    #count = 0
    now = datetime.datetime.now().strftime('%H')
    if int(now) < 10:
        return IntentCommand(90.0,'早')
    else:
        return IntentCommand(50.0,'早')
    pass

@on_natural_language(keywords={'晚安','睡了'})
async def _(session: NLPSession):
    #msg = session.msg_text.strip()
    #count = 0
    now = datetime.datetime.now().strftime('%H')
    if int(now) < 5 or int(now) > 22:
        return IntentCommand(90.0,'晚安')
    else:
        return IntentCommand(50.0,'晚安')
    pass