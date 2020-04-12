### 问题定义

#### 系统功能

- 新推特即时获取并转发至群聊
- 生成随机码并接收翻译文本反馈
- 利用烤推机获取图片并由文本反馈生成嵌字图

#### 可拓展功能

- 各功能开关
- 粉丝群开播通知（这个简单 有现成的）

#### 环境

- CoolQ for Docker 部署至服务器
- CoolQ <- NoneBot <- twint 获取推送
- CoolQ -> NoneBot -> MatsuriTranslation -> NoneBot -> CoolQ 获取图像

#### Reference

> https://github.com/twintproject/twint

> https://github.com/richardchien/nonebot

#### 安装方法

`pip install twint`

`pip install nonebot`

- CoolQ需要用Git下
### 开发进度

- 基于Nonebot的接口已在本地环境测试完成
- 搬推部分已完成(v1.0)
- 命令调用错误 排除多类型修饰的问题 分模块

### 总体设计