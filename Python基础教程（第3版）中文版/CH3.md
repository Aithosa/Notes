# Python 基础教程（第三版）

## CH3 使用字符串

1. 字符串基本操作
    * 所有标准序列操作（索引、切片、乘法、成员资格检查、长度、最小值和最大值）都适用于字符串，
    * 字符串是不可变的，因此所有的元素赋值和切片赋值都是非法的。

2. 设置字符串的格式：精简版
    * Python提供了多种字符串格式设置方法。
    * 主要的解决方案是使用字符串格式设置运算符——百分号。
        * 这个运算符的行为类似于C语言中的经典函数printf：在%左边指定一个字符串（格式字符串），并在右边指定要设置其格式的值。指定要设置其格式的值时，可使用单个值（如字符串或数字），可使用元组（如果要设置多个值的格式），还可使用字典（这将在下一章讨论），其中最常见的是元组。
        * %s称为转换说明符，指出了要将值插入什么地方。
        * 如果指定的值不是字符串，将使用str将其转换为字符串。
     ```Python
     format = "Hello, %s. %s enough for ya?"
     values = ('world', 'Hot')
     format % values
     'Hello, world. Hot enough for ya?'
    ```

    * 另一种解决方案是所谓的模板字符串，使用类似于UNIX shell的语法，旨在简化基本的格式设置机制。
        * 包含等号的参数称为关键字参数.在字符串格式设置中，可将关键字参数视为一种向命名替换字段提供值的方式。
    ```Python
    from string import Template
    tmpl = Template("Hello, $who! $what enough for ya?")
    tmpl.substitute(who="Mars", what="Dusty")
    'Hello, Mars! Dusty enough for ya?'
    ```
    * 编写新代码时，应选择使用字符串方法format，它融合并强化了早期方法的优点。
        * 每个替换字段都用花括号括起，其中可能包含名称，还可能包含有关如何对相应的值进行转换和格式设置的信息。
        * 在最简单的情况下，替换字段没有名称或将索引用作名称。
    ```Python
     "{}, {} and {}".format("first", "second", "third")
     'first, second and third'
     "{0}, {1} and {2}".format("first", "second", "third")
     'first, second and third'
     ```
        * 索引无需像上面这样按顺序排列。
    ```Python
    "{3} {0} {2} {1} {3} {0}".format("be", "not", "or", "to")
    'to be or not to be'
    ```
        * 命名字段的工作原理与你预期的完全相同。
    ```Python
     from math import pi
     "{name} is approximately {value:.2f}.".format(value=pi, name="π")
     'π is approximately 3.14.'
     ```
        * 关键字参数的排列顺序无关紧要
    ```Python
    "{name} is approximately {value}.".format(value=pi, name="π")
    'π is approximately 3.141592653589793.'
    ```
        * 在Python 3.6中，如果变量与替换字段同名，还可使用一种简写。在这种情况下，可使用f字符串——在字符串前面加上f。
    ```Python
     from math import e
     f"Euler's constant is roughly {e}."
     "Euler's constant is roughly 2.718281828459045."
    ```
        * 与下面这个更明确一些的表达式等价：
    ```Python
     "Euler's constant is roughly {e}.".format(e=e)
     "Euler's constant is roughly 2.718281828459045."
    ```
3. 设置字符串的格式：完整版
<br>基本思想是对字符串调用方法format，并提供要设置其格式的值。
<br>每个值都被插入字符串中，以替换用花括号括起的替换字段。要在最终结果中包含花括号，可在格式字符串中使用两个花括号（即`{{`或`}}`）来指定。
```Python
"{{ceci n'est pas une replacement field}}".format()
"{ceci n'est pas une replacement field}"
```
> **替换字段**
    * **字段名**：索引或标识符，指出要设置哪个值的格式并使用结果来替换该字段。除指定值外，还可指定值的特定部分，如列表的元素。
    * **转换标志**：跟在叹号后面的单个字符。当前支持的字符包括r（表示repr）、s（表示str）和a（表示ascii）。如果你指定了转换标志，将不使用对象本身的格式设置机制，而是使用指定的函数将对象转换为字符串，再做进一步的格式设置。
    * **格式说明符**：跟在冒号后面的表达式（这种表达式是使用微型格式指定语言表示的）。格式说明符让我们能够详细地指定最终的格式，包括格式类型（如字符串、浮点数或十六进制数），字段宽度和数的精度，如何显示符号和千位分隔符，以及各种对齐和填充方式。

    1. 替换字段名
        * 向format提供要设置其格式的未命名参数，并在格式字符串中使用未命名字段。
        * 通过索引来指定要在哪个字段中使用相应的未命名参数，这样可不按顺序使用未命名参数。
        * 然而，不能同时使用手工编号和自动编号，因为这样很快会变得混乱不堪。
        ```Python
        "{foo} {} {bar} {}".format(1, 2, bar=4, foo=3)
        "{foo} {1} {bar} {0}".format(1, 2, bar=4, foo=3)
        '3 2 4 1'
        ```
        * 并非只能使用提供的值本身，而是可访问其组成部分（就像在常规Python代码中一样）
        ```Python
        fullname = ["Alfred", "Smoketoomuch"]
        "Mr {name[1]}".format(name=fullname)
        //'Mr Smoketoomuch'
        import math
        tmpl = "The {mod.__name__} module defines the value {mod.pi} for π"
        tmpl.format(mod=math)
        //'The math module defines the value 3.141592653589793 for π'
        ```
    2. 基本转换
        * 指定要在字段中包含的值后，就可添加有关如何设置其格式的指令。
        ```Python
        print("{pi!s} {pi!r} {pi!a}".format(pi="π"))
        π 'π' '\u03c0'
        ```
        > s、r和a指str、repr和ascii
        >* 函数str通常创建外观普通的字符串版本（这里没有对输入字符串做任何处理）。
        >* 函数repr尝试创建给定值的Python表示（这里是一个字符串字面量）。
        >* 函数ascii创建只包含ASCII字符的表示，类似于Python 2中的repr。

        * 指定要转换的值是哪种类型，更准确地说，是要将其视为哪种类型。
            > 提供一个整数，但将其作为小数进行处理。
        ```Python
        >>> "The number is {num}".format(num=42)
        'The number is 42'
        >>> "The number is {num:f}".format(num=42)
        'The number is 42.000000'
        ```
            > 作为二进制数进行处理
        ```Python
        >>> "The number is {num:b}".format(num=42)
        'The number is 101010'
        ```

    3. 宽度、精度和千位分隔符
        *


4. 字符串方法
    0. 前面介绍了列表的方法，而字符串的方法要多得多，因为其很多方法都是从模块string那里“继承”而来的。

    > 在较早的Python版本中，这些方法为模块string中的函数。如果需要，现在依然能够找到这些函数。

    > <br>模块string未死
    > <br>虽然字符串方法完全盖住了模块string的风头，但这个模块包含一些字符串没有的常量和函数。下面就是模块string中几个很有用的常量①。
    >* string.digits：包含数字0～9的字符串。
    >* string.ascii_letters：包含所有ASCII字母（大写和小写）的字符串。
    >* string.ascii_lowercase：包含所有小写ASCII字母的字符串。
    >* string.printable：包含所有可打印的ASCII字符的字符串。
    >* string.punctuation：包含所有ASCII标点字符的字符串。
    >* string.ascii_uppercase：包含所有大写ASCII字母的字符串。
    >
    > 虽然说的是ASCII字符，但值实际上是未解码的Unicode字符串。

    1. center
        * 方法center通过在两边添加填充字符（默认为空格）让字符串居中。
        ```Python
        >>> "The Middle by Jimmy Eat World".center(39)
        '     The Middle by Jimmy Eat World     '
        >>> "The Middle by Jimmy Eat World".center(39, "*")
        '*****The Middle by Jimmy Eat World*****'
        ```
        > 附录B：ljust、rjust和zfill。

    2. find
        * 方法find在字符串中查找子串。如果找到，就返回子串的第一个字符的索引，否则返回-1。
        > 字符串方法find返回的并非布尔值。如果find像这样返回0，就意味着它在索引0处找到了指定的子串。

        ```Python
        >>> 'With a moo-moo here, and a moo-moo there'.find('moo')
        7
        >>> title = "Monty Python's Flying Circus"
        >>> title.find('Monty')
        0
        >>> title.find('Python')
        6
        >>> title.find('Flying')
        15
        >>> title.find('Zirquss')
        -1
        ```
        * 指定搜索的起点和终点（它们都是可选的）。
        ```Python
        >>> subject = '$$$ Get rich now!!! $$$'
        >>> subject.find('$$$')
        0
        >>> subject.find('$$$', 1) # 只指定了起点
        20
        >>> subject.find('!!!')
        16
        >>> subject.find('!!!', 0, 16) # 同时指定了起点和终点
        -1
        ```
        > 请注意，起点和终点值（第二个和第三个参数）指定的搜索范围包含起点，但不包含终点。这是Python惯常的做法。
        > 附录B：rfind、index、rindex、count、startswith、endswith。

    3. join
        * join是一个非常重要的字符串方法，其作用与split相反，用于合并序列的元素。
        * 所合并序列的元素必须都是字符串。
        ```Python
        >>> seq = [1, 2, 3, 4, 5]
        >>> sep = '+'
        >>> sep.join(seq) # 尝试合并一个数字列表
        Traceback (most recent call last):
        File "<stdin>", line 1, in ?
        TypeError: sequence item 0: expected string, int found
        >>> seq = ['1', '2', '3', '4', '5']
        >>> sep.join(seq) # 合并一个字符串列表
        '1+2+3+4+5'
        >>> dirs = '', 'usr', 'bin', 'env'
        >>> '/'.join(dirs)
        '/usr/bin/env'
        >>> print('C:' + '\\'.join(dirs))
        C:\usr\bin\env
        ````
    4. lower
        * 方法lower返回字符串的小写版本。
        ```Python
        >>> 'Trondheim Hammer Dance'.lower()
        'trondheim hammer dance'
        ```
        ```Python
        >>> name = 'Gumby'
        >>> names = ['gumby', 'smith', 'jones']
        >>> if name.lower() in names: print('Found it!')
        ...
        Found it!
        ```
        >* 另请参见：islower、istitle、isupper、translate。
        >* 附录B：capitalize、casefold、swapcase、title、upper。

        * 词首大写
            * title（参见附录B）
                * 它将字符串转换为词首大写，即所有单词的首字母都大写，其他字母都小写。
                * 它确定单词边界的方式可能导致结果不合理。
                ```Python
                >>> "that's all folks".title()
                "That'S All, Folks"
                ```
            * 使用模块string中的函数capwords。
            ```Python
            >>> import string
            >>> string.capwords("that's all, folks")
            That's All, Folks"
            ```
    5. replace
        * 方法replace将指定子串都替换为另一个字符串，并返回替换后的结果。
        ```Python
        >>> 'This is a test'.replace('is', 'eez')
        'Theez eez a test'
        ```
        >* 另请参见：translate。
        >* 附录B：expandtabs。

    6. split
        * split是一个非常重要的字符串方法，其作用与join相反，用于将字符串拆分为序列。
        ```Python
        >>> '1+2+3+4+5'.split('+')
        ['1', '2', '3', '4', '5']
        >>> '/usr/bin/env'.split('/')
        ['', 'usr', 'bin', 'env']
        >>> 'Using the default'.split()
        ['Using', 'the', 'default']
        ```
        >* 注：如果没有指定分隔符，将默认在单个或多个连续的空白字符（空格、制表符、换行符等）处进行拆分。
        >* 另请参见：join。
        >* 附录B：partition、rpartition、rsplit、splitlines。

    7. strip
        * 方法strip将字符串开头和末尾的空白（但不包括中间的空白）删除，并返回删除后的结果。
        ```Python
        >>> ' internal whitespace is kept '.strip()
        'internal whitespace is kept'
        ```
        * 与lower一样，需要将输入与存储的值进行比较时，strip很有用。
        ```Python
        >>> names = ['gumby', 'smith', 'jones']
        >>> name = 'gumby '
        >>> if name in names: print('Found it!')
        ...
        >>> if name.strip() in names: print('Found it!')
        ...
        Found it!
        ```
        * 还可在一个字符串参数中指定要删除哪些字符。
        ```Python
        >>> '*** SPAM * for * everyone!!! ***'.strip(' *!')
        'SPAM * for * everyone'
        ```
        >* 这个方法只删除开头或末尾的指定字符，因此中间的星号未被删除。
        >* 附录B：lstrip、rstrip。

    8. translate
        * 方法translate与replace一样替换字符串的特定部分，但不同的是它只能进行单字符替换。
        * 这个方法的优势在于能够同时替换多个字符，因此效率比replace高。
        * 使用translate前必须创建一个转换表。
        ```python
        >>> table = str.maketrans('cs', 'kz')
        >>> table
        {115: 122, 99: 107}
        >>> 'this is an incredible test'.translate(table)
        'thiz iz an inkredible tezt'
        ```
        * 调用方法maketrans时，还可提供可选的第三个参数，指定要将哪些字母删除
        ```Python
        >>> table = str.maketrans('cs', 'kz', ' ')
        >>> 'this is an incredible test'.translate(table)
        'thizizaninkredibletezt'
        ```
        > 另请参见：replace、lower。

    9. 判断字符串是否满足特定的条件
        * 很多字符串方法都以is打头，如isspace、isdigit和isupper，它们判断字符串是否具有特定的性质（如包含的字符全为空白、数字或大写）。如果字符串具备特定的性质，这些方法就返回True，否则返回False。
        > 附录B：isalnum、isalpha、isdecimal、isdigit、isidentifier、islower、isnumeric、isprintable、isspace、istitle、isupper。

5. 本章介绍的新函数

|函 数|描 述|
|:|:|
|string.capwords(s[, sep]) |使用split根据sep拆分s，将每项的首字母大写，再以空格为分隔符将它们合并起来|
|ascii(obj) |创建指定对象的ASCII表示|


6. 字符串格式设置中的类型说明符

|类型|含 义|
|:|:|
|b |将整数表示为二进制数|
|d |将整数视为十进制数进行处理，这是整数默认使用的说明符|
|e |使用科学表示法来表示小数（用e来表示指数）|
|E |与e相同，但使用E来表示指数|
|f |将小数表示为定点数|
|F |与f相同，但对于特殊值（nan和inf），使用大写表示|
|g |自动在定点表示法和科学表示法之间做出选择。这是默认用于小数的说明符，但在默认情况下至少有1位小数|
|G |与g相同，但使用大写来表示指数和特殊值|
|n |与g相同，但插入随区域而异的数字分隔符|
|o |将整数表示为八进制数|
|s |保持字符串的格式不变，这是默认用于字符串的说明符|
|x |将整数表示为十六进制数并使用小写字母|
|X |与x相同，但使用大写字母|
|% |将数表示为百分比值（乘以100，按说明符f设置格式，再在后面加上%）|
