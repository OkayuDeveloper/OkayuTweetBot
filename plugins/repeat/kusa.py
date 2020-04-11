from nonebot import on_command, CommandSession
import random

@on_command('草',only_to_me=False)
async def kusa(session: CommandSession):
    await session.send("草")