#coding:utf-8
"""
C:\Users\Administrator>scrapy startproject -h
Usage
=====
  scrapy startproject <project_name> [project_dir]

Create new project

Options
=======
--help, -h              show this help message and exit

Global Options
--------------
--logfile=FILE          log file. if omitted stderr will be used  日志文件路径
--loglevel=LEVEL, -L LEVEL                                        日志信息等级
                        log level (default: DEBUG)
--nolog                 disable logging completely                不输出日志信息
--profile=FILE          write python cProfile stats to FILE
--pidfile=FILE          write process ID to FILE
--set=NAME=VALUE, -s NAME=VALUE
                        set/override setting (may be repeated)
--pdb                   enable pdb on failure
"""
"""
C:\Users\Administrator>scrapy -h
Scrapy 1.3.3 - no active project

Usage:
  scrapy <command> [options] [args]

Available commands:
  bench         Run quick benchmark test     #测试本地硬件的性能
  commands
  fetch         Fetch a URL using the Scrapy downloader  # 显示爬虫爬取过程  scrapy fetch https://www.baidu.com
  genspider     Generate new spider using pre-defined templates  #模版创建爬虫文件
  runspider     Run a self-contained spider (without creating a project)   #直接运行一个爬虫文件.py，不需要依托项目(进去文件目录scrapy runspider --loglevel=INFO test027.py )
  settings      Get settings values   #scrapy settings --get BOT_NAME
  shell         Interactive scraping console   #启动scrapy的交互终端 scrapy shell http://www.baidu.com
  startproject  Create new project    #创建项目
  version       Print Scrapy version  #scrapy version -v看版本号
  view          Open URL in browser, as seen by Scrapy  #scrapy view http://news.163.com/  下载到本地并且打开

  [ more ]      More commands available when run from project directory

Use "scrapy <command> -h" to see more info about a command
"""
"""
C:\Users\Administrator>scrapy fetch -h
Usage
=====
  scrapy fetch [options] <url>

Fetch a URL using the Scrapy downloader and print its content to stdout. You
may want to use --nolog to disable logging

Options
=======
--help, -h              show this help message and exit
--spider=SPIDER         use this spider
--headers               print response HTTP headers instead of body   # scrapy fetch --headers  --nolog http://news.sina.com.cn/
--no-redirect           do not handle HTTP 3xx status codes and print response
                        as-is

Global Options
--------------
--logfile=FILE          log file. if omitted stderr will be used
--loglevel=LEVEL, -L LEVEL
                        log level (default: DEBUG)
--nolog                 disable logging completely
--profile=FILE          write python cProfile stats to FILE
--pidfile=FILE          write process ID to FILE
--set=NAME=VALUE, -s NAME=VALUE
                        set/override setting (may be repeated)
--pdb                   enable pdb on failure

"""