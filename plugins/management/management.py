# -*- coding: UTF-8 -*-
import nonebot
import config
from aiocqhttp import *
import nonebot.permission as perm
from plugins.configure.configuration import *

#bot = nonebot.get_bot()

@nonebot.on_command("admin",aliases=("管理员",),only_to_me=False,permission=perm.SUPERUSER)
async def offon(session: nonebot.CommandSession):
    global function_press
    if function_press:
        function_press = False
        await session.send("功能已停用")
    else:
        function_press = True
        await session.send("功能已启用")
    pass

@nonebot.on_notice("group_increase")
async def welcome(session: nonebot.NoticeSession):
    bot = nonebot.get_bot()
    #newass = session.user_id
    newman = session.event['user_id']
    await bot.send_group_msg(group_id=valid_group,message='欢迎新龙！！进群首先请查看群公告，阅读「猫又小粥字幕组组规」并完成如下操作：\n1、修改群昵称为：【职位】ID\n2、再次浏览群公告，熟悉各表单及各项工具的使用，并于工作表中“粥组人口普查”中登记注册\n3、打开群空间，打开规范与资料文件夹，浏览“共通”与所“申请职位”对应文件夹全部内容，并获取相关资料')
#     await bot.send_group_msg(group_id=valid_group,message='''===============
# 注意：请勿在未授权的情况下对外透露任何组内相关内容
# （包括进度、消息、资料等）
# ===============
# 自我介绍一下，我是本群最菜群友，负责日常推特搬运及其他辅助管理工作，请多指教
# 粥组欢迎你的到来！[CQ:at,qq=(beingOperateQQ)]''')
    await bot.send_group_msg(group_id=valid_group,message='''===============
注意：请勿在未授权的情况下对外透露任何组内相关内容
（包括进度、消息、资料等）
===============
自我介绍一下，我是本群最菜群友，负责日常推特搬运及其他辅助管理工作，请多指教
粥组欢迎你的到来！[CQ:at,qq={0}]'''.format(newman))

@nonebot.on_command("welcome", aliases = ("欢迎",),only_to_me=False)
async def force_welcome(session: nonebot.CommandSession):

    bot = nonebot.get_bot()
    # welcome_words = '''
    # 欢迎新龙！！
    # 进群首先请查看群公告，阅读「猫又小粥字幕组组规」
    # 并完成如下操作：
    # 1、修改群昵称为：【职位】ID，例如：【时轴】BF天下
    # 2、再次浏览群公告，熟悉各表单及各项工具的使用，并于工作表中“粥组人口普查”中登记注册
    # 3、打开群空间，打开规范与资料文件夹，浏览“共通”与所“申请职位”对应文件夹全部内容，并获取相关资料
    # ===============
    # 注意：请勿在未授权的情况下对外透露任何组内相关内容（包括进度、消息、资料等）
    # ===============
    # 自我介绍一下，我是本群最菜群友，负责日常推特搬运及其他辅助管理工作，请多指教
    # 粥组欢迎你的到来！
    # '''.strip()
    await bot.send_group_msg(group_id=valid_group,message='欢迎新龙！！进群首先请查看群公告，阅读「猫又小粥字幕组组规」并完成如下操作：\n1、修改群昵称为：【职位】ID\n2、再次浏览群公告，熟悉各表单及各项工具的使用，并于工作表中“粥组人口普查”中登记注册\n3、打开群空间，打开规范与资料文件夹，浏览“共通”与所“申请职位”对应文件夹全部内容，并获取相关资料')
    await bot.send_group_msg(group_id=valid_group,message='''===============
注意：请勿在未授权的情况下对外透露任何组内相关内容
（包括进度、消息、资料等）
===============
自我介绍一下，我是本群最菜群友，负责日常推特搬运及其他辅助管理工作，请多指教
粥组欢迎你的到来！''')


@nonebot.on_command("addlist", aliases = ("可选职位",), only_to_me = False)
async def add_list(session: nonebot.CommandSession):
    joblist = '目前可选择的职位参数有\n===================\n翻译 时轴 校对 美工 剪辑 后期 调音 特效轴 组长 开发者'
    await session.send(message = joblist,ignore_failure = False)


@nonebot.on_command("addmember",aliases = ("添加成员",), only_to_me = False, permission = perm.SUPERUSER)
async def addMember(session:nonebot.CommandSession):
    pass

@nonebot.on_command("removemember",aliases = ("删除成员"), only_to_me = False, permission = perm.SUPERUSER)
async def removeMember(session:nonebot.CommandSession):
    pass
@nonebot.on_command("addjob",aliases = ("添加职位"), only_to_me = False, permission = perm.SUPERUSER)
async def _(session:nonebot.CommandSession):
    pass
@nonebot.on_command("removejob",aliases = ("删除职位"), only_to_me = False, permission = perm.SUPERUSER)
async def _(session:nonebot.CommandSession):
    pass

@nonebot.on_command("modjob",aliases = ("变更职位"), only_to_me = False, permission = perm.SUPERUSER)
async def _(session:nonebot.CommandSession):
    pass
