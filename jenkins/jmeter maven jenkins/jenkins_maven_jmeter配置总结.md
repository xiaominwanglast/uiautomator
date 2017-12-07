### 一.maven
#### maven安装配置
>maven下载官方地址[Apache Maven Project](http://maven.apache.org/download.cgi)
- 需要安装jdk
- 配置path环境，安装成功后输入mvn -v如下信息表明安装成功
```
Apache Maven 3.5.0 (ff8f5e7444045639af65f6095c62210b5713f426; 2017-04-04T03:39:06+08:00)
Maven home: E:\apache-maven-3.5.0\bin\..
Java version: 1.8.0_144, vendor: Oracle Corporation
Java home: C:\Program Files\Java\jdk1.8.0_144
Default locale: zh_CN, platform encoding: GBK
OS name: "windows 10", version: "10.0", arch: "amd64", family: "windows"
```
- 默认生成的本地仓库在${user.home}/.m2/repository，可在maven/confg/settings.xml配置文件看到<localRepository>...</localRepository>路径，若自定义路径取消注释，加入路径后,下面简单创建maven项目后及会在自定义仓库路径下download依赖包(*首次download会很多很慢*)
 ```
 mvn archetype:generate -DgroupId=com.yiibai -DartifactId=NumberGenerator -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
 ```
#### maven资源库
>检查pom文件，确定依赖下载
```
graph LR
a[maven本地资源库] -->b[maven中央资源库]
b -->c[java.net远程仓库]
c-->d[找到ok]
c-->e[找不到提示错误]
```
- 添加java.net或是JBoss远程存储库，确保依赖文件获取正常执行
```
<project ...>
<repositories>
    <repository>
      <id>java.net</id>
      <url>https://maven.java.net/content/repositories/public/</url>
    </repository>
 </repositories>
</project>
```
```
<project ...>
    <repositories>
      <repository>
	<id>JBoss repository</id>
	<url>http://repository.jboss.org/nexus/content/groups/public/</url>
      </repository>
    </repositories>
</project>
```
#### maven依赖机制
>如何定位依赖位置
- groupId,artifactId来定位maven仓库坐标,举例
```
<groupId>log4j</groupId>
<artifactId>log4j</artifactId>
<version>1.2.14</version>
```
>说明maven坐标为仓库repository/log4j，模块路径为repository/log4j/log4j,版本路径repository/log4j/log4j/1.2.14
- pom.xml文件中加入maven坐标
```
<dependencies>
    <dependency>
	<groupId>log4j</groupId>
	<artifactId>log4j</artifactId>
	<version>1.2.14</version>
    </dependency>
</dependencies>
```
#### maven创建项目
>maven基础项目目录
```
graph LR
wp[project] --> a[src]
wp --> d[pom.xml]
a --> b[main]
a --> c[test]
b --> e[java]
b --> h[resources]
c --> i[java]
c --> k[resources]
```
### 二.maven,jmeter,jenkins
#### maven运行jmeter脚本
>maven运行jmeter脚本目录
>>创建文件目录
```
graph LR
wp[project] --> a[src]
wp --> d[pom.xml]
a --> c[test]
c --> i[java]
c --> k[resources]
c --> b[jmeter]
k --> h[jmeter-results-detail-report_21.xsl]
k --> j[jmeter.results.shanhe.me.xsl]
b --> l[HTTP_test1.jmx]
b --> m[HTTP_test2.jmx]
```
>>执行pom.xml文件后,在project下多出了一个target目录(src目录跟上面一样)
```
graph LR
wp[project] --> a[src]
wp --> d[pom.xml]
wp -->b[target]
b -->c[jmeter]
c -->e[html]
e -->j[html测试报告]
c -->f[results]
f -->k[.jtl结果文件]
c -->g[testfiles]
g -->l[.jmx测试文件]
c -->h[logs]
h -->m[测试log]
```
- 注意jmeter脚本为另存为的测试计划.jmx文件。
- 每个http请求加入断句，**加入结果查看树这类，会在maven运行时报NoGUI sendbytes错误，是插件版本问题**。
- maven默认执行jmeter脚本位置为src\test\jmeter\\\*.jmx。
- src/test/resources为项目html生成模板文件(可以在apache-jmeter-3.3\extras\目录下看到)

#### jenkins配置与插件
- Maven Integration plugin maven项目插件
- Performance Plugin **最新插件版本与jenkins最新2.73版本不兼容问题**，会出现安装了Performance Plugin不能选用。目前是降低版本使用2.0版本配合jenkins2.73版本
- [Publish HTML reports](https://wiki.jenkins.io/display/JENKINS/HTML+Publisher+Plugin)插件下载用于展示html测试报告
- Extended E-mail Notification 邮件插件安装(2.6.0版本),**注意系统里面因为这个插件也要设置一次账号密码，若是项目含有email插件，系统里必须要设置两次账号和密码**
- maven的默认使用仓库为${user.home}/.m2/repository
- jenkins执行目录在系统配置中默认是安装目录，设置JENKINS_HOME系统环境变量规定jenkins目录(首先要安装在这个目录下)

  ##### Performance Plugin插件
  - Performance report中加入jmeter，默认路径是workpace，执行pom.xml生成一个target目标文件，此时路径设置为target\jmeter\results\\\*.jtl
  ##### Publish HTML reports插件
  - HTML directory to archive 指定html报告存放的目录target/jmeter/html
  - Index page[s] 指定报告名字，**确保src/target/jmeter/html/目录下的html报告名字与此处填写的报告名字一致，否则会报404错误**
  - Report title 为job/下的目录名字，也是报告的配置文件名
  ##### Extended E-mail Notification插件
  ###### 项目中构建配置
  - Project Recipient List 添加邮件发送人
  - Attachments 添加附件target/jmeter/html/*\.html，**确保是工作目录/target/jmeter/html/文件**
  - Attach Build Log 添加build log(日志)选择Attach Build Log
  - Triggers 触发邮件发送，选择发送对象与当前状态构建发送(个人选择always,选择Recipient List)
  ###### 系统设置邮件
  - Default Subject 邮件标题，自己定义
  - Default Content 邮件内容，(需要定义邮件html报告模板,自定义模板记录如下)
```
<!DOCTYPE html>  
<html>  
<head>  
<meta charset="UTF-8">  
<title>${ENV, var="JOB_NAME"}-第${BUILD_NUMBER}次构建日志</title>  
</head>    
<body leftmargin="8" marginwidth="0" topmargin="8" marginheight="4"  offset="0">  
    <table width="95%" cellpadding="0" cellspacing="0"  
        style="font-size: 11pt; font-family: Tahoma, Arial, Helvetica, sans-serif">  
        <tr>  
            <td>(本邮件是程序自动下发的，请勿回复！)</td>  
        </tr>  
        <tr>  
            <td><h2>  
                    <font color="#0000FF">构建结果 - ${BUILD_STATUS}</font>  
                </h2></td>  
        </tr>  
       	<tr>
	    ${FILE,path="target/jmeter/html/HTTP_test1.html"}<br/><hr/>
	</tr>
        <tr>  
            <td><br />  
            <b><font color="#0B610B">构建信息</font></b>  
            <hr size="2" width="100%" align="center" /></td>  
        </tr>  
        <tr>  
            <td>  
                <ul>  
                    <li>项目名称 ： ${PROJECT_NAME}</li>  
                    <li>构建编号 ： 第${BUILD_NUMBER}次构建</li>   
                    <li>触发原因： ${CAUSE}</li>  
                    <li>构建日志： <a href="${BUILD_URL}console">${BUILD_URL}console</a></li>  
                    <li>构建  Url ： <a href="${BUILD_URL}">${BUILD_URL}</a></li>  
                    <li>工作目录 ： <a href="${PROJECT_URL}ws">${PROJECT_URL}ws</a></li>  
                    <li>项目  Url ： <a href="${PROJECT_URL}">${PROJECT_URL}</a></li>  
                </ul>  
            </td>  
        </tr>  
    </table>  
</body>  
</html>  
```
#### maven pom.xml配置
>现在使用的pom.xml模板，注意如下几点
- <properties>····</properties>设置环境变量${project.build.directory}为target，
- 加载仓库repository/com/lazerycode/jmeter目录下jmeter-maven-plugin插件在verify阶段执行jmeter
- 加载仓库repository/org/codehaus/mojo目录下xml-maven-plugin xml转换成html文件，模板库路径src\test\resources\
- 2.1.0jmeter-maven-plugin版本可以兼容jmeter 结果查看树
```
			<dependencies>
				<dependency>
					<groupId>net.sf.saxon</groupId>
					<artifactId>saxon</artifactId>
					<version>8.7</version>
				</dependency>
			</dependencies>
```
- **上段依赖的插件可以解决maven 报告NAN问题，这个问题困扰很久** [参考文章](https://www.2cto.com/kf/201708/671784.html)
- jmeter json插件的依赖问题解决[参考网站](http://www.cnblogs.com/shengulong/p/6562291.html)
> 添加依赖插件
> copy插件到依赖目录，默认是执行文件的target/jmeter/bin下面
> 30的模板是[参考文章](http://www.cnblogs.com/jaychang/p/5881525.html)
> 原文参考[参考文章](http://www.cnblogs.com/a2602162453/p/5180253.html)
```
		 <dependency>
			<groupId>kg.apc</groupId>
			<artifactId>jmeter-plugins-json</artifactId>
			<version>2.6</version>
		</dependency>
		<dependency>
			<groupId>kg.apc</groupId>
			<artifactId>jmeter-plugins-cmn-jmeter</artifactId>
			<version>0.3</version>
		</dependency>
		<dependency>
			<groupId>kg.apc</groupId>
			<artifactId>jmeter-plugins-manager</artifactId>
			<version>0.11</version>
		</dependency>
```
```
		<plugin>  
        <groupId>org.apache.maven.plugins</groupId>  
        <artifactId>maven-dependency-plugin</artifactId>  
        <version>2.8</version>  
        <executions>  
            <execution>  
                <phase>package</phase>  
                <goals>  
                    <goal>copy-dependencies</goal>  
                </goals>  
            </execution>  
        </executions>  
         <configuration>  
                 <includeArtifactIds>jmeter-plugins-json,jmeter-plugins-cmn-jmeter,jmeter-plugins-manager</includeArtifactIds>  
                 <outputDirectory>target/jmeter/lib/ext</outputDirectory>
         </configuration>
		</plugin>  
```
- 结果报告展示格式问题，在系统脚本命令行输入，System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")
```
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>MavenDome_git_test</groupId>
  <artifactId>test</artifactId>
  <version>0.0.1-SNAPSHOT</version>
  <packaging>jar</packaging>

  <name>test</name>
  <url>http://maven.apache.org</url>
    <dependencies>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>3.8.1</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
  <properties>
         <jmeter.result.jtl.dir>${project.build.directory}\jmeter\results</jmeter.result.jtl.dir>
        <jmeter.result.html.dir>${project.build.directory}\jmeter\html</jmeter.result.html.dir>
        <jmeter.result.html.dir1>${project.build.directory}\jmeter\html1</jmeter.result.html.dir1>
        <ReportName>TestReport</ReportName>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>
  <build>
	<plugins>
		<plugin>
			<groupId>com.lazerycode.jmeter</groupId>  
			<artifactId>jmeter-maven-plugin</artifactId>  
			<version>2.1.0</version>  
            <configuration>
                <resultsFileFormat>xml</resultsFileFormat>
                <ignoreResultFailures>true</ignoreResultFailures>
                <testResultsTimestamp>flase</testResultsTimestamp>
             </configuration>
			<executions>  
				<execution>  
					<id>jmeter-tests</id>  
					<phase>verify</phase>  
					<goals>  
						<goal>jmeter</goal>  
					</goals>  
				</execution>  
			</executions>  
		</plugin> 
		<plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>xml-maven-plugin</artifactId>
                <version>1.0-beta-3</version>
                <executions>
                    <execution>
                        <phase>verify</phase>
                        <goals>
                            <goal>transform</goal>
                        </goals>
                    </execution>
                </executions>
                <configuration>
                    <transformationSets>
                        <transformationSet>
                            <dir>${jmeter.result.jtl.dir}</dir>
                            <stylesheet>src\test\resources\jmeter-results-detail-report_21.xsl</stylesheet>
                            <outputDir>${jmeter.result.html.dir}</outputDir>
                            <fileMappers>
                                <fileMapper
                                    implementation="org.codehaus.plexus.components.io.filemappers.FileExtensionMapper">
                                    <targetExtension>html</targetExtension>
                                </fileMapper>
                            </fileMappers>
                        </transformationSet>
                        <transformationSet>
                            <dir>${jmeter.result.jtl.dir}</dir>
                            <stylesheet>src\test\resources\jmeter.results.shanhe.me.xsl</stylesheet>
                            <outputDir>${jmeter.result.html.dir1}</outputDir>
                            <fileMappers>
                                <fileMapper
                                    implementation="org.codehaus.plexus.components.io.filemappers.FileExtensionMapper">
                                    <targetExtension>html</targetExtension>
                                </fileMapper>
                            </fileMappers>
                        </transformationSet>
                    </transformationSets>
                </configuration>
			<dependencies>
				<dependency>
					<groupId>net.sf.saxon</groupId>
					<artifactId>saxon</artifactId>
					<version>8.7</version>
				</dependency>
			</dependencies>
            </plugin>
		</plugins>
	<defaultGoal>clean</defaultGoal>
   </build>
</project>


```
#### jmeter，git，jenkins
>jmeter脚本在git目录如下
```
graph LR
A[git项目名] -->B[pom.xml]
A -->C[src]
C -->D[test]
C -->E[main]
D -->F[jmeter]
D -->G[resources]
F -->H[jmx脚本文件]
G -->I[报告模板文件]
I -->J[jmeter.results.shanhe.me.xsl]
I -->K[jmeter-results-detail-report_21.xsl]
```
>jenkins运行
```
graph TD
A[git remote] -->|配置git私钥对远程公钥连接|B(git地址)
B -->|init仓库,fetch文件|c(workpace/project)
c -->|执行 pom.xml|d(maven verify)
d -->|html report/send email|e(over)
```

>jmeter内置函数用法
- ${__urlencode('${token}'))} url地址中中文urlencode转码
- ${__time(,)}13位数，${__time(/1000,)}10位数，${__time(yyyy-MM-dd,)}日期格式，全格式${__time(YMDHMS,)}[见文章](http://blog.csdn.net/dreamtl/article/details/68957447)
