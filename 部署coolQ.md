## 安装Docker

- 更新apt库

  ` sudo apt update`

- 安装依赖

  `sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common`

- 添加GPG密钥匙

  `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`

- 验证密钥

  `sudo apt-key fingerprint 0EBFCD88`

- 使用稳定版仓库

  `sudo add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"`

- 更新索引

  `apt update`

- 安装Docker-Community & Container

  `apt install docker-ce docker-ce-cli containerd.io`

- 测试安装成功

  `sudo docker run hell-world`

- 创建根目录

  `mkdir /root/coolq-data`

- 拉取镜像

  ` docker pull coolq/wine-coolq`

- 运行镜像

  `docker run --name=coolq --rm -p 2000:9000 -v /root/coolq-data:/home/user/coolq -e VNC_PASSWD=password -e COOLQ_ACCOUNT=2334790041 coolq/wine-coolq`

- IP:2000访问，用password登入

- 插件目录位于/home/user/coolq/app

- 后台运行镜像

  `docker run --name=coolq -d -p 2000:9000 -v /root/coolq-data:/home/user/coolq -e VNC_PASSWD=password -e COOLQ_ACCOUNT=2334790041 coolq/wine-coolq`

- 后期监控

  查看运行情况 `docker logs coolq`

  启动/停止服务 docker start/stop coolq
