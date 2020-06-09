# -*- coding: UTF-8 -*-
from nonebot.default_config import *

#添加超级管理员 Q号-数值 例:SUPERUSERS.add(12345678)
SUPERUSERS.add(12345)

#nonebot的监听端口
HOST = '127.0.0.1'
PORT = 9100
#SECRET = ''
#ACCESS_TOKEN = ''
#API_ROOT = 'http://127.0.0.1:5700'
#nonebot的debug开关
DEBUG = False

COMMAND_START = {'!','！'}
NICKNAME = {'bot', 'bot哥', '工具人', '最菜群友'}
SESSION_CANCEL_EXPRESSION = ("好 我爬","好 我现在就爬",)
#SHORT_MESSAGE_MAX_LENGTH = 500

#默认botQQ 默认推送用的bot，错误信息会使用此bot推送。(此QQ不存在时报错将影响程序运行)
default_bot_QQ : int = 12345
#bot错误信息推送到的Q号，为空时不进行推送
feedback_push_switch : bool = True #推送反馈信息
error_push_switch : bool = True #推送错误信息
bot_waring_printID : int = 12345

#语音发送映射
music_path = r"file:///E:\CQ\python-okayu_two\cache"