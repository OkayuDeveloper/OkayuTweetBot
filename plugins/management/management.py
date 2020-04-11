import nonebot
#from nonebot import NoticeSession
from aiocqhttp import *

function_press = True
valid_group = 1094163087

#bot = nonebot.get_bot()

@nonebot.on_command("admin",aliases=("管理员",),only_to_me=False)
async def offon(arg):
    global function_press
    if function_press:
        function_press = False
    else:
        function_press = True
    pass

@nonebot.on_notice("group_increase")
async def welcome(session: nonebot.NoticeSession):
    #bot = nonebot.get_bot()
    welcomewords = '欢迎新龙！！\n进群首先请查看群公告，阅读「猫又小粥字幕组组规」并完成如下操作：'
    point_1 = '1、修改群昵称为：【职位】ID，例如：【时轴】BF天下'
    point_2 = '2、再次浏览群公告，熟悉各表单及各项工具的使用，并于工作表中“粥组人口普查”中登记注册'
    point_3 = '3、打开群空间，打开规范与资料文件夹，浏览“共通”与所“申请职位”对应文件夹全部内容，并获取相关资料'
    caution = '===============\n注意：请勿在未授权的情况下对外透露任何组内相关内容（包括进度、消息、资料等）\n==============='
    ending = '自我介绍一下，我是本群最菜群友，负责日常推特搬运及其他辅助管理工作，请多指教\n粥组欢迎你的到来！'
    await session.send(message = welcomewords,ignore_failure = False)
    await session.send(message = point_1,ignore_failure = False)
    await session.send(message = point_2,ignore_failure = False)
    await session.send(message = point_3,ignore_failure = False)
    await session.send(message = caution,ignore_failure = False)
    await session.send(message = ending,ignore_failure = False)

@nonebot.on_command("welcome", aliases = ("欢迎",),only_to_me=False)
async def force_welcome(session: nonebot.CommandSession):
    welcomewords = '欢迎新龙！！\n进群首先请查看群公告，阅读「猫又小粥字幕组组规」并完成如下操作：'
    point_1 = '1、修改群昵称为：【职位】ID，例如：【时轴】BF天下'
    point_2 = '2、再次浏览群公告，熟悉各表单及各项工具的使用，并于工作表中“粥组人口普查”中登记注册'
    point_3 = '3、打开群空间，打开规范与资料文件夹，浏览“共通”与所“申请职位”对应文件夹全部内容，并获取相关资料'
    caution = '===============\n注意：请勿在未授权的情况下对外透露任何组内相关内容（包括进度、消息、资料等）\n==============='
    ending = '自我介绍一下，我是本群最菜群友，负责日常推特搬运及其他辅助管理工作，请多指教\n粥组欢迎你的到来！'
    await session.send(message = welcomewords,ignore_failure = False)
    await session.send(message = point_1,ignore_failure = False)
    await session.send(message = point_2,ignore_failure = False)
    await session.send(message = point_3,ignore_failure = False)
    await session.send(message = caution,ignore_failure = False)
    await session.send(message = ending,ignore_failure = False)

@nonebot.on_command("addlist", aliases = ("可选职位",), only_to_me = False)
async def add_list(session: nonebot.CommandSession):
    #bot = nonebot.get_bot
    joblist = '目前可选择的职位参数有\n===================\n翻译 时轴 校对 美工 剪辑 后期 调音 咖啡 夕云'
    #job = '这是一条bot.send测试'
    #jj = '这是一条send_group_msg测试'
    #jb = '这是第二条send_group_msg测试'
    #await bot.send_group_msg(group_id = valid_group, message = joblist)
    await session.send(message = joblist,ignore_failure = False)
    #await session.bot.send(message = job)
    #await session.bot.send_group_msg(group_id = valid_group, message = jj)
    # It good to be ↓
    # await bot.send_group_msg(group_id = valid_group, message = jb)

@nonebot.on_command("add", aliases = ("添加",), only_to_me = False)
async def add_member(session: nonebot.CommandSession):
    pass
# weather.args_parser 装饰器将函数声明为 weather 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
# @add.args_parser
# async def _(session: CommandSession):
#     # 去掉消息首尾的空白符
#     stripped_arg = session.current_arg_text.strip()

#     if session.is_first_run:
#         # 该命令第一次运行（第一次进入命令会话）
#         if stripped_arg:
#             # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
#             # 例如用户可能发送了：天气 南京
#             session.state['job'] = stripped_arg
#         return

#     if not stripped_arg:
#         # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
#         # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
#         session.pause('要查询的城市名称不能为空呢，请重新输入')

#     # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
#     session.state[session.current_key] = stripped_arg
#     message = session.get('job').split()
#     with open("../joblist.txt", 'a') as l:
#         l.write("{0} {1}\n".format(message[0],message[1]))
