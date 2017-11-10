### jenkins ant jmeter
> [github模板项目地址(接口保密)](https://github.com/xiaominwanglast/uiautomator.git)
---
#### jmeter优势
* 不依赖于界面,测试脚本不需要懂编程,熟悉http请求,熟悉业务流程,对象来编写接口测试用例。
* 测试脚本维护方便,多人共同维护
* 使用参数化以及Jmeter提供的函数功能，可以快速完成测试数据的添加修改等。
* 功能测试和性能测试均可完成
* 可结合jenkins ant/maven做日构建持续集成
* **尽量不要从业务逻辑走接口**，jmeter提供的测试报告模板会让业务变得很乱,找不到问题所在
#### ant优势
* ant核心build.xml比较简单,在于路径的维护
* 运行的jmeter jmx脚本,自动加载jmeter第三方jar包(json的插件，mysql驱动插件)
#### 业务如何走
> 准备条件
```
1.jenkins环境已搭建好,配置系统环境ant,git,java
2.数据准备以主文件python运行，从后台接口与数据库做数据准备
```
>配置
```
1.jenkins定时器Build periodically H 8 * * 1,2,3,4,5 每周1,2,3,4,5早晨8点跑接口
2.python文件放在gitlab上，配置git地址，直接放SSH或者用账号密码
3.配置ant 的build.xml文件
4.配置Extended E-mail Notification邮件，附带log与测试报告
```
>build.xml
```
<?xml version="1.0" encoding="UTF8"?>
<project name="ant-jmeter-test" default="run" basedir=".">
<tstamp>
<format property="time" pattern="yyyy_MM_dd hh:mm" />
</tstamp>
<!-- 需要改成自己本地的 Jmeter 目录-->
<property name="jmeter.home" value="D:\apache-jmeter-3.3" />
<!-- jmeter生成jtl格式的结果报告的路径-->
<property name="jmeter.result.jtl.dir" value="jmeter\report\jtl" />
<!-- jmeter生成html格式的结果报告的路径-->
<property name="jmeter.result.html.dir" value="jmeter\report\html" />
<!-- 生成的报告的前缀-->
<property name="ReportName" value="TestReport" />
<property name="jmeter.result.jtlName" value="${jmeter.result.jtl.dir}/${ReportName}.jtl" />
<property name="jmeter.result.htmlName" value="${jmeter.result.html.dir}/${ReportName}.html" />        
<property name="lib.dir" value="${jmeter.home}/lib"/>  
<path id="xslt.classpath">
<fileset dir="${lib.dir}" includes="xalan*.jar"/>
<fileset dir="${lib.dir}" includes="serializer*.jar"/>
</path>
<target name="run">
<antcall target="test" />
<antcall target="report" />
</target>
<target name="test">
<taskdef name="jmeter" classname="org.programmerplanet.ant.taskdefs.jmeter.JMeterTask" />
<jmeter jmeterhome="${jmeter.home}" resultlog="${jmeter.result.jtlName}">
<!-- 声明要运行的脚本。"*.jmx"指包含此目录下的所有jmeter脚本-->
<testplans dir="xml" includes="*.jmx" />
<property name="jmeter.save.saveservice.output_format" value="xml"/>
</jmeter>
</target>
<target name="report">
<xslt classpathref="xslt.classpath"
force="true"
in="${jmeter.result.jtlName}"
out="${jmeter.result.htmlName}"
style="jmeter-results-detail-report_30.xsl">
<!-- 因为上面生成报告的时候，不会将相关的图片也一起拷贝至目标目录，所以，需要手动拷贝 -->
<param name="showData" expression="${show-data}"/>
<param name="titleReport" expression="${ReportName}"/>
<param name="dateReport" expression="${time}"/>
</xslt>
<copy todir="${jmeter.result.html.dir}">
<fileset dir="${jmeter.home}/extras">
<include name="collapse.png" />
<include name="expand.png" />
</fileset>
</copy>
</target>
</project>
```
>运行
```
1.jenkins定时器运行
2.git自动拉取gitlab python文件
3.构建前python执行python文件，准备jmeter测试数据
4.配置Invoke Ant
5.配置Performance Plugin插件,用于执行后浏览测试报告
6.配置Extended E-mail Notification插件，用于发送邮件报告和报告样式
```
>邮件html报告模板
```
<!DOCTYPE html>  
<html>  
<head>  
<meta charset="UTF-8">  
<title>${ENV, var="JOB_NAME"}-第${BUILD_NUMBER}次构建日志</title>  
</head>    
<body leftmargin="8" marginwidth="0" topmargin="8" marginheight="4"  
    offset="0">  
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
	    ${FILE,path="jmeter/report/html/TestReport.html"}<br/><hr/>
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
> 测试报告如下
![image](http://note.youdao.com/yws/api/personal/file/E0DE4DC910C145388693C7F9FEA40C23?method=download&shareKey=88e908808fd271a39b00370b30541723)

