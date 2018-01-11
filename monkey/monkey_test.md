### monkey
#### 一、Monkey测试简介
##### Monkey测试是Android平台自动化测试的一种手段，通过Monkey程序模拟用户触摸屏幕、滑动Trackball、按键等操作来对设备上的程序进行压力测试，检测程序多久的时间会发生可能的异常。
* Monkey程序由Android系统自带，使用Java语言写成，在Android文件系统中的存放路径是：/system/framework/monkey.jar；
* Monkey.jar程序是由一个名为“monkey”的Shell脚本来启动执行，shell脚本在Android文件系统中的存放路径是：/system/bin/ monkey；
* 通过在CMD窗口中执行: adb shell monkey｛+命令参数｝来进行Monkey测试。(**注意部分机型需要在开发者选项中勾选USB模拟点击，否则会不运行或报Kill问题**)
#### 二、Monkey参数
> ##### adb shell monkey –help可以查看详细命令
1) 参数 -p 指定一个或多个包
> 指定包之后，Monkey将只允许系统启动指定的APP。如果不指定包，Monkey将允许系统启动设备中的所有APP。
* 指定一个包： adb shell monkey -p com.htc.Weather 100 [100是事件计(即让Monkey程序模拟100次随机用户事件)]。
* 指定多个包：adb shell monkey -p com.htc.Weather –p com.htc.pdfreader  -p com.htc.photo.widgets 100
* 不指定包：adb shell monkey 100
2) 参数 -v 指定日志详细
>  分为三级信息日志，-v -v -v三级日志最详细, -v一级日志缺省值信息量少
日志级别 Level0 
* 示例 adb shell monkey -p com.ddinfo.ddmall –v 100,说明缺省值，仅提供启动提示、测试完成和最终结果等少量信息
* 日志级别 Level 1
示例 adb shell monkey -p com.ddinfo.ddmall –v -v 100,说明提供较为详细的日志，包括每个发送到Activity的事件信息
* 日志级别 Level 2
示例 adb shell monkey -p com.ddinfo.ddmall –v -v –v 100,说明最详细的日志，包括了测试中选中/未选中的Activity信息
3) 参数 -s 用于指定伪随机数生成器的seed值
> 如果seed相同，则两次Monkey测试所产生的事件序列也相同的。
* Monkey测试1：adb shell monkey -p com.htc.Weather –s 10 100|| Monkey 测试2：adb shell monkey -p com.htc.Weather–s 10 100 运行展示的行为是完全一致的
4) 参数 --throttle 模拟用户操作时间的延迟时间，单位是毫秒1000ms=1s
* adb shell monkey -p com.htc.Weather –throttle 3000 100
5) 参数 --ignore-crashes 
> 用于指定当应用程序崩溃时，Monkey是否停止运行。如果使用此参数，即使应用程序崩溃，Monkey依然会发送事件，直到事件计数完成。
* 示例1：adb shellmonkey -p com.htc.Weather --ignore-crashes 1000
  测试过程中即使Weather程序崩溃，Monkey依然会继续发送事件直到事件数目达到1000为止；
* 示例2：adb shellmonkey -p com.htc.Weather 1000
  测试过程中，如果Weather程序崩溃，Monkey将会停止运行。
6) 参数 --ignore-timeouts 
> 用于指定当应用程序发生ANR（Application NoResponding）错误时，Monkey是否停止运行。如果使用此参数，即使应用程序发生ANR错误，Monkey依然会发送事件，直到事件计数完成。
7) 参数 --ignore-security-exceptions
> 用于指定当应用程序发生许可错误时（如证书许可，网络许可等），Monkey是否停止运行。如果使用此参数，即使应用程序发生许可错误，

8) 参数 --kill-process-after-error
>用于指定当应用程序发生错误时，是否停止其运行。如果指定此参数，当应用程序发生错误时，应用程序停止运行并保持在当前状态（注意应用程序仅是静止在发生错误时的状态，系统并不会结束该应用程序的进程）。
9) 参数 --monitor-native-crashes
>用于指定是否监视并报告应用程序发生崩溃的本地代码。
10) 参数  --pct-｛+事件类别｝｛+事件类别百分比｝
>用于指定每种类别事件的数目百分比（在Monkey事件序列中，该类事件数目占总事件数目的百分比）
##### *详细说明参数--pct-，并且主要分析log日志来说明monkey运行过程*
* --pct-touch+百分比 调整触摸事件的百分比,仅限于屏幕上某个点的down-up事件，adb shell monkey --pct-touch 100 -v -v -v 10 (**为了说明--pct-touch参数，故意把百分比写满 100来分析问题，**)
```
运行日志 备注{**内容}为个人后追加解释
C:\Users\hahah>adb shell monkey --throttle 1000 --pct-touch 100 -v -v -v 10
:Monkey: seed=1510815654118 count=10   {**未定义monkey的seed时随机定义一个seed值,count是事件综合10}
:IncludeCategory: android.intent.category.LAUNCHER {**要运行的package内活动名}
:IncludeCategory: android.intent.category.MONKEY {**要运行的package内活动名}
// Selecting main activities from category android.intent.category.LAUNCHER  {**选择主要activities，未定义包名则所有包活动都作为main activity}
//   + Using main activity com.android.gallery3d.vivo.GalleryTabActivity (from package com.vivo.gallery)
//   + Using main activity com.vivo.childrenmode.activity.ChildHomeActivity (from package com.vivo.childrenmode)
//   + Using main activity com.android.contacts.DialtactsContactsEntryActivity (from package com.android.contacts)
//   + Using main activity com.android.dialer.TwelveKeyDialer (from package com.android.dialer)
//   + Using main activity com.vivo.email.activity.Welcome (from package com.vivo.email)
//   + Using main activity com.android.mms.ui.ConversationList (from package com.android.mms)
//   + Using main activity com.android.settings.Settings (from package com.android.settings)
//   + Using main activity com.android.bbksoundrecorder.SoundRecorder (from package com.android.bbksoundrecorder)
//   + Using main activity com.android.VideoPlayer.VideoPlayer (from package com.android.VideoPlayer)
//   + Using main activity com.bbk.calendar.MainActivity (from package com.bbk.calendar)
//   + Using main activity com.android.camera.CameraActivity (from package com.android.camera)
//   + Using main activity com.android.bbkmusic.WidgetToTrackActivity (from package com.android.bbkmusic)
//   + Using main activity com.chaozh.iReader.ui.activity.WelcomeActivity (from package com.chaozh.iReader)
//   + Using main activity com.bbk.theme.Theme (from package com.bbk.theme)
//   + Using main activity com.baidu.baidumaps.WelcomeScreen (from package com.baidu.BaiduMap)
//   + Using main activity com.tencent.assistant.activity.SplashActivity (from package com.tencent.android.qqdownloader)
//   + Using main activity com.android.bbkcalculator.Calculator (from package com.android.bbkcalculator)
//   + Using main activity com.bbk.cloud.activities.BBKCloudHomeScreen (from package com.bbk.cloud)
//   + Using main activity com.vivo.FMRadio.FMRadio (from package com.vivo.FMRadio)
//   + Using main activity com.android.filemanager.FileManagerActivity (from package com.android.filemanager)
//   + Using main activity com.android.notes.Notes (from package com.android.notes)
//   + Using main activity com.android.BBKClock.Timer (from package com.android.BBKClock)
//   + Using main activity com.vivo.weather.WeatherMain (from package com.vivo.weather)
//   + Using main activity com.vivo.compass.CalibrationActivity (from package com.vivo.compass)
//   + Using main activity com.iqoo.secure.MainGuideActivity (from package com.iqoo.secure)
//   + Using main activity com.vivo.Tips.MainActivity (from package com.vivo.Tips)
//   + Using main activity com.vivo.space.ui.LogoActivity (from package com.vivo.space)
//   + Using main activity com.bbk.appstore.ui.AppStore (from package com.bbk.appstore)
//   + Using main activity com.vivo.game.ui.LogoActivity (from package com.vivo.game)
//   + Using main activity com.vivo.browser.BrowserActivity (from package com.vivo.browser)
//   + Using main activity com.wuba.activity.launch.LaunchActivity (from package com.wuba)
//   + Using main activity com.ddinfo.ddmall.activity.menu.HelloActivity (from package com.ddinfo.ddmall)
//   + Using main activity com.sankuai.meituan.activity.Welcome (from package com.sankuai.meituan)
//   + Using main activity com.android.bbk.lockscreen3.LockScreenActivity (from package com.android.bbk.lockscreen3)
//   + Using main activity com.vivo.easyshare.activity.SplashScreenActivity (from package com.vivo.easyshare)
//   + Using main activity com.youku.phone.ActivityWelcome (from package com.youku.phone)
//   + Using main activity com.sina.weibo.SplashActivity (from package com.sina.weibo)
//   + Using main activity com.ss.android.article.news.activity.SplashBadgeActivity (from package com.ss.android.article.news)
//   + Using main activity com.tencent.mm.ui.LauncherUI (from package com.tencent.mm)
//   + Using main activity com.ddinfo.salesman.activity.LaunchActivity (from package com.ddinfo.salesman)
//   + Using main activity io.appium.settings.Settings (from package io.appium.settings)
//   + Using main activity com.sh.gj.MainActivity (from package com.sh.gj)
//   + Using main activity io.appium.unlock.Unlock (from package io.appium.unlock)
//   + Using main activity com.bbk.iqoo.feedback.activities.UserFeedBackActivity (from package com.bbk.iqoo.feedback)
//   + Using main activity com.jingdong.app.mall.main.MainActivity (from package com.jingdong.app.mall)
//   + Using main activity com.taobao.tao.welcome.Welcome (from package com.taobao.taobao)
//   + Using main activity com.tencent.mobileqq.activity.SplashActivity (from package com.tencent.mobileqq)
//   + Using main activity com.tencent.qqlive.ona.activity.WelcomeActivity (from package com.tencent.qqlive)
//   + Using main activity ctrip.business.splash.CtripSplashActivity (from package ctrip.android.view)
// Selecting main activities from category android.intent.category.MONKEY
//   + Using main activity com.vivo.childrenmode.activity.ChildHomeActivity (from package com.vivo.childrenmode)
//   + Using main activity com.android.settings.Settings$RunningServicesActivity (from package com.android.settings)
//   + Using main activity com.android.settings.Settings$StorageUseActivity (from package com.android.settings)
//   + Using main activity com.bbk.launcher2.Launcher (from package com.bbk.launcher2)
//   + Using main activity com.bbk.scene.launcher.theme.SceneLauncherThemeMainActivity (from package com.bbk.scene.launcher.theme)
//   + Using main activity com.iqoo.engineermode.EngineerMode (from package com.iqoo.engineermode)
//   + Using main activity com.android.systemui.vivo.common.monkeytest.MonkeyTestActivity (from package com.android.systemui)
// Seeded: 1510815654118 {**seeded 种子同初始化一致}
// Event percentages: {**事件百分比，可以都看到--pct-touch默认event类型为0，所有事件总和必为100%}
//   0: 100.0%
//   1: 0.0%
//   2: 0.0%
//   3: 0.0%
//   4: -0.0%
//   5: -0.0%
//   6: 0.0%
//   7: 0.0%
//   8: 0.0%
//   9: 0.0%
//   10: 0.0%
//   11: 0.0%
{**跳转到主事件，未定义包则随机选中了com.bbk.iqoo.feedback，并且启动了.activities.UserFeedBackActivity}
:Switch: #Intent;action=android.intent.action.MAIN;category=android.intent.category.LAUNCHER;launchFlags=0x10200000;component=com.bbk.iqoo.feedback/.activities.UserFeedBackActivity;end
    // Allowing start of Intent { act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER] cmp=com.bbk.iqoo.feedback/.activities.UserFeedBackActivity } in package com.bbk.iqoo.feedback {**代表允许此跳转}
Sleeping for 1000 milliseconds
:Sending Touch (ACTION_DOWN): 0:(167.0,734.0)
:Sending Touch (ACTION_UP): 0:(178.81384,737.14557) {**sleep 1秒可以看出--pct-touch的down-up事件是两个步骤，但是作为一个整体动作，执行完毕然后进入延迟等待}
Sleeping for 1000 milliseconds
:Sending Touch (ACTION_DOWN): 0:(453.0,1107.0)
:Sending Touch (ACTION_UP): 0:(440.52118,1109.9523)
Sleeping for 1000 milliseconds
:Sending Touch (ACTION_DOWN): 0:(56.0,500.0)
:Sending Touch (ACTION_UP): 0:(53.049572,499.63184)
Sleeping for 1000 milliseconds
:Sending Touch (ACTION_DOWN): 0:(500.0,420.0)
:Sending Touch (ACTION_UP): 0:(487.34482,410.93445)
Sleeping for 1000 milliseconds
:Sending Touch (ACTION_DOWN): 0:(170.0,1209.0)
Events injected: 10 {**注入事件10，数一下动作只有9个，其实还有switch的一个启动动作，则共10个}
:Sending rotation degree=0, persist=false  {**发送屏幕翻转 度=0，存留=假}
:Dropped: keys=0 pointers=0 trackballs=0 flips=0 rotations=0 {**丢弃：键=0，指针=0，轨迹球=0，键盘轻弹=0，屏幕翻转=0}
## Network stats: elapsed time=5064ms (0ms mobile, 0ms wifi, 5064ms not connected) {**网络状态：占用时间=5064ms（手机0ms，wifi0ms，未连接5064ms}
// Monkey finished  {**测试完成}

C:\Users\hahah>
```
* --pct-motion+百分比 调整动作事件的百分比(动作事件由屏幕上某处的一个down事件、一系列的伪随机事件和一个up事件组成),
adb shell monkey -p com.ddinfo.ddmall --pct-motion 100 -v -v -v 10，**如下新加package运行日志不相同点**
```
运行日志 备注{**内容}为个人后追加解释
C:\Users\hahah>adb shell monkey -p com.ddinfo.ddmall --pct-motion 100 -v -v -v 10
:Monkey: seed=1510817506766 count=10
:AllowPackage: com.ddinfo.ddmall {**定义了包，则只允许这个包运行}
:IncludeCategory: android.intent.category.LAUNCHER
:IncludeCategory: android.intent.category.MONKEY
// Selecting main activities from category android.intent.category.LAUNCHER {**如下可以看到主活动除了定义的包的活动，其他都是not using不可用}
//   - NOT USING main activity com.android.gallery3d.vivo.GalleryTabActivity (from package com.vivo.gallery)
//   - NOT USING main activity com.vivo.childrenmode.activity.ChildHomeActivity (from package com.vivo.childrenmode)
//   - NOT USING main activity com.android.contacts.DialtactsContactsEntryActivity (from package com.android.contacts)
//   - NOT USING main activity com.android.dialer.TwelveKeyDialer (from package com.android.dialer)
//   - NOT USING main activity com.vivo.email.activity.Welcome (from package com.vivo.email)
//   - NOT USING main activity com.android.mms.ui.ConversationList (from package com.android.mms)
//   - NOT USING main activity com.android.settings.Settings (from package com.android.settings)
//   - NOT USING main activity com.android.bbksoundrecorder.SoundRecorder (from package com.android.bbksoundrecorder)
//   - NOT USING main activity com.android.VideoPlayer.VideoPlayer (from package com.android.VideoPlayer)
//   - NOT USING main activity com.bbk.calendar.MainActivity (from package com.bbk.calendar)
//   - NOT USING main activity com.android.camera.CameraActivity (from package com.android.camera)
//   - NOT USING main activity com.android.bbkmusic.WidgetToTrackActivity (from package com.android.bbkmusic)
//   - NOT USING main activity com.chaozh.iReader.ui.activity.WelcomeActivity (from package com.chaozh.iReader)
//   - NOT USING main activity com.bbk.theme.Theme (from package com.bbk.theme)
//   - NOT USING main activity com.baidu.baidumaps.WelcomeScreen (from package com.baidu.BaiduMap)
//   - NOT USING main activity com.tencent.assistant.activity.SplashActivity (from package com.tencent.android.qqdownloader)
//   - NOT USING main activity com.android.bbkcalculator.Calculator (from package com.android.bbkcalculator)
//   - NOT USING main activity com.bbk.cloud.activities.BBKCloudHomeScreen (from package com.bbk.cloud)
//   - NOT USING main activity com.vivo.FMRadio.FMRadio (from package com.vivo.FMRadio)
//   - NOT USING main activity com.android.filemanager.FileManagerActivity (from package com.android.filemanager)
//   - NOT USING main activity com.android.notes.Notes (from package com.android.notes)
//   - NOT USING main activity com.android.BBKClock.Timer (from package com.android.BBKClock)
//   - NOT USING main activity com.vivo.weather.WeatherMain (from package com.vivo.weather)
//   - NOT USING main activity com.vivo.compass.CalibrationActivity (from package com.vivo.compass)
//   - NOT USING main activity com.iqoo.secure.MainGuideActivity (from package com.iqoo.secure)
//   - NOT USING main activity com.vivo.Tips.MainActivity (from package com.vivo.Tips)
//   - NOT USING main activity com.vivo.space.ui.LogoActivity (from package com.vivo.space)
//   - NOT USING main activity com.bbk.appstore.ui.AppStore (from package com.bbk.appstore)
//   - NOT USING main activity com.vivo.game.ui.LogoActivity (from package com.vivo.game)
//   - NOT USING main activity com.vivo.browser.BrowserActivity (from package com.vivo.browser)
//   - NOT USING main activity com.wuba.activity.launch.LaunchActivity (from package com.wuba)
//   + Using main activity com.ddinfo.ddmall.activity.menu.HelloActivity (from package com.ddinfo.ddmall)  {** 可以看到定义的主活动名可以被使用}
//   - NOT USING main activity com.sankuai.meituan.activity.Welcome (from package com.sankuai.meituan)
//   - NOT USING main activity com.android.bbk.lockscreen3.LockScreenActivity (from package com.android.bbk.lockscreen3)
//   - NOT USING main activity com.vivo.easyshare.activity.SplashScreenActivity (from package com.vivo.easyshare)
//   - NOT USING main activity com.youku.phone.ActivityWelcome (from package com.youku.phone)
//   - NOT USING main activity com.sina.weibo.SplashActivity (from package com.sina.weibo)
//   - NOT USING main activity com.ss.android.article.news.activity.SplashBadgeActivity (from package com.ss.android.article.news)
//   - NOT USING main activity com.tencent.mm.ui.LauncherUI (from package com.tencent.mm)
//   - NOT USING main activity com.ddinfo.salesman.activity.LaunchActivity (from package com.ddinfo.salesman)
//   - NOT USING main activity io.appium.settings.Settings (from package io.appium.settings)
//   - NOT USING main activity com.sh.gj.MainActivity (from package com.sh.gj)
//   - NOT USING main activity io.appium.unlock.Unlock (from package io.appium.unlock)
//   - NOT USING main activity com.bbk.iqoo.feedback.activities.UserFeedBackActivity (from package com.bbk.iqoo.feedback)
//   - NOT USING main activity com.jingdong.app.mall.main.MainActivity (from package com.jingdong.app.mall)
//   - NOT USING main activity com.taobao.tao.welcome.Welcome (from package com.taobao.taobao)
//   - NOT USING main activity com.tencent.mobileqq.activity.SplashActivity (from package com.tencent.mobileqq)
//   - NOT USING main activity com.tencent.qqlive.ona.activity.WelcomeActivity (from package com.tencent.qqlive)
//   - NOT USING main activity ctrip.business.splash.CtripSplashActivity (from package ctrip.android.view)
// Selecting main activities from category android.intent.category.MONKEY
//   - NOT USING main activity com.vivo.childrenmode.activity.ChildHomeActivity (from package com.vivo.childrenmode)
//   - NOT USING main activity com.android.settings.Settings$RunningServicesActivity (from package com.android.settings)
//   - NOT USING main activity com.android.settings.Settings$StorageUseActivity (from package com.android.settings)
//   - NOT USING main activity com.bbk.launcher2.Launcher (from package com.bbk.launcher2)
//   - NOT USING main activity com.bbk.scene.launcher.theme.SceneLauncherThemeMainActivity (from package com.bbk.scene.launcher.theme)
//   - NOT USING main activity com.iqoo.engineermode.EngineerMode (from package com.iqoo.engineermode)
//   - NOT USING main activity com.android.systemui.vivo.common.monkeytest.MonkeyTestActivity (from package com.android.systemui)
// Seeded: 1510817506766
// Event percentages: {** 可以看到--pct-motion的event类型为1}
//   0: 0.0%
//   1: 100.0%
//   2: 0.0%
//   3: 0.0%
//   4: -0.0%
//   5: -0.0%
//   6: 0.0%
//   7: 0.0%
//   8: 0.0%
//   9: 0.0%
//   10: 0.0%
//   11: 0.0%
:Switch: #Intent;action=android.intent.action.MAIN;category=android.intent.category.LAUNCHER;launchFlags=0x10200000;component=com.ddinfo.ddmall/.activity.menu.HelloActivity;end
    // Allowing start of Intent { act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER] cmp=com.ddinfo.ddmall/.activity.menu.HelloActivity } in package com.ddinfo.ddmall
Sleeping for 0 milliseconds
:Sending Touch (ACTION_DOWN): 0:(244.0,931.0)
:Sending Touch (ACTION_MOVE): 0:(257.84354,936.4823)
:Sending Touch (ACTION_MOVE): 0:(271.68744,940.2001)
:Sending Touch (ACTION_MOVE): 0:(281.8605,941.76605)
:Sending Touch (ACTION_MOVE): 0:(287.41925,943.70874)
:Sending Touch (ACTION_MOVE): 0:(295.70917,954.2028)
:Sending Touch (ACTION_MOVE): 0:(298.17896,958.79175)
:Sending Touch (ACTION_MOVE): 0:(304.72922,965.4881)
:Sending Touch (ACTION_MOVE): 0:(306.156,970.51776)
Events injected: 10
:Sending rotation degree=0, persist=false
:Dropped: keys=0 pointers=0 trackballs=0 flips=0 rotations=0
## Network stats: elapsed time=48ms (0ms mobile, 0ms wifi, 48ms not connected)
// Monkey finished

C:\Users\hahah>
```
* --pct-trackball+百分比，调整轨迹事件的百分比(轨迹事件由一个或几个随机的移动组成，有时还伴随有点击)，adb shell monkey -p com.ddinfo.ddmall --pct-trackball 30 1000
```
部分日志
:Sending Trackball (ACTION_MOVE): 0:(1.0,3.0)
:Sending Trackball (ACTION_MOVE): 0:(-3.0,4.0)
:Sending Trackball (ACTION_MOVE): 0:(1.0,2.0)
:Sending Trackball (ACTION_MOVE): 0:(-1.0,-1.0)
:Sending Trackball (ACTION_MOVE): 0:(-2.0,-4.0)
:Sending Trackball (ACTION_MOVE): 0:(-5.0,0.0)
:Sending Trackball (ACTION_MOVE): 0:(3.0,-4.0)
:Sending Trackball (ACTION_MOVE): 0:(2.0,-4.0)
:Sending Trackball (ACTION_MOVE): 0:(2.0,-2.0)
:Sending Trackball (ACTION_MOVE): 0:(0.0,0.0)
:Sending Trackball (ACTION_MOVE): 0:(-5.0,-3.0)
:Sending Trackball (ACTION_MOVE): 0:(-5.0,-1.0)
:Sending Trackball (ACTION_MOVE): 0:(0.0,-3.0)
```
* --pct-nav+百分比，调整“基本”导航事件的百分比(导航事件由来自方向输入设备的up/down/left/right组成)，adb shell monkey --pct-nav 40 1000，**类似于上下左右滑动**
```
部分日志
:Sending Key (ACTION_DOWN): 22    // KEYCODE_DPAD_RIGHT
:Sending Key (ACTION_UP): 22    // KEYCODE_DPAD_RIGHT
Sleeping for 1000 milliseconds
:Sending Key (ACTION_DOWN): 19    // KEYCODE_DPAD_UP
:Sending Key (ACTION_UP): 19    // KEYCODE_DPAD_UP
Sleeping for 1000 milliseconds
:Sending Key (ACTION_DOWN): 22    // KEYCODE_DPAD_RIGHT
:Sending Key (ACTION_UP): 22    // KEYCODE_DPAD_RIGHT
Sleeping for 1000 milliseconds
:Sending Key (ACTION_DOWN): 22    // KEYCODE_DPAD_RIGHT
Events injected: 10
```
* --pct-majornav +百分比，调整“主要”导航事件的百分比(这些导航事件通常引发图形界面中的动作，如：5-way键盘的中间按键、回退按键、菜单按键)，adb shell monkey --pct-majornav 100 10
```
部分日志
Sleeping for 1000 milliseconds
:Sending Key (ACTION_DOWN): 23    // KEYCODE_DPAD_CENTER
:Sending Key (ACTION_UP): 23    // KEYCODE_DPAD_CENTER
Sleeping for 1000 milliseconds
    // activityResuming(com.bbk.appstore)
    // activityResuming(com.bbk.appstore)
    // activityResuming(com.bbk.appstore)
:Sending Key (ACTION_DOWN): 82    // KEYCODE_MENU
:Sending Key (ACTION_UP): 82    // KEYCODE_MENU
```
* --pct-syskeys +百分比，调整“系统”按键事件的百分比(这些按键通常被保留，由系统使用，如Home、Back、Start Call、End Call及音量控制键)，adb shell monkey --pct-syskeys 60 1000，**注意被音量控制键坑**
```
部分日志
:Sending Key (ACTION_DOWN): 25    // KEYCODE_VOLUME_DOWN
:Sending Key (ACTION_UP): 25    // KEYCODE_VOLUME_DOWN
Sleeping for 1000 milliseconds
:Sending Key (ACTION_DOWN): 24    // KEYCODE_VOLUME_UP
:Sending Key (ACTION_UP): 24    // KEYCODE_VOLUME_UP
Sleeping for 1000 milliseconds
:Sending Key (ACTION_DOWN): 25    // KEYCODE_VOLUME_DOWN
:Sending Key (ACTION_UP): 25    // KEYCODE_VOLUME_DOWN
Sleeping for 1000 milliseconds
:Sending Key (ACTION_DOWN): 4    // KEYCODE_BACK
```
* --pct-appswitch +百分比，调整启动Activity的百分比。在随机间隔里，Monkey将执行一个startActivity()调用，作为最大程度覆盖包中全部Activity的一种方法，adb shell monkey -p com.ddinfo.ddmall --pct-appswitch 70 1000，**也就是保持当前app的几率**
```
部分日志
:Switch: #Intent;action=android.intent.action.MAIN;category=android.intent.category.LAUNCHER;launchFlags=0x10200000;component=com.ddinfo.ddmall/.activity.menu.HelloActivity;end
    // Allowing start of Intent { act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER] cmp=com.ddinfo.ddmall/.activity.menu.HelloActivity } in package com.ddinfo.ddmall
Sleeping for 10000 milliseconds
    // Allowing start of Intent { cmp=com.ddinfo.ddmall/.activity.menu.MenuActivity } in package com.ddinfo.ddmall
    // activityResuming(com.ddinfo.ddmall)
:Switch: #Intent;action=android.intent.action.MAIN;category=android.intent.category.LAUNCHER;launchFlags=0x10200000;component=com.ddinfo.ddmall/.activity.menu.HelloActivity;end
    // Allowing start of Intent { act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER] cmp=com.ddinfo.ddmall/.activity.menu.HelloActivity } in package com.ddinfo.ddmall
Sleeping for 10000 milliseconds
:Switch: #Intent;action=android.intent.action.MAIN;category=android.intent.category.LAUNCHER;launchFlags=0x10200000;component=com.ddinfo.ddmall/.activity.menu.HelloActivity;end
    // Allowing start of Intent { act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER] cmp=com.ddinfo.ddmall/.activity.menu.HelloActivity } in package com.ddinfo.ddmall
Sleeping for 10000 milliseconds
```
* --pct-anyevent +百分比，调整其它类型事件的百分比。它包罗了所有其它类型的事件，如：按键、其它不常用的设备按钮、等等，不常用
#### 三、停止monkey命令
* adb shell ps | findstr com.android.commands.monkey 返回第一个数字即是monkey的pid
* adb shell kill pid，结束进程
