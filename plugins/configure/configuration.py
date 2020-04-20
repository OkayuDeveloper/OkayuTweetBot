'''

本模块为其余各模块提供静态参数
亦可使用JSON管理（不过我懒）
如需进行变更可直接修改此处各参数

'''
import sys

#目标群(自动推送服务的发送目标)
valid_group = 1094163087
#推特昵称（作为推文推送的Title内容）
monitor_nickname = "小粥"
#推特用户名（为所监控推特用户地址[重要]）
monitor_user = "nekomataokayu"
#接入工坊烤推机路径（涉及烤推功能[重要]）
#matsuri_translation_path = "D:/EclipseJavaWorkspace/matsuri_translation/Matsuri_translation"
#功能开关（当关闭时 除开启开关外 其他一切功能禁用）
#待生效
function_press = True

#专属联系人QQ
#用于plugins.call.specail模块
#高度自定义
qq_yuugumo = 296172851
qq_coffee = 920239562
qq_hibiki = 375353085
qq_haiyu = 920337594


home_path = ""