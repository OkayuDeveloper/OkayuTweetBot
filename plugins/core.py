import nonebot
from nonebot import on_command,CommandSession,permission
import asyncio


@on_command("usage",aliases=("功能列表","功能"),only_to_me=False)
async def usage(session: CommandSession):
    plugins = list(filter(lambda p: p.name,(nonebot.get_loaded_plugins())))
    arg = session.current_arg_text.strip().lower()
    if not arg:
        await session.send("BOT目前支持的功能\n=====\n"+"\n".join(p.name for p in plugins))
        return
    else:
        for p in plugins:
            if p.name.lower() == arg:
                await session.send(p.usage)


on_command("off",aliases=("关闭功能"),permission = permission.SUPERUSER,only_to_me=True)
async def offfunction(session):
    plugins = list(nonebot.get_loaded_plugins)
    arg = session.current_arg_text.strip().lower()
    if not arg:
        await session.send("要关闭哪个功能鸭~\n请按照!off <功能名>的格式进行操作\n功能名列表可以使用usage命令查看QuQ")
    else:
        for p in plugins:
            if p.name.lower() == arg:
                #await 
                pass