from nonebot import on_command, CommandSession,permission as perm
import asyncio
import traceback
from helper import getlogger,msgSendToBot,CQsessionToStr,data_read,data_save
from module.roll import match_roll
logger = getlogger(__name__)
__plugin_name__ = 'ROLL骰'
__plugin_usage__ = r"""
roll命令
"""
#预处理
def headdeal(session: CommandSession):
    if session.event['message_type'] == "group" and session.event.sub_type != 'normal':
        return False
    return True

# on_command 装饰器将函数声明为一个命令处理器
@on_command('roll',aliases=['掷骰','掷骰子','骰子'],only_to_me = False)
async def roll(session: CommandSession):
    if not headdeal(session):
        return
    stripped_arg = session.current_arg_text.strip()
    #if stripped_arg == '':
    #    await session.send('参数为空！')
    #    return
    logger.info(CQsessionToStr(session))
    event = session.event
    nick = event['user_id']
    if hasattr(event,'sender'):
        if 'card' in event.sender and event['sender']['card'] != '':
            nick = event['sender']['card']
        elif 'nickname' in event.sender and event['sender']['nickname'] != '':
            nick = event['sender']['nickname']
    res = stripped_arg.split('#',1)
    addmsg = ''
    if len(res) == 2:
        stripped_arg = res[1]
        if len(res[0]) > 25:
            addmsg = "---{0}---\n".format(res[0])
        else:
            addmsg = res[0] + '#'

    if stripped_arg == '':
        stripped_arg = '1d100<50'
    elif stripped_arg[:1] in ('<','>','!'):
        stripped_arg = '1d100' + stripped_arg
    elif stripped_arg.isdecimal():
        stripped_arg = '1d100<' + stripped_arg

    try:
        msg = match_roll(nick,stripped_arg)
        if msg == '':
            await session.send('参数不正确')
            return
    except:
        s = traceback.format_exc(limit=10)
        logger.error(s)
        await session.send("内部错误！")
        return
    await session.send(addmsg + msg)

@on_command('rollhelp',aliases=['掷骰帮助','掷骰子帮助','骰子帮助','骰娘帮助'],only_to_me = False)
async def rollhelp(session: CommandSession):
    if not headdeal(session):
        return
    msg = '--掷骰帮助--' + "\n"
    msg = msg + '!roll 参数' + "\n"
    msg = msg + '无参默认为1d100>50' + "\n"
    msg = msg + '1d100固定1-5大成功,96-100大失败' + "\n"
    msg = msg + '支持符号>,<,>=,<=,!=,=,+,-,*,/' + "\n"
    msg = msg + "代码主体来自：https://github.com/akrisrn/dice"
    await session.send(msg)