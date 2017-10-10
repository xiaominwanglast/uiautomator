## git使用方法
#### 备注：参考目录可以到 [推荐！手把手教你使用Git](http://blog.jobbole.com/78960/)
- **安装git**
  >安装后注意配置信息,git身份认证，再次使用时类似于修改信息
  ##### *配置*
  -  git config --global user.name "wangxm",
  -  git config --global user.email "2274052689@qq.com"
  ***
- **创建文件**
  >先进入指定目的，再创建文件，然后init初始化
  ##### *步骤*
    -  mkdir file,
    -  cd file,
    -  git init(目的是让文件可被git管理，生成.git文件)
  ***
- **基本工作**
  >工作区文件变动后，add到.git的暂存区，然后commit提交到仓库
  ##### *步骤*
    - git add readme.txt
    - git commit -m "备注信息"
    - git status (*查看工作状态,此时为clean*)
    - 修改readme.txt文件后
    - git status(*会有颜色提示 <font color=darkred>modified readme.txt</font>*)
    - (*此时未被commit*)git diff readme.txt (*查看改动内容*)
    - git add readme.txt
    - git status (*会有颜色提示 <font color=blue>modified readme.txt</font>*)
    
   ##### *备注*
    >多次add文件,add可以是文件或者文件夹
  ***
- **版本回退**
  >版本回退指的是本地仓库的处理
  ##### *步骤*
    - git log(查看<font color=orange>版本号</font>)，若是需要按行显示的话，git log --pretty=oneline
    - 回退版本命令
    ```cmd
    git reset --hard HEAD^
    git reset --hard HEAD~1
    ```
    - git reflog(**回退最新版本**),
    ```cmd
    git reset --hard 版本号
    ```
    - cat readme.txt查看是否已经恢复
  ***
- **撤销修改**
  >1.手动删除，2.git reset --hard HEAD^
  ##### *步骤*
    - git checkout --readme.txt 丢弃工作区修改(未放到暂存区，撤销与版本库一致，已经放入暂存区，撤销与暂存区一致)
    - 删除文件 rm 文件(已经commit文件)
    - git checkout -- b.txt 恢复文件
  ***
- **远程仓库**
  >查看用户下的.ssh如果没有ssh-keygen  -t rsa –C “youremail@example.com”，默认路径获取秘钥
  ##### *步骤*
  ##### 方法一
    - 添加ssh-keys
    - Create repository
    - 输入如下命令,第一次链接要用u
    ```
    git remote add origin https://github.com/tugenhua0707/testgit.git
    git push -u origin master
    ```
    - 后续提交只需要 git push origin master
  ##### 方法二
  - new repository
  - 勾选 REAMDE
  - Create repository
  - 选好本地文件夹位置，git clone后则链接上远程git，本地也会生成一个.git文件




    192.168.