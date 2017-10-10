## Jenkins
>官方下载地址[Jenkins下载](https://jenkins.io/index.html)
#### 配置
- maven自行下载[maven官方地址](http://maven.apache.org/download.cgi),选择Link-gz压缩包
>>配置环境变量,1.新建环境变量MAVEN_HOME,添加安装目录,2.path下添加%MAVEN_HOME%\bin,cmd中输入mvn -v,输出正常日志代表ok
```
cmd.log
Apache Maven 3.5.0 (ff8f5e7444045639af65f6095c62210b5713f426; 2017-04-04T03:39:06+08:00)
Maven home: C:\apache-maven-3.5.0\bin\..
Java version: 1.8.0_144, vendor: Oracle Corporation
Java home: C:\Program Files\Java\jdk1.8.0_144\jre
Default locale: zh_CN, platform encoding: GBK
OS name: "windows 10", version: "10.0", arch: "amd64", family: "windows"
```
- JDK自行下载[jdk官方网址](http://www.oracle.com/technetwork/cn/java/javase/downloads/jdk8-downloads-2133151-zhs.html)
>>配置环境变量，1.新建环境变量JAVA_HOME,添加安装目录，2.path下放入配置信息
```
java -version
java version "1.8.0_144"
Java(TM) SE Runtime Environment (build 1.8.0_144-b01)
Java HotSpot(TM) 64-Bit Server VM (build 25.144-b01, mixed mode)
```
- git下载
>>git下载地址[官方网址](https://git-scm.com/downloads),path中配置cmd安装目录
```
git --version
git version 2.13.0.windows.1
```

#### 安装jenkins
- 下载的jenkins.smi直接点击安装后打开localhost:8080,安装插件，设置账号密码
- 开始配置jdk,maven,git。在系统管理-->Global Tool Configuration里面JDK安装与Maven安装模块，新建name与本地环境变量对应的地址，git默认是git.exe程序，需要改成对应的本地执行目录

#### 配置jenkins 
- jmeter -n -t HTTP_test1.jmx -l result.jtl
- jmeter -n -t HTTP_test.jmx -l result.jtl
  