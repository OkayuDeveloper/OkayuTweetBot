from plugins.management.management import valid_group
import os
import sys
import file

#MemberList类 用于存储Member类
class MemberList:
    #整合自Member类
    def __init__(self,rawList):
        self.mList = rawList
    def __str__(self):
        return "\n".join(str(member) for member in self.mList)
    def __repr__(self):
        return " ".join(member.cq() for member in self.mList)
    def cq(self):
        return " ".join(member.cq() for member in self.mList)


#Member类 用于存储成员信息
class Member:
    # TODO: 翻译字典
    # 名称星尘你定就好了.jpg
    jobDict = {"Translator":"翻译","Timeline":"时轴","Effect":"特效轴","Check":"校对"}
    # 构造函数
    def __init__(self,line):
        content = line.split()
        self.name = content.pop(0)
        self.id = content.pop(0)
        self.job = content
    # 职位翻译为中文 输入job表 输出翻译后的job表
    def trans(self):
        trans = []
        for j in self.job:
            trans.append(jobDict[j])
        return trans
    # TODO: 通过中文找英文名（用于添加成员）
    def reverse_trans(self):
        pass
    # 打印人员信息用
    def __str__(self):
        return "成员={0} QQ={1} 当前职位={2}".format(self.name,self.id,self.trans())
    # 单独CUE人用 称呼+at
    def __repr__(self):
        return self.name+cq(self)
    # 群CUE用 at
    def cq(self):
        return "[CQ:at,qq={1}]".format(self.id)
# TODO: 用于获取和刷新列表
# 后面方法构造memList请调用此方法
def get_memberList_from_file(memberFile = 'member.txt'):
    pass
# TODO: 通过名字找人
def search_by_name(memberFile = 'member.txt',name = None):
    pass
# TODO: 通过QQ号找人
def search_by_qq(memberFile = 'member.txt',qq = None):
    pass
# TODO: 返回指定职位成员列表
def search_by_job(memberFile = 'member.txt',job = None):
    pass
# TODO: 添加成员
def add_member(memberFile = 'member.txt',member = None):
    #直接文件IO 后同
    #文本路径可忽略 直接写member.txt就可以
    #运行测试的时候 记得使用命令py -3 -m callingUtils←作为模块加载/没有.py后缀
    pass
# TODO: 删除成员
def remove_member(memberFile = 'member.txt',member = None):
    pass
# TODO: 添加成员职位
# Tjob指中文名称 需要做翻译
def add_member_job(memberFile = 'member.txt',member = None,Tjob = None):
    pass
# TODO: 删除成员职位
def remove_member_job(memberFile = 'member.txt',member = None,Tjob = None):
    pass
# TODO: 变更成员名称（使用上面两个方法就可以）
def modify_member_name(memberFile = 'member.txt',member = None,newName = None):
    pass
# TODO: 变更成员职位
def modify_member_job(memberFile = 'member.txt',member = None,fromTjob = None,toTjob = None):
    pass
