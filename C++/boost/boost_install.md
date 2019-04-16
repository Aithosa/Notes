# Boost的安装

## 环境

Ubuntu 14.04.05(Linux 4.4.0) 

GCC 4.8.4

## 快捷安装

在Boost解压缩后的目录下直接执行命令：

```bash
# 编译前的配置工作
./bootstrap.sh
# b2开始真正的编译并安装Boost
./b2 install
```

如果不指定额外选项，boost将编译release版本的库文件，把头文件安装到"/usr/local/include", 库文件安装到"/use/local/lib"。

## 完全安装

完整编译Boost，使用buildtype选项制定变异类型(如不指定则默认使用release模式)，在bootstrap.sh之后执行如下命令：

```bash
./b2 --buildtype=complete install
```

这样开始对Boost的完整编译，安装所有的调试版，发行版的静态库和动态库。

## 定制安装

完整编译boost费时耗力，而且这些库并不可能在开发过程中全部用到，因此，Boost也允许用户自行选择要变异的库。

执行命令

```bash
./b2 --show-libraries
```

可查看所有必须编译才能使用的库。

在完全变异命令的基础上，使用--with或者--without选项可打开或者关闭某个库的编译，如：

```bash
./b2 --with-date_time --buildtype=complete install
```

将仅编译安装date_time库。

本书使用的安装命令是：

```bash
sudo ./b2 link=static install    # 编译安装所有静态链接库
```

b2和bootstrap.sh还有其他很多选项，如指定安装路径、指定debug或release版等等，可以使用--help选项或者参考Boost文档以获得更多信息。

## 编译验证

让我们来编写一个简单的boost程序来验证开发环境。

头文件<boost/version.hpp>里有两个宏，定义了当前使用的Boost程序库版本号：

```C++
#define BOOST_VERSION 106400    // 数字形式的版本号
#define BOOST_LIB_VERSION "1_64"    // 字符串形式的版本号
```

头文件<boost/config.hpp>里由三个宏：BOOST_PLATFORM、 BOOST_COMPILER 和 BOOST_STDLIB，分别定义了当前的操作系统、编译器和标准库。

下面的代码就是我们与Boost的第一次接触：

```C++
#include <boost/version.hpp>    // 包含Boost头文件
#include <boost/config.hpp>    // 包含Boost头文件

int main()
{
	cout << BOOST_VERSION << endl;    // Boost版本号
	cout << BOOST_LIB_VERSION << endl;    // Boost版本号
	cout << BOOST_PLATFORM << endl;    // 操作系统
	cout << BOOST_COMPILER << endl;    // 编译器
	cout << BOOST_STDLIB << endl;    // 标准库
}
```

然后使用g++编译：

```bash
g++ -o a.out test.cpp -I
```

程序运行的结果是：

```
106400
1_64
linux
GNU c++ version 4.8.4
GNU libstdc++ version 20150426
```