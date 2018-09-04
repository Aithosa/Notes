# CH8 异常

## 8.1 异常是什么

Python使用异常对象来表示异常状态，并在遇到错误时引发异常。异常对象未被处理（或捕获）时，程序将终止并显示一条错误消息（traceback）。
<br>事实上，每个异常都是某个类（这里是ZeroDivisionError）的实例。你能以各种方式引发和捕获这些实例，从而逮住错误并采取措施，而不是放任整个程序失败。

## 8.2 让事情沿你指定的轨道出错

### 8.2.1 raise 语句

要引发异常，可使用raise语句，并将一个类（必须是Exception的子类）或实例作为参数。将类作为参数时，将自动创建一个实例。
<br>下面的示例使用的是内置异常类Exception：
```bash
>>> raise Exception    # 引发的是通用异常，没有指出出现了什么错误
Traceback (most recent call last):
File "<stdin>", line 1, in ?
Exception

>>> raise Exception('hyperdrive overload')    # 添加了错误消息hyperdrive overload
Traceback (most recent call last):
File "<stdin>", line 1, in ?
Exception: hyperdrive overload
```
在“Python库参考手册”的Built-in Exceptions一节，可找到有关所有内置异常类的描述。这些异常类都可用于raise语句中。

表8-1 一些内置的异常类

|类 名|描 述|
|:|:|
|Exception |几乎所有的异常类都是从它派生而来的|
|AttributeError |引用属性或给它赋值失败时引发|
|OSError |操作系统不能执行指定的任务（如打开文件）时引发，有多个子类|
|IndexError |使用序列中不存在的索引时引发，为LookupError的子类|
|KeyError |使用映射中不存在的键时引发，为LookupError的子类|
|NameError |找不到名称（变量）时引发|
|SyntaxError |代码不正确时引发|
|TypeError |将内置操作或函数用于类型不正确的对象时引发|
|ValueError |将内置操作或函数用于这样的对象时引发：其类型正确但包含的值不合适|
|ZeroDivisionError |在除法或求模运算的第二个参数为零时引发|

### 8.2.2 自定义的异常类

如果你要使用特殊的错误处理代码对超光速推进装置错误进行处理，就必须有一个专门用于表示这些异常的类。
那么如何创建异常类呢？就像创建其他类一样，但务必直接或间接地继承Exception（这意味着从任何内置异常类派生都可以）。因此，自定义异常类的代码类似于下面这样：
<br>`class SomeCustomException(Exception): pass`

## 8.3 捕获异常

前面说过，异常比较有趣的地方是可对其进行处理，通常称之为捕获异常。为此，可使用try/except语句。
```Python
try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except ZeroDivisionError: # 不能引发别的错误，还是会报错ZeroDivisionError
    print("The second number can't be zero!")
```
*注意: 异常从函数向外传播到调用函数的地方。如果在这里也没有被捕获，异常将向程序的最顶层传播。这意味着你可使用try/except来捕获他人所编写函数引发的异常。*

### 8.3.1 不用提供参数

捕获异常后，如果要重新引发它（即继续向上传播），可调用raise且不提供任何参数（也可显式提供捕获到的异常，参见8.3.4节）。
<br>来看一个能够“抑制”异常ZeroDivisionError的计算器类。如果启用了这种功能，计算器将打印一条错误消息，而不让异常继续传播。在与用户交互的会话中使用这个计算器时，抑制异常很有用；但在程序内部使用时，引发异常是更佳的选择（此时应关闭“抑制”功能）。
```Python
class MuffledCalculator:
    muffled = False
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:    # 捕获异常
            if self.muffled:
                print('Division by zero is illegal')    # 没有raise则继续向上传播
            else:
                raise    # 引发异常
```
*注意: 发生除零行为时，如果启用了“抑制”功能，方法calc将（隐式地）返回None。换而言之，如果启用了“抑制”功能，就不应依赖返回值。*
```Python
>>> calculator = MuffledCalculator()
>>> calculator.calc('10 / 0') # 关闭了抑制功能
Traceback (most recent call last): File "<stdin>", line 1, in ?
    File "MuffledCalculator.py", line 6, in calc
        return eval(expr)
    File "<string>", line 0, in ?
ZeroDivisionError: integer division or modulo by zero

>>> calculator.muffled = True    # 打开抑制功能时，捕获了异常ZeroDivisionError，但继续向上传播它。
>>> calculator.calc('10 / 0')
Division by zero is illegal
```
如果无法处理异常，在except子句中使用不带参数的raise通常是不错的选择，但有时你可能想引发别的异常。在这种情况下，导致进入except子句的异常将被作为异常上下文存储起来，并出现在最终的错误消息中：
```Python
>>> try:
        1/0
    except ZeroDivisionError:
         raise ValueError

Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
ZeroDivisionError: division by zero
# 在处理上述异常时，引发了另一个异常：
Traceback (most recent call last):
    File "<stdin>", line 4, in <module>
ValueError
```
你可使用raise ... from ...语句来提供自己的异常上下文，也可使用None来禁用上下文。
```python

>>> try:
        1/0
    except ZeroDivisionError:
        raise ValueError from None    # 这里只显示ValueError，没有ZeroDivisionError

Traceback (most recent call last):
    File "<stdin>", line 4, in <module>
ValueError
```
### 8.3.2 多个except 子句

由于程序中的except子句只捕获ZeroDivisionError异常，其他异常将成为漏网之鱼，导致程序终止。为同时捕获这种异常，可在try/except语句中再添加一个except子句。
```Python
try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except ZeroDivisionError:
    print("The second number can't be zero!")
except TypeError:
    print("That wasn't a number, was it?")
```
**如何检查一个值能否用于除法运算呢？方法有很多，但最佳的方法无疑是尝试将两个值相除，看看是否可行。**
<br>另外，注意到异常处理并不会导致代码混乱，而添加大量的if语句来检查各种可能的错误状态将导致代码的可读性极差。

### 8.3.3 一箭双雕

如果要使用一个except子句捕获多种异常，可在一个元组中指定这些异常，如下所示：
```Python
try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except (ZeroDivisionError, TypeError, NameError):
    print('Your numbers were bogus ...')
```
在except子句中，异常两边的圆括号很重要。一种常见的错误是省略这些括号，这可能导致你不想要的结果。
<br>当然，仅仅打印错误消息帮助不大。另一种解决方案是不断地要求用户输入数字，直到能够执行除法运算为止。

### 8.3.4 捕获对象

要在except子句中访问异常对象本身，可使用两个而不是一个参数。（请注意，即便是在你捕获多个异常时，也只向except提供了一个参数——一个元组。）需要让程序继续运行并记录错误（可能只是向用户显示）时，这很有用。
```Python
try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except (ZeroDivisionError, TypeError) as e:    # except子句捕获两种异常，
    print(e)    # 但由于你同时显式地捕获了对象本身，因此可将其打印出来，让用户知道发生了什么情况
```

### 8.3.5 一网打尽

异常无法完全被try/except语句捕获，这理所当然，因为你没有预测到这种问题，也没有采取相应的措施。在这些情况下，与其使用并非要捕获这些异常的try/except语句将它们隐藏起来，还不如让程序马上崩溃，因为这样你就知道什么地方出了问题。
<br>然而，如果你就是要使用一段代码捕获所有的异常，只需在except语句中不指定任何异常类即可。
```Python
try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except:
    print('Something wrong happened ...')
```
像这样捕获所有的异常很危险，因为这不仅会隐藏你有心理准备的错误，还会隐藏你没有考虑过的错误。这还将捕获用户使用`Ctrl + C`终止执行的企图、调用函数`sys.exit`来终止执行的企图等。
<br>在大多数情况下，更好的选择是使用`except Exception as e`并对异常对象进行检查。这样做将让不是从`Exception`派生而来的为数不多的异常成为漏网之鱼，其中包括`SystemExit`和`KeyboardInterrupt`，因为它们是从`BaseException`（`Exception`的超类）派生而来的。

### 8.3.6 万事大吉时

在有些情况下，在没有出现异常时执行一个代码块很有用。为此，可像条件语句和循环一样，给try/except语句添加一个else子句。
```Python
try:
    print('A simple task')
except:
    print('What? Something went wrong?')
else:
    print('Ah ... It went as planned.')
```
如果你运行这些代码，输出将如下：
```bash
A simple task
Ah ... It went as planned.
```
通过使用else子句，可实现8.3.3节所说的循环。
```Python
while True:
    try:
        x = int(input('Enter the first number: '))
        y = int(input('Enter the second number: '))
        value = x / y
        print('x / y is', value)
    except:
        print('Invalid input. Please try again.')
    else:
        break
```
在这里，仅当没有引发异常时，才会跳出循环（这是由else子句中的break语句实现的）。换而言之，只要出现错误，程序就会要求用户提供新的输入。

前面说过，一种更佳的替代方案是使用空的except子句来捕获所有属于类Exception（或其子类）的异常。你不能完全确定这将捕获所有的异常，因为try/except语句中的代码可能使用旧式的字符串异常或引发并非从Exception派生而来的异常。然而，如果使用`except Exception as e`，就可利用8.3.4节介绍的技巧在这个小型除法程序中打印更有用的错误消息。
```python
while True:
    try:
        x = int(input('Enter the first number: '))
        y = int(input('Enter the second number: '))
        value = x / y
        print('x / y is', value)
    except Exception as e:
        print('Invalid input:', e)
        print('Please try again')
    else:
        break
```

### 8.3.7 最后

最后，还有finally子句，可用于在发生异常时执行清理工作。这个子句是与try子句配套的。
```Python
# 运行这个程序，它将在执行清理工作后崩溃。
x = None
try:
    x = 1 / 0
finally:    # 不管try子句中发生什么异常，都将执行finally子句。
    print('Cleaning up ...')
    del x
```
为何在try子句之前初始化x呢？因为如果不这样做，ZeroDivisionError将导致根本没有机会给它赋值，进而导致在finally子句中对其执行del时引发未捕获的异常。
<br>虽然使用del来删除变量是相当愚蠢的清理措施，但finally子句非常适合用于确保文件或网络套接字等得以关闭
<br>也可在一条语句中同时包含try、except、finally和else（或其中的3个）。
```Python
try:
    1 / 0
except ZeroDivisionError:
    print("Unknown variable")
else:
    print("That went well!")
finally:
    print("Cleaning up.")
```

## 8.4 异常和函数

异常和函数有着天然的联系。**如果不处理函数中引发的异常，它将向上传播到调用函数的地方。如果在那里也未得到处理，异常将继续传播，直至到达主程序（全局作用域）。如果主程序中也没有异常处理程序，程序将终止并显示栈跟踪消息。**
```Python
>>> def faulty():
...     raise Exception('Something is wrong')
...
>>> def ignore_exception():
...     faulty()
...
>>> def handle_exception():
...     try:
...         faulty()
...     except:
...         print('Exception handled')
...
# 这里怎样才算处理异常？本例是不是只是捕获了异常，而之前是直接引发了异常。
>>> ignore_exception()
Traceback (most recent call last):    # faulty中引发的异常依次从fault和ignore_exception向外传播，最终导致显示一条栈跟踪消息
一条栈跟踪消息
File '<stdin>', line 1, in ?
File '<stdin>', line 2, in ignore_exception
File '<stdin>', line 2, in faulty
Exception: Something is wrong
>>> handle_exception()    # 调用handle_exception时，异常最终传播到handle_exception，并被这里的try/except语句处理。
try/except语句处理。
Exception handled
```

## 8.5 异常之禅

如果你知道代码可能引发某种异常，且不希望出现这种异常时程序终止并显示栈跟踪消息，可添加必要的try/except或try/finally语句（或结合使用）来处理它。
```python
def describe_person(person):
    print('Description of', person['name'])
    print('Age:', person['age'])
    try:
        print('Occupation:', person['occupation'])
    except KeyError: pass   # 如果这个键不存在，将引发KeyError异常，而except子句将捕获这个异常。
```
这里只查找了person['occupation']一次，如果用`if 'occupation' in person:`语句要先找一次，有的话打印时又找了一次。
<br>检查对象是否包含特定的属性时，try/except也很有用。
```Python
try:
    obj.write    # try子句只是访问属性write，而没有使用它来做任何事情
except AttributeError:    
    # 如果引发了AttributeError异常，说明对象没有属性write，否则就说明有这个属性。
    # 可替代7.2.9节介绍的使用getattr的解决方案，而且更自然。
    print('The object is not writeable')
else:
    print('The object is writeable')
```
注意: 这在效率方面的提高微乎其微。一般而言，除非程序存在性能方面的问题，否则不应过多考虑这样的优化。关键是在很多情况下，相比于使用if/else，**使用try/except语句更自然，也更符合Python的风格**。因此你应养成尽可能使用try/except语句的习惯①。

## 8.6 不那么异常的情况: 警告

如果你只想发出警告，指出情况偏离了正轨，可使用模块warnings中的函数warn。
```Python
>>> from warnings import warn
# 警告只显示一次。如果再次运行最后一行代码，什么事情都不会发生。
>>> warn("I've got a bad feeling about this.")
__main__:1: UserWarning: I've got a bad feeling about this.
```
如果其他代码在使用你的模块，可使用模块warnings中的函数filterwarnings来抑制你发出的警告（或特定类型的警告），并指定要采取的措施，如"error"或"ignore"。
```Python
>>> from warnings import filterwarnings
>>> filterwarnings("ignore")    # 抑制警告
>>> warn("Anyone out there?")
>>> filterwarnings("error")    # 打开警告
>>> warn("Something is very wrong!")
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
UserWarning: Something is very wrong!    # 引发的异常为UserWarning。
```
发出警告时，可指定将引发的异常（即警告类别），但必须是Warning的子类。如果将警告转换为错误，将使用你指定的异常。另外，还可根据异常来过滤掉特定类型的警告。
```Python
>>> filterwarnings("error")
>>> warn("This function is really old...", DeprecationWarning)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
DeprecationWarning: This function is really old...
>>> filterwarnings("ignore", category=DeprecationWarning)   # 只抑制/过滤这一个警告
>>> warn("Another deprecation warning.", DeprecationWarning)
>>> warn("Something else.")
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
UserWarning: Something else.
```
模块warnings还提供了一些高级功能。如果你对此感兴趣，请参阅库参考手册。

## 8.7 小结

本章介绍了如下重要主题。
* **异常对象**：异常情况（如发生错误）是用异常对象表示的。对于异常情况，有多种处理方式；如果忽略，将导致程序终止。
* **引发异常**：可使用raise语句来引发异常。它将一个异常类或异常实例作为参数，但你也可提供两个参数（异常和错误消息）。如果在except子句中调用raise时没有提供任何参数，它将重新引发该子句捕获的异常。
* **自定义的异常类**：你可通过从Exception派生来创建自定义的异常。
* **捕获异常**：要捕获异常，可在try语句中使用except子句。在except子句中，如果没有指定异常类，将捕获所有的异常。你可指定多个异常类，方法是将它们放在元组中。如果向except提供两个参数，第二个参数将关联到异常对象。在同一条try/except语句中，可包含多个except子句，以便对不同的异常采取不同的措施。
* **else子句**：除except子句外，你还可使用else子句，它在主try块没有引发异常时执行。
* **finally**：要确保代码块（如清理代码）无论是否引发异常都将执行，可使用try/finally，并将代码块放在finally子句中。
* **异常和函数**：在函数中引发异常时，异常将传播到调用函数的地方（对方法来说亦如此）。
* **警告**：警告类似于异常，但（通常）只打印一条错误消息。你可指定警告类别，它们是Warning的子类。
