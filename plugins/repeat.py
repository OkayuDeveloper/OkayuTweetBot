import nonebot.log
#import nonebot.natural_language
import nonebot.message
from nonebot import on_notice,NoticeSession
from config import general_config as conf

messageList = []
@on_notice
async def _(session:NoticeSession):
    global messageList
    times = conf['repeataftertime']
    if len(messageList) < times:
        messageList.append(session.event['message'].strip())
    else:
        messageList.pop(0)
        messageList.append(session.event['message'].strip())
    if messageList.count(messageList[0]) >= times:
        session.send(messageList[0])
        messageList = []
    pass

