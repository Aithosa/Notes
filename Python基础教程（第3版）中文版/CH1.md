# Python 基础教程（第三版）

## CH1 基础知识

1. 除法：
	* `1 / 2` 得到浮点数
	* `1 // 2` 得到整数（整除）
2. 从命令行运行较旧的Python版本时，还可使用命令行开关`-Qnew`
3.  求余（求模）：
	* 即`x % y`等价于`x - ((x // y) * y)`
	* 每10分钟检查一次`if time % 60 == 0: print('On the hour!')`
	> 对于整除运算，需要明白的一个重点是它向下圆整结果。因此在结果为负数的情况下，圆整后将离0更远。这意味着对于-10 // 3，将向下圆整到-4，而不是向上圆整到-3。

4.  乘方（求幂）：`2 ** 3`
	> 乘方运算符的优先级比求负（单目减）高，因此-3 ** 2等价于-(3 ** 2)

5. 进制：
	* 十六进制：`0xAF`
	*  八进制：`010`
	*  二进制：`0b1011010010`
	> 以这些表示法都以0打头

6. 变量：
	> * Python使用变量前必须给它赋值，因为变量没有默认值。
	> * 在Python中，名称（标识符）只能由字母、数字和下划线`_`构成，且不能以数字打头。

7. 获取用户输入：
	* `input("The meaning of life: ")`
	> 被input(以文本或字符串的方式)返回

8. 函数： 通常将pow等标准函数称为内置函数
	* pow执行幂运算
	* abs计算绝对值，
	* round将浮点数圆整为与之最接近的整数
	> 整数总是向下圆整，而round圆整到最接近的整数，并在两个整数一样近时圆整到偶数。

	```Python
	 2 // 3
	 0
	 round(2 / 3)
	1.0
	```

9. 模块：
	> 工作原理：我们使用import导入模块，再以`module.function`的方式使用模块中的函数。
	> 还有一些函数，可用于转换类型，如str和float。实际上，它们并不是函数，而是类。

	* floor返回小于或等于给定数的最小整数（向下圆整）。
	* ceil与floor相反，返回大于或等于给定数的最小整数。
	> * 通过使用命令import的变种`from module import function`，可在调用函数时不指定模块前缀。
	> * 事实上，可使用变量来引用函数（以及其他大部分Python元素）。执行赋值语句`foo =math.sqrt`后，就可使用`foo`来计算平方根。
	> * Python标准库提供了一个专门用于处理复数的模块。` import cmath`
	> * Python没有专门表示虚数的类型，而将虚数视为实部为零的复数。

10.  海龟绘图法（turtle graphic）：能够绘制图形（而不是打印文本）
	* `from turtle import *`
	> 确定需要使用哪些函数后，可回过头去修改import语句，以便只导入这些函数。

11. 让脚本像普通程序一样：
 	* 在UNIX中轻松运行脚本：
		> * `#!/usr/bin/env python`
		> * 如果你安装了多个版本的Python，可用更具体的可执行文件名（如python3）替换python。

	* 将其变成可执行的：`$ chmod a+x hello.py`
	* 运行：`$ hello.py`或`./hello.py`
	* 如果你愿意，可对文件进行重命名并删除扩展名`.py`，使其看起来更像普通程序。
	* 运行等待：`input("Press <enter>")`

12. 字符串
	* 单双引号混用否则使用转义`\`
	* `"Let's say " '"Hello, world!"'`，仅当你同时依次输入两个字符串时，这种机制才管用。
	* 拼接字符串`+`
	* 使用`print()`，将不会打印字符串的引号，而是直接把格式符号转变为格式。
    > * 使用str能以合理的方式将值转换为用户能够看懂的字符串。
    > * 使用repr时，通常会获得值的合法Python表达式表示。

13. 长字符串、原始字符串和字节
	> 在Python 3中，所有的字符串都是Unicode字符串。

	* 长字符串：要表示很长的字符串（跨越多行的字符串），可使用三引号（而不是普通引号），还可使用三个双引号，无需使用反斜杠进行转义。
		> 常规字符串也可横跨多行。只要在行尾加上反斜杠，反斜杠和换行符将被转义，即被忽略。

	* 原始字符串：原始字符串不以特殊方式处理反斜杠，原始字符串用前缀r表示。
		> 例外是，引号需要像通常那样进行转义，但这意味着用于执行转义的反斜杠也将包含在最终的字符串中。

	* 另外，原始字符串不能以单个反斜杠结尾。
    	> * 原始字符串的最后一个字符不能是反斜杠，除非你对其进行转义（但进行转义时，用于转义的反斜杠也将是字符串的一部分）。

		```Python
    	print(r"This is illegal\\")
    	This is illegal\\
		```
    	> * 基本技巧是将反斜杠单独作为一个字符串

    	```Python
		print(r'C:\Program Files\foo\bar' '\\')
		```

14. Unicode、bytes和bytearray
	* 有一种指定Unicode字符的通用机制：使用16或32位的十六进制字面量（分别加上前缀\u或\U）或者使用字符的Unicode名称（\N{name}）。
	> 网站: [http://unicode-table.com](http://unicode-table.com)

	* Python提供了两种类似的类型：不可变的bytes和可变的bytearray。
	* 可直接创建bytes对象（而不是字符串），方法是使用前缀b：b'Hello, world!'
	* 下面来使用ASCII、UTF-8和UTF-32编码将字符串转换为bytes。
	```Python
	> "Hello, world!".encode("ASCII")
	> "Hello, world!".encode("UTF-8")
	> "Hello, world!".encode("UTF-32")
	>
	> len("How long is this?".encode("UTF-8"))    17
	> len("How long is this?".encode("UTF-32"))    72
	```

	* 如果必须使用ASCII编码（这样的情况肯定会遇到），可向encode提供另一个实参，告诉它如何处理错误。
	* 这个参数默认为strict，但可将其指定为其他值，以忽略或替换不在ASCII表中的字符。
	```Python
	> "Hællå, wørld!".encode("ASCII", "ignore")
	> "Hællå, wørld!".encode("ASCII", "replace")
	> "Hællå, wørld!".encode("ASCII", "backslashreplace")
	> "Hællå, wørld!".encode("ASCII", "xmlcharrefreplace")
	> "Hællå, wørld!".encode()`
	> b'H\xc3\xa6ll\xc3\xa5, w\xc3\xb8rld!'.decode()
	```
	* bytes对象本身并不知道使用的是哪种编码，因此你必须负责跟踪这一点。
	* 几乎在所有情况下，都最好使用UTF-8。事实上，它也是默认使用的编码。
	* 可不使用方法encode和decode，而直接创建bytes和str（即字符串）对象，如下所示：
	```Python
	> bytes("Hællå, wørld!", encoding="utf-8")
	> str(b'H\xc3\xa6ll\xc3\xa5, w\xc3\xb8rld!', encoding="utf-8")
	```
	* 这种方法更通用一些，在你不知道类似于字符串或bytes的对象属于哪个类时，使用这种方法也更管用。一个通用规则是，不要做过于严格的假设。
	* 源代码也将被编码，且默认使用的也是UTF-8编码。
	* 如果你想使用其他编码，可使用特殊的注释来指定。
	> `# -*- coding: encoding name -*-`
	> <br>请将其中的encoding name替换为你要使用的编码（大小写都行），如`utf-8`或`latin-1`

	* bytearray是bytes的可变版，从某种意义上说，它就像是可修改的字符串——常规字符串是不能修改的。


### 本章介绍的新函数

| 函 数 | 描 述 |
| - | - |
| abs(number) | 返回指定数的绝对值 |
| bytes(string, encoding[, errors])  | 对指定的字符串进行编码，并以指定的方式处理错误 |
| cmath.sqrt(number)  | 返回平方根；可用于负数 |
| float(object)  | 将字符串或数字转换为浮点数 |
| help([object])  | 提供交互式帮助 |
| input(prompt)  | 以字符串的方式获取用户输入 |
| int(object)  | 将字符串或数转换为整数 |
| math.ceil(number)  | 以浮点数的方式返回向上圆整的结果 |
| math.floor(number)  | 以浮点数的方式返回向下圆整的结果 |
| math.sqrt(number)  | 返回平方根；不能用于负数 |
| pow(x, y[, z])  | 返回x的y次方对z求模的结果 |
| print(object, ...)  | 将提供的实参打印出来，并用空格分隔 |
| repr(object)  | 返回指定值的字符串表示 |
| round(number[, ndigits])  | 四舍五入为指定的精度，正好为5时舍入到偶数 |
| str(object)  | 将指定的值转换为字符串。用于转换bytes时，可指定编码和错误处理方式 |
