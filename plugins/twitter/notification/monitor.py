import twint
import os
import time
import datetime
import random
import math
monitor_user = 'nekomataokayu'
#monitor_user = 'Cyame1121'

class twitterList:
    def __init__(self,inlist):
        self.tList = list(inlist)
        pass


class twitterInfo(object):
    """docstring fortwitterInfo."""

    def __init__(self, line):
        self.address, self.date, self.time, self.timezone, self.username, self.content = line.split(' ',5)
        self.id = hex(int(self.address))[10:]

    def __repr__(self):
        if self.username == "<nekomataokayu>":
            return("{0} 小粥在{1} {2}发布了新推特：".format(self.id, self.date, self.time)+"\n"+r"{0}".format(self.content)+"==============\n原推特地址为：\n"+r"http://https://twitter.com/{0}/status/{1}".format(self.username[1:-1],self.address))
        else:
            return("===暂不支持其他用户===\n臭弟弟爬")
    def __str__(self):
        return repr(self)



def initialUser(monitor_user,today):
    conf = twint.Config()
    conf.Username = monitor_user
    #conf.Store_json = True
    #conf.Output = "temp.json"
    conf.Output = "newTweet.txt"
    #JSON is hard to modify
    #conf.Store_csv = True
    #conf.Output = "temp.csv"
    #conf.Custom["content"] = ["date","time","tweet"]
    conf.Since = "{0} 00:00:00".format(today)
    return conf

def getYesterday():
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    return yesterday

def get_new_twitter():
    # empty list
    newTweet = twitterList([])
    yesterdayDate = getYesterday()
    user = initialUser(monitor_user,yesterdayDate)
    #twint.run.Search(user)
    twint.run.Search(user)
    with open(file = 'newTweet.txt',mode='r',encoding='utf-8') as new:
        for line in new.readlines():
            if line == '\n':
                pass
            else:
                tempTweet = twitterInfo(line)
                newTweet.tList.append(tempTweet)
    return newTweet
                # print("Address: {}, Date: {},Time: {}, Timezone: {}, Username: {},Content: {},".format(Address,Date,Time,TimeZone,UserName,Content))

def get_old_twitter():
    # Read file
    oldTweet = twitterList([])
    if not os.path.exists("oldTweet.txt"):
        print("NO OLDTWEET FIND")
        return oldTweet
    with open(file = 'oldTweet.txt',mode='r',encoding='utf-8') as new:
        for line in new.readlines():
            if line == '\n' or line == '':
                pass
            else:
                tempTweet = twitterInfo(line)
                oldTweet.tList.append(tempTweet)
    return oldTweet
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
def automation():
    oldTweet = get_old_twitter()
    #print("OLD TWEETER RETURNED, as",oldTweet)
    newTweet = get_new_twitter()
    #print("NEW TWEETER RETURNED, as",newTweet)
    #flag = False
    #Have Something New
    updateTweet = twitterList([])
    #print("UPDATELIST INVOLVED.")
    if  (not newTweet.tList) :
        #second day
        #print("BRANCH: Empty newTweet")
        os.system("rm newTweet.txt")
        #print("Removed text")
    elif (not oldTweet.tList) or (oldTweet.tList[-1].address != newTweet.tList[-1].address):
    #     # 返回一个变更
        #flag = True
        updateTweet = compare(oldTweet,newTweet)
        #print("UpdateList generated, as",updateTweet)
        oldTweet = newTweet
        #print("INTERATED.")
        os.system("rm oldTweet.txt")
        #print("RM OLD ONE")
        os.system("mv newTweet.txt oldTweet.txt")
        #print("REPLACED.")
    #     # newTweet -> oldTweet
    #     pass
    else:
        os.system("rm newTweet.txt")
    #print("=============DONE=============")
    return updateTweet, oldTweet
    #     # silence & keep
    #     pass
    # get_new_twitter()
