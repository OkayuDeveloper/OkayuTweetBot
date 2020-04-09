import twint
import os
import time
import datetime

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
    def __repr__(self):
        if self.username = "<nekomataokayu>":
            return("小粥在{0} {1}发布了新推特：\N{2}\N原推特地址为：{3}".format(self.time,self.date,self.content))
        else:
            return("===暂不支持其他用户===")
    def __str__(self):
        return __repr__(self)



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
    with open("newTweet.txt",'r') as new:
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
    with open("oldTweet.txt",'r') as new:
        for line in new.readlines():
            if line == '\n' or line == '':
                pass
            else:
                tempTweet = twitterInfo(line)
                oldTweet.tList.append(tempTweet)
    return oldTweet

def main():
    oldTweet = get_old_twitter()
    newTweet = get_new_twitter()
    flag = False
    #Have Something New
    if  (not newTweet.tList) :
        #second day
        os.system("rm newTweet.txt")
    elif (not oldTweet.tList) or (oldTweet.tList[-1].address != newTweet.tList[-1].address):
    #     # 返回一个变更
        flag = True
        oldTweet = newTweet
        os.system("rm oldTweet.txt")
        os.system("mv newTweet.txt oldTweet.txt")
    #     # newTweet -> oldTweet
    #     pass
    else:
        os.system("rm newTweet.txt")
    return flag,oldTweet
    #     # silence & keep
    #     pass
    # get_new_twitter()

if __name__ == '__main__':
    #flag = F 没更新 flag = T 更新了
    flag, oldTweet = main()
    #print(flag, oldTweet)
