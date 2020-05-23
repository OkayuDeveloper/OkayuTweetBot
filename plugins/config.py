import sys
valid_group = 1094163087


general_config = {
    #复读机
    'enable_repeat':True,
    #死亡笔记 指催活定时提醒
    'enable_deathnote':True,
    #娱乐插件 指静态回复和自然语言处理
    'enable_entertainment':True,
    #欢迎新人 指入群自动发送
    'enable_auto_welcome':True,
    #广播呼叫 指群体圈人干活
    'enable_atcalling':True,
    #私聊操作 指是否允许私聊对其他群聊的操作(暂时没想好咋写)
    'enable_privateOP':True,
    #职位名单
    'jobs':{
        '翻译',
        '时轴',
        '特效轴',
        '美工',
        '剪辑',
        '后期',
        '校对',
        '混音',
        '同传',
        '画师',
        '开发',
        '组长',
        '复查',
        '入驻'
    },
    #职位大类名单
    'jobtypes':{
        '烤肉':{
            '翻译',
            '时轴',
            '校对',
            '复查'
        },
        'PV':{
            '后期',
            '画师',
            '调音'
        },
        '管理':{
            '组长',
            '复查'
        }
    },
    #职位索引存储位置
    'memberList':"member.txt",
    #欢迎新人模板
    'welcome_template':'欢迎新龙',
    #留言消息模板
    'message_template':'{called},{act}刚才叫你，他说：{message}',
    #广播呼叫模板
    'calling_template':'{member}醒醒,{actor}叫你干活啦{message}',
    #定时催活模板
    'death_template':'{member}你醒啦,你{message}交了吗(噔噔咚)',
    'pa_template':['我爬 我现在就爬','我爪巴','你给爷爬','呜呜呜别骂了 再骂BOT就傻了']

}