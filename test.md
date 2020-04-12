### 工程框架

#### 根目录
> config.py nonebot指定的config文档

> api.py 原框架（已废弃）

> connection.py CQHTTP启动脚本

> \*.txt 暂留缓存文件 重新测试时请清空其中所有内容

> \*.md 说明文档

#### plugins **插件包**

##### call **一键呼叫某职能人员(待开发)**
> calling.py 没写呢还

##### example **API中所示每日一句相应脚本 作为扩展暂留**
> daily_example.py nonebot接口

> utils.py 金山词霸API链接

##### management **管理插件(目前只开发欢迎群友功能←以后可以加定时滴滴代公告功能以免圈全体用完了难顶)**
> management.py 主接口

##### repeat **复读机**
>kusa.py 它草和爬一直可以的.jpg

##### twiiter **搬推**
- notification 通知（目前暂时只搞通知罢 以后如果能接烤推机就单做一个translation包分开）
> auto_scratcher.py 定时从**缓存文件**中获取更新

> force_scratcher.py 强制从**缓存文件**中立即获取更新(与auto调用不同方法 不冲突)

> ScheduledMonitor.py ASPScheduler驱动的定时**twint获取**器

> timerMonitor.py threading.Timer驱动的定时**twint获取**器

> tweetUtils.py 集成twint接口和读缓存接口

#### temp **暂时废弃but一度可用的代码(暂留)**
> api/botinterface 如果能有推特API的话将使用

> monitor_auto 旧写法的**twint获取+更新**接口（现使用Utils）

> twint_scratcher 旧定时获取器


##注记

当前框架和4-11以前的框架有了较大区别，目的是为了解决获取时session提前关闭导致无法返回的问题
####旧获取流程
- 使用 monitor_auto + twint_scratcher

twint_scratcher定期被调用
↓
twint_scratcher调用montior_auto中的方法
↓
从twint获取更新
↓
比对oldTweet.txt中缓存 获取updateList
↓
更新oldTweet.txt 将新获取的推特注入缓存
↓
返回updateList和oldList对象
↓
返回到twint_scratcher之后通过CQHTTP返回

#### 新获取流程
##### 将获取和返回分离
- 获取：获取自twint并缓存
- 返回：从缓存中读出并通过CQHTTP返回

##### 获取流程(function getProcess)
预计使用ASP或Timer框架独立运行
具体流程为：

- 从twint获取新推特
- 从缓存获取老推特（如果无就返回空）
- 比对后将更新缓存至updateTweet.txt
- 将新推特替换老推特

##### 返回流程(function readProcess)
使用nonebot提供的ASP修饰进行（预计）
具体流程为：

- 从缓冲中读出老推特（作为推特列表）
- 从缓冲中读出更新列表
- 返回CQHTTP接口
