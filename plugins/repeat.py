#import nonebot.log
#import nonebot.natural_language
#import nonebot.message
import nonebot
import aiocqhttp
#from nonebot import on
#from nonebot import on_notice,NoticeSession
#from nonebot import NLPSession,on_natural_language
from plugins.config import general_config as conf
bot = nonebot.get_bot()
lastlog = {}
@bot.on_message('group')
async def _(event: aiocqhttp.Event):
    global lastlog
    times = conf['repeataftertime']
    thisgroup = str(event.group_id)
    previousmessage = str(event.message)
    
    
    if not thisgroup in lastlog.keys():
        lastlog[thisgroup] = (previousmessage,1)
    elif lastlog[thisgroup][0] != previousmessage:
        lastlog[thisgroup] = (previousmessage,1)
    else:
        lastlog[thisgroup] = (previousmessage,lastlog[thisgroup][1]+1)
    print(lastlog[thisgroup])
    if lastlog[thisgroup][1] >= times:
        await bot.send_group_msg(group_id=int(thisgroup),message=previousmessage)
        lastlog[thisgroup][1] = 0


