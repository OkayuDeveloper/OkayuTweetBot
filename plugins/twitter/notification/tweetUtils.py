import twint
import os
import time
import datetime
import random
import math
import traceback
monitor_user = 'nekomataokayu'
#monitor_user = 'Cyame1121'

# 定义一个推特列表用于存储tweet封装
class twitterList:
    def __init__(self,inlist):
        self.tList = list(inlist)
        pass

# tweet封装 由txt读取得来 使用其repr或str方法可直接打印至消息
# 请勿使用直接调用 session.send不支持自动调用repr
class twitterInfo(object):
    """docstring fortwitterInfo."""
    #构造 直接传入读取自twint写入的行即可
    def __init__(self, line):
        self.address, self.date, self.time, self.timezone, self.username, self.content = line.split(' ',5)
        self.id = hex(int(self.address))[10:]
    #调用 用于独立作为控制台调试模块时使用
    def __repr__(self):
        if self.username == "<nekomataokayu>":
            return("{0} 小粥在{1} {2}发布了新推特：".format(self.id, self.date, self.time)+"\n"+r"{0}".format(self.content)+"==============\n原推特地址为：\n"+r"https://twitter.com/{0}/status/{1}".format(self.username[1:-1],self.address))
        else:
            return("===暂不支持其他用户===\n臭弟弟爬")#笑
    #打印 返回字符串值(不做独立构造 同repr)
    def __str__(self):
        return repr(self)

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
    #获取指定日期之后的推文筛选条件
    return conf

def getYesterday():
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    #指定获取时间为昨天凌晨(避免凌晨前后推文覆盖)
    return yesterday

# 利用twint包进行推特捕获
# param save_file:存储为(根目录)
def getTwitterFromTwint(save_file):
    #声明容器
    getList = twitterList([])
    #获取昨天日期
    targetDay = getYesterday()
    #构造搜索
    thisSearch = initialSearch(monitor_user,targetDay,save_file)
    #RUN
    twint.run.Search(thisSearch)

    return save_file

# 从已保存的文件中获取推特表以备输出
# param read_file:所需读取位置
# return 返回twitterList对象
def configTwitterFromFile(read_file):
    getList = twitterList([])
    if not os.path.exists(read_file):
        print("NO TWEET FOUND")
        return getList
    with open(file = read_file,mode='r',encoding='utf-8') as new:
        for line in new.readlines():
            if line == '\n' or line == '':
                pass
            else:
                tempTweet = twitterInfo(line)
                getList.tList.append(tempTweet)
    return getList

# 获取新推特(旧方法重构)
def get_new_twitter():
    newTweetFile = getTwitterFromTwint("newTweet.txt")
    newTweetList = configTwitterFromFile(newTweetFile)
    return newTweetList

# 获取新推特(旧方法重构)
def get_old_twitter():
    # Read file
    oldTweetList = configTwitterFromFile("oldTweet.txt")
    return oldTweetList

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
    updateTweetList = configTwitterFromFile("update.txt")
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
    try:
        newTweetFile = getTwitterFromTwint("newTweet.txt")
        oldTweetFile = "oldTweet.txt"
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