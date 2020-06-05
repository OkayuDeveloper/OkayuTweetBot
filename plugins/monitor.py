import nonebot
import aiocqhttp
from plugins.config import general_config as conf
from nonebot import on_command, CommandSession
import datetime
'''
消息检测模块：多功能模块

- 复读机模块：群内N次重复消息后复读
次数由plugin.config内repeataftertime指定
- 留言模块
- DDL模块

'''
#使用aiocqhttp内方法
bot = nonebot.get_bot()

#留言词典
#元素格式 leaving_message[群] = {[接收人,发起人,留言内容]}
leaving_message = {}

#DDL词典
#元素格式 ddl_message[群] = {[时间, DDL对象, DDL内容]}
ddl_message = {}

#消息Log词典
#元素格式 lastlog[群] = (上回消息,出现次数) <- 实现多群并行
lastlog = {}

def getCurrentTime():
    return datetime.datetime.now().strftime("%m-%d %H:%M:%S")
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    return False
@bot.on_message('group')
async def _(event: aiocqhttp.Event):
    global lastlog
    global leaving_message
    global ddl_message

    ## 复读机
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

    ## 留言
    # if not thisgroup in leaving_message.keys():
    #     leaving_message[thisgroup] = list()
    


# @on_command("note",aliases=("留言",),only_to_me = False)
# async def note(session: CommandSession):
#     pass


# @on_command('ddl',aliases=("死亡笔记",),only_to_me = False)
# async def note(session: CommandSession):
#     #print(session.event)
#     message_type = session.event['message_type']
#     arguments = session.event['raw_message'].split()
#     send_id = session.event['sender']['user_id']
#     if message_type == 'group':
#         # <command> <who> <dowhat> <ddlat>
#         if len(arguments) != 4:
#             await session.send("参数个数错误 是不是格式错了> <\n!ddl <@任务执行人> <任务内容> <DDL时间>")
#             return
#         if 'CQ:at' in arguments[1]:
#             planned_id = arguments[1].split("qq=")[1][:-1]
#             print("id = ",planned_id)
#         elif is_number(arguments[1]):
#             planned_id = arguments[1]
#         else:
#             #NAME
#             pass
#         if arguments[2] == '':
#             await session.send("未指定内容")
#             return
#         ddl_content = arguments[2]

#         if ':' in arguments[3]:
#             ## YYYY-MM-DD HH:MM
#             ddl_datetime = datetime.datetime.fromisoformat(arguments[3])
#             pass
#         elif '-' in arguments[3]:
#             ## YYYY-MM-DD
#             ddl_datetime = datetime.datetime.fromisoformat(arguments[3]+' 20:00:00')
#             pass
#         else:
#             await session.send("日期格式有误 请以<YYYY-MM-DD> 或 <YYYY-MM-DD hh:mm:ss>输入")
        
#         group_id = str(session.event['group_id'])
#         log = [send_id,planned_id,ddl_content,ddl_datetime]
#         if group_id in ddl_message.keys():
#             ddl_message[group_id] = list()
#         ddl_message[group_id].append(log)
        
#         #print(log)
#     elif message_type == 'private':
#         # <command> <group> <who> <dowhat> <ddlat>
#         # TODO
#         # if len()
#         pass
#     # print(session.event)
#     # print(arguments)
#     # print(message_type)
