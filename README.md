# InterfaceTest

灵感来源于写WebUI自动化的PageObject的设计模式；根据被测项目的实际情况，将接口抽离出来封装成接口层。辅以单元测试框架unittest、数据驱动ddt的用例层和数据层，提高测试代码的维护性和可阅读性 ~~ （尤其是RESTful风格的api ）~~。

##  开始

**安装**

克隆或下载项目，安装依赖。

~~~
pip install -r requirement.txt
~~~

启动测试代码

~~~
python run.py
~~~



## 目录结构描述

~~~
InterfaceTest
├── run.py										# 启动测试
├── CONFIG.py									# 配置文件
├── CONFIG_RAW.txt								# 配置源文件
├── case										# 测试用例
│   ├── test_{modulename}.py             
│   ├── ...
├── data										# 测试数据集
│   ├── test_{modulename}_{interfacename}.yaml	# 测试数据
│   ├── ...            
└── interface									# 接口封装
    └── __init__.py
    └── {modelname}.py
    └── BASE.py
~~~

##  DEMO

### 接口封装

...持续更新中

### 测试用例

...持续更新中

### 数据层

...持续更新中

## 更新计划

- 替换用例执行器至HTMLrunner、并保存html报告
- 添加发送邮件的模块、并将报告发送至相关人员
- 自己实现一个被测服务（也可能另外开一个项目）