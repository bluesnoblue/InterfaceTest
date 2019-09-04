# InterfaceTest

灵感来源于写WebUI自动化的PageObject的设计模式；根据被测项目的实际情况，将接口抽离出来封装成接口层。辅以单元测试框架unittest、数据驱动ddt的用例层和数据层，提高测试代码的维护性和可阅读性 ~~（尤其是RESTful风格的api ）~~。

##  开始

**安装**

克隆或下载项目，安装依赖。

~~~
pip install -r requirement.txt
~~~

~~不知道requirement.txt里面有没有漏掉什么依赖包，因为作者没有使用虚拟环境的习惯所以是没有直接用pip生成requirement.txt，如果运行测试代码的时候报错就用pip install直接安装相应的包吧。~~

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

### 接口封装InterfaceTest.interface

Demo这里假设被测项目有两个模块共计四个接口：

Auth 模块
- 注册	POST	/register
- 登录	POST	/login
- 登出	DELETE	/logout

User 模块
- 获取个人信息	GET	/profile

为了提高代码维护性，接口推荐按接口的模块实现接口的mixin类，所有的mixin类继承BASE.py里的BaseInterface类，最后在\_\_init\_\_.py内混入Interface类。

在BaseInterface类中主要是实现请求头的工厂方法（接口常见需要附带时间戳、随机数、静态签名等需求可以在这里这里实现）。

在Auth登录、登出的接口实现上实现了更新token，而在Interface类的初始化方法中，提供可以在实例化的过程中登录以便后续直接调用需要登录的接口（参考测试用例TestUser）。

推荐每个mixin类内按一个接口与一个函数来实现，函数一般按{HTTP method}_{resource}来命名。

如果遇到服务端同时有多个用户体系，可以在包里另外抽象一个Base类和Inteface类，也可以另外写一个包。

### 测试用例InterfaceTest.case

在case中，同样的根据接口的模块分文件编写测试用例，为了方便后续可以按端、模块单独运行文件按test\_{module}.py（或test\_app\_{module}.py、test\_admin\_{module}.py）进行命名。这里可以参考主入口run.py当中-p \<pattern\>的逻辑。

在每一个模块中一般用一个TestCase来维护相关的用例、一个test方法来维护一个接口用例，这里的分类粒度可以根据实际项目来划分，因为遇到过Auth模块接口过多、所以按密码登录相关接口、验证码登录相关接口分了两个TestCase。而一个test方法来维护一个接口的所有用例可能会违背“一个测试只有一个断言”的原则

在遇到某个接口需要相对大量测试数据则可以用ddt模块将数据层的yaml数据引入测试用例中，一般少量、或者业务逻辑上的小量用例一般直接在用例层中实现。

### 数据层

每个yaml文件维护单个接口的测试数据，按test\_{module}\_{mothod}命名。~~（这里我想不通为啥我要按test_开头）~~

### 配置源文件及配置文件CONFIG.py & CONFIG_raw.txt

这部分作者暂时没有想到什么更好的办法实现根据执行脚本的入参动态修改CONFIG文件。
所以目前是根据CONFIG_raw.txt复制多一份CONFIG.py。在调试的时候可以修改CONFIG.py，如果确定了配置之后记得修改配置源文件。

## 更新计划

- 替换用例执行器至HTMLrunner、并保存html报告
- 添加发送邮件的模块、并将报告发送至相关人员
- 自己实现一个被测服务（也可能另外开一个项目）