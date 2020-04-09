from nonebot import *
from utils import *
import os

@on_command('refresh',aliases = ('刷新',))
async def run_scratch():
    os.system("python3 ../monitor.py")
