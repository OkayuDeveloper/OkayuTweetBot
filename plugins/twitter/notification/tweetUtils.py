# -*- coding: UTF-8 -*-
import twint
import os
import time
import datetime
import random
import math
import traceback
import json
import sys
d = os.path.dirname(__file__)
home_path = os.path.dirname(os.path.dirname(os.path.dirname(d)))
sys.path.append(home_path)

from plugins.configure.configuration import monitor_user


#monitor_user = 'Cyame1121'
class twintError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# 定义一个推特列表用于存储tweet封装
class twitterList:
    def __init__(self,inlist):
        self.tList = list(inlist)
        pass

# tweet封装 由JSON读取得来 使用repr返回
# 请勿使用直接调用 session.send不支持自动调用str
class twitterInfo(object):
    """docstring fortwitterInfo."""
    #构造 直接传入读取自twint写入的行 在内部通过读取JSON转化
    def __init__(self, dict):
        self.info = json.loads(dict)
        self.code = hex(int(self.info['id']))[10:]
    #调用 用于独立作为控制台调试模块时使用
    def __str__(self):
        return str(self.info)
    def getTweet(self):
        return self.info["tweet"] 
    def getCode(self):
        return self.code
    def getDateAndTime(self):
        return "{} {}".format(self.info["date"],self.info["time"])

# 初始化监控对象
# 参数表
# param monitor_user:监视用户名 仅供扩展(已全局声明)
# param current_day:目标监视日期
# param save_file:捕获结果保存路径
def initialSearch(monitor_user,current_day,save_file):
    conf = twint.Config()
    conf.Username = monitor_user
    conf.Output = save_file
    conf.Since = "{0} 00:00:00".format(current_day)
    conf.Store_json = True
    #获取指定日期之后的推文筛选条件
    return conf

def getYesterday():
    #获取24小时内推文
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    return yesterday

# 利用twint包进行推特捕获
# param save_file:存储为(根目录)
def getTwitterFromTwint(save_file):
    #声明容器
    #getList = twitterList([])
    #获取昨天日期
    targetDay = getYesterday()
    #构造搜索
    try:
        thisSearch = initialSearch(monitor_user,targetDay,save_file)
        #RUN
        twint.run.Search(thisSearch)
    except:
        traceback.print_exc()
        raise twintError("=============GET ERROR WHEN CONNECT TO TWINT=============")

    return save_file

# 从已保存的文件中获取推特表以备输出
# param read_file:所需读取位置
# return 返回twitterList对象
def configTwitterFromFile(read_file):
    getList = twitterList([])
    if not os.path.exists(read_file):
        print("======FILE NOT FOUND=======")
        return getList
    with open(file = read_file,mode='r',encoding='utf-8') as target:
        for line in target.readlines():
            if line == '\n' or line == '':
                pass
            else:
                tempTweet = twitterInfo(line)
                getList.tList.append(tempTweet)
    return getList

# 获取新推特(旧方法重构)
def get_new_twitter():
    newTweetFile = getTwitterFromTwint("newTweet.json")
    newTweetList = configTwitterFromFile(newTweetFile)
    return newTweetList

# 获取新推特(旧方法重构)
def get_old_twitter():
    # Read file
    if os.path.exists("oldTweet.json"):
        oldTweetList = configTwitterFromFile("oldTweet.json")
        return oldTweetList
    else:
        return twitterList([])

# 获取新增推特(新方法：从文件)
def File_compare(oldTweetFile,newTweetFile):
    #已存在推文地址ID
    oldAddressList = []
    updateTweetList = []
    update_path = "updateTweet.txt"
    with open(file = oldTweetFile, mode='r',encoding='utf-8') as o:
        for line in o.readlines():
            if line == '\n' or line == '':
                continue
            else:
                oldAddressList.append(line.split()[0])
    with open(file = newTweetFile, mode='r',encoding='utf-8') as n:
        for line in n.readlines():
            if line == '\n' or line == '':
                continue
            else:
                temp = line.split()[0]
                if not temp in oldAddressList:
                    #New
                    updateTweetList.append(line)
    with open(file = update_path, mode='w',encoding='utf-8') as u:
        for rawTweet in updateTweetList:
            u.write(rawTweet)
    return update_path

# 获取新增推特(新方法)
def get_update_twitter():
    updateTweetList = configTwitterFromFile("updateTweet.txt")
    return updateTweetList

# 每次生成UPDATE后迭代
def fileIterator(oldTweetFile = 'oldTweet.txt',newTweetFile = 'newTweet.txt'):
    os.system("mv -f {0} {1}".format(newTweetFile,oldTweetFile))

# 当无更新时删除新增避免重复获取
def fileExpire(newTweetFile = 'newTweet.txt'):
    os.system("rm {0}".format(newTweetFile))

# 获取新增推特(旧方法)
# 读入twitterList 返回twitterList
def compare(oldTweetList,newTweetList):
    updateList = []
    addressList = []
    for oldTweet in oldTweetList.tList:
        addressList.append(oldTweet.address)
    for tweet in newTweetList.tList:
        if not tweet.address in addressList:
            #New
            updateList.append(tweet)
    updateTweet = twitterList(updateList)
    return updateTweet

# 主函数旧方法重构
def automation():
    oldTweet = get_old_twitter()
    newTweet = get_new_twitter()
    updateTweet = twitterList([])
    if  (not newTweet.tList) :
        #New Day
        fileExpire()
    elif (not oldTweet.tList) or (oldTweet.tList[-1].address != newTweet.tList[-1].address):
        #Changed
        updateTweet = compare(oldTweet,newTweet)
        oldTweet = newTweet
        fileIterator()
    else:
        fileExpire()
    return updateTweet, oldTweet

# 获取过程
def getProcess():
    newTweetFile = ''
    oldTweetFile = ''
    try:
        newTweetFile = getTwitterFromTwint("newTweet.txt")
        oldTweetFile = "oldTweet.txt"
        if not os.path.exists(newTweetFile):
            #EMPTY
            empty = open(newTweetFile,mode='w+',encoding='utf-8')
            empty.close()
        if os.path.exists(oldTweetFile):
            updateTweetFile = File_compare(oldTweetFile,newTweetFile)
        fileIterator(oldTweetFile,newTweetFile)

    except BaseException:
        print(BaseException)
        traceback.print_exc()
        if os.path.exists(newTweetFile):
            fileExpire(newTweetFile)


        return False

    return True

# 推送过程
def readProcess():
    updateList = get_update_twitter()
    oldList = get_old_twitter()
    return updateList,oldList
