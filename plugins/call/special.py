import nonebot

qq_yuugumo = 296172851
qq_coffee = 920239562
qq_hibiki = 375353085
qq_haiyu = 920337594

@nonebot.on_command("夕云",aliases = ("夕雲","yuugumo","xiyun",),only_to_me = False)
async def yuugumo(nonebot.session: CommandSession):
    #id = nonebot.session.user_id
    #Need check api how to get user_id from session
    session.send("夕云[CQ:at,qq={0}]".format(qq_yuugumo))
    pass
#TODO
@nonebot.on_command("咖啡",aliases = ("Coffee","coffee","kafei",),only_to_me = False)
async def coffee(nonebot.session: CommandSession):
    pass
#TODO
@nonebot.on_command("hibiki", aliases = ("响佬", "响爷", "响前辈",),only_to_me = False)
async def hibiki(nonebot.session: CommandSession):
    pass
#TODO
@nonebot.on_command("haiyu", aliases = ("海鱼","海藻","海草","海带","海鱼鱼",),only_to_me = False)
async def haiyu(nonebot.session:CommandSession):
    pass