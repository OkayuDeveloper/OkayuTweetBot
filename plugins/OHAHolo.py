from nonebot import CommandSession, on_command
import datetime
import asyncio
import random
'''
早安Holo占卜模拟

慢慢添加条目就好

'''
Holomembers = {
    '时乃空',
    '萝卜子',
    '樱巫女',
    '夏色祭',
    '白上吹雪',
    '夜空梅露',
    '亚绮罗森',
    '赤井心',
    '湊阿库娅',
    '紫咲诗音',
    '百鬼绫目',
    '癒月巧可',
    '大空昴',
    '大神澪',
    '猫又小粥',
    '戌神沁音',
    '兔田佩克拉',
    '润羽露西娅',
    '不知火芙蕾雅',
    '白银诺艾尔',
    '宝钟玛琳',
    'AZKi',
    '星街彗星',
    '桐生可可',
    '天音彼方',
    '角卷绵芽',
    '常暗永远',
    '姬森璐娜'
}

Zodiac = {
    '白羊座',
    '金牛座',
    '双子座',
    '巨蟹座',
    '狮子座',
    '处女座',
    '天秤座',
    '天蝎座',
    '射手座',
    '摩羯座',
    '水瓶座',
    '双鱼座'
}

Uranai = {
    '万事顺利的一天 麻利烤肉为吉',
    '变得更加顽强 朋友是幸运的关键',
    '看东西的眼光很准的一天 SALE也◎',
    '原本的魅力闪耀的一天 珍惜喜欢的事物',
    '去获取时效性高的情报吧！',
    '求知欲比平时更高！',
    '对头上的锤子也能感觉到有意义',
    '做惯了的工作会发生低级错误！？',
    '和亲近之人心灵相通 传达感激之情吧',
    '同情心加深的一天 坦率道出温柔话语吧',
    '可以期待心动时刻的一天 慢慢进展便好',
    '自我主张要适可而止 步调保持一致',
    '曾经的努力和经验 会成为他人眼中魅力的日子',
    '财运顺畅！临时收入也值得期待',
    '越出远门越能提高幸运值的日子',
    '善解人意的一天 道出鼓励的话语吧',
    '寄全身于好奇心 世界将更加宽阔',
    '今天要小心不要被甜言蜜语所欺骗',
    '拥有独处的时间会使内心满足',
    '能够通过的新的体验深造自己的一天',
    '越是凭直觉大胆行动越能加速进展的日子',
    '可能会从亲近的亲戚那里得知条件不错的事！？',
    '匀出自由的时间 便能充实地度过',
    '才能开花! 在擅长的领域积极行动',
    '可能会得到上司和同事的感谢!',
    '尽情享受的日子 不要放过灵感!',
    '诸事顺利的一天 行云流水般行动◎',
    '成为领头人的日子 不要退缩',
    '试着设立好目标去工作',
    '立刻下单OK 消费似乎会使财运上升',
    '也许会遇上条件不错的事!',
    '购物慎重为吉 要多加斟酌',
    '做好自己分内的工作 早点下班',
    '直觉会变得敏锐 凭感觉行动○',
    '可能会遇上不错的事物 随心所欲地度过一天',
    '有意义的工作 将会是成长的关键',
    '被异性喜爱的一天 相信自己的魅力',
    '即使想法被驳回也不要气馁！',
    '会有重要的邂逅 或许能发展为长期交往',
    '可能会遇上不错的事物 随心所欲地度过一天',
    '买点东西来犒劳自己吧',
    '要多用心于与人交流',
    '即使代价偏高 今天的直觉也是正确的！',
    '临时收入转来奖励自己',
    '今天要广泛收集情报',
    '来之不易的财运有消失的危险！',
    '培养大局观 让财运跟着UP!',
    '能准确又迅速地完成工作',
    '意外之处出财运 放轻松去行动◎',
    '有收入的同时 消费也可能会增加',
    '协调的人际关系 将会有益于工作', 
    '今天要广泛收集情报',
    '即使代价偏高 今天的直觉也是正确的！',
}

done = {}
@on_command('占卜',aliases = ['抽卡'], only_to_me = False)
async def _(session:CommandSession):
    today = datetime.datetime.now().strftime('%m-%d')
    if today in done.keys():
        await asyncio.sleep(0.2)
        await session.send("今天已经占卜过了哦~")
        await asyncio.sleep(0.2)
        await session.send(done[today])
    else:
        #生成
        await asyncio.sleep(0.2)
        await session.send("正在生成今天的占卜= v =")
        await asyncio.sleep(1)
        done.clear()
        #ura = {}
        holomembers = list(Holomembers)
        zodiac = list(Zodiac)
        uranai = list(Uranai)
        message = ""
        for place in range(1,13):
            pick_holomember = holomembers.pop(random.randint(0,len(holomembers)-1))
            pick_zodiac = zodiac.pop(random.randint(0,len(zodiac)-1))
            pick_uranai = uranai.pop(random.randint(0,len(uranai)-1))
            message += "第{place}位 {zodiac} {holo}\n{ura}\n".format(place=place,zodiac=pick_zodiac,holo=pick_holomember,ura=pick_uranai)
            
        done[today] = message
        await session.send(done[today])

    pass


    