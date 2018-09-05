# CH9 魔法方法、特性和迭代器

在Python中，有些名称很特别，开头和结尾都是两个下划线。你在本书前面已经见过一些，如`__future__`。这样的拼写表示名称有特殊意义，因此绝不要在程序中创建这样的名称。在这样的名称中，很大一部分都是魔法（特殊）方法的名称。如果你的对象实现了这些方法，它们将在特定情况下（具体是哪种情况取决于方法的名称）被Python调用，而几乎不需要直接调用。

## 9.1 如果你使用的不是Python 3

即便你使用的是较新的Python 2版本，有些功能（如特性和函数super）也不适用于旧式类。要让你的类是新式的，要么在模块开头包含赋值语句`__metaclass__ = type`（这在第7章提到过），要么直接或间接地继承内置类object或其他新式类。
```Python
class NewStyle(object):
    more_code_here

class OldStyle:
    more_code_here
```
*注意: 如果文件开头包含赋值语句`__metaclass__ = type`，这两个类都将是新式类。也可在类的作用域内给变量 `__metaclass__` 赋值， 但这样做只设置当前类的元类（metaclass）。元类是其他类所属的类，这是一个非常复杂的主题。*

注意，在Python 3中没有旧式类，因此无需显式地继承object或将`__metaclass__`设置为type。所有的类都将隐式地继承object。如果没有指定超类，将直接继承它，否则将间接地继承它。

## 9.2 构造函数

构造函数（constructor），其实就是本书前面一些示例中使用的初始化方法，只是命名为`__init__`。然而，构造函数不同于普通方法的地方在于，将在对象创建后自动调用它们。
<br>在Python中，创建构造函数很容易，只需将方法init的名称从普通的init改为魔法版`__init__`即可。
```Python
class FooBar:
    def __init__(self):
        self.somevar = 42
>>> f = FooBar()
>>> f.somevar
42
```
如果给构造函数添加几个参数:
```Python
class FooBar:
def __init__(self, value=42):
self.somevar = value
>>> f = FooBar('This is a constructor argument')
>>> f.somevar
'This is a constructor argument'
```
*注意: Python提供了魔法方法`__del__`，也称作析构函数（destructor）。这个方法在对象被销毁（作为垃圾被收集）前被调用，但鉴于你无法知道准确的调用时间，建议尽可能不要使用`__del__`。*

### 9.2.1 重写普通方法和特殊的构造函数

要在子类中添加功能，一种基本方式是 **添加方法**。然而，你可能想 **重写超类的某些方法**，以定制继承而来的行为。
<br>重写是继承机制的一个重要方面，对构造函数来说尤其重要。构造函数用于初始化新建对象
的状态，而对大多数子类来说，除超类的初始化代码外，还需要有自己的初始化代码。虽然所有
方法的重写机制都相同，但与重写普通方法相比，重写构造函数时更有可能遇到一个特别的问题：
**重写构造函数时，必须调用超类（继承的类）的构造函数，否则可能无法正确地初始化对象。**
```Python
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaah ...')
            self.hungry = False
        else:
            print('No, thanks!')
```
子类SongBird新增了鸣叫功能
```Python
class SongBird(Bird):
    def __init__(self):
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)
```
**子类缺少hungry，所以无法调用eat。因为在SongBird中重写了构造函数，但新的构造函数没有包含任何初始化属性hungry的代码。** 要消除这种错误，SongBird的构造函数必须调用其超类（Bird）的构造函数，以确保基本的初始化得以执行。为此，有两种方法：调用未关联的超类构造函数，以及使用函数`super`。

### 9.2.2 调用未关联的超类构造函数

调用超类的构造函数实际上很容易，也很有用。
```Python
class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)    # 程序的重点在传入了SongBird的self
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)
```
对实例调用方法时，方法的参数self将自动关联到实例（称为关联的方法）。然而，如果你 **通过类调用方法**（如`Bird.__init__`），就没有实例与其相关联。在这种情况下，你可随便设置参数self。这样的方法称为未关联的。
<br>通过将这个未关联方法的self参数设置为当前实例，将使用超类的构造函数来初始化SongBird对象。这意味着将设置其属性hungry。

### 9.2.3 使用函数super

函数super只适用于新式类。而你无论如何都应使用新式类。调用这个函数时，将当前类和当前实例作为参数。对其返回的对象调用方法时，调用的将是超类（而不是当前类）的方法。因此，在SongBird的构造函数中，可不使用Bird，而是使用`super(SongBird, self)`。另外，可像通常那样（也就是像调用关联的方法那样）调用方法`__init__`。在Python 3中调用函数super时，可不提供任何参数（通常也应该这样做），而它将像变魔术一样完成任务。
```Python
# 这个新式版本与旧式版本等效
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaah ...')
            self.hungry = False
        else:
            print('No, thanks!')

class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)
```
#### 使用函数super有何优点
**相比于直接对超类调用未关联方法，使用函数super更直观**，但这并非其唯一的优点。实际上，函数super很聪明，因此 **即便有多个超类，也只需调用函数super一次（条件是所有超类的构造函数也使用函数super）**。另外，对于使用旧式类时处理起来很棘手的问题（如两个超类从同一个类派生而来），在使用新式类和函数super时将自动得到处理。你无需知道函数super的内部工作原理，但必须知道的是，**使用函数super比调用超类的未关联构造函数（或其他方法）要好得多**。
<br>函数super返回的到底是什么呢？通常，只管假定它返回你所需的超类即可。实际上，它返回的是一个super对象，这个对象将负责为你执行方法解析。当你访问它的属性时，它将在所有的超类（以及超类的超类，等等）中查找，直到找到指定的属性或引发AttributeError异常。

## 9.3 元素访问

**注意**: 在Python中，协议通常指的是规范行为的规则，有点类似于第7章提及的接口。协议指定应实现哪些方法以及这些方法应做什么。在Python中，多态仅仅基于对象的行为（而不基于祖先，如属于哪个类或其超类等），因此这个概念很重要：其他的语言可能要求对象属于特定的类或实现了特定的接口，而Python通常只要求对象遵循特定的协议。因此，要成为序列，只需遵循序列协议即可。

### 9.3.1 基本的序列和映射协议

序列和映射基本上是元素（item）的集合，要实现它们的基本行为（协议），不可变对象需要实现2个方法，而可变对象需要实现4个。
* `__len__(self)`：这个方法应返回集合包含的项数，对序列来说为元素个数，对映射来说为键-值对数。如果`__len__`返回零（且没有实现覆盖这种行为的`__nonzero__`），对象在布尔上下文中将被视为假（就像空的列表、元组、字符串和字典一样）。
* `__getitem__(self, key)`：这个方法应返回与指定键相关联的值。对序列来说，键应该是0~n-1的整数（也可以是负数，这将在后面说明），其中n为序列的长度。对映射来说，键可以是任何类型。
* `__setitem__(self, key, value)`：这个方法应以与键相关联的方式存储值，以便以后能够使用`__getitem__`来获取。当然，仅当对象可变时才需要实现这个方法。
* `__delitem__(self, key)`：这个方法在对对象的组成部分使用`__del__`语句时被调用，应删除与key相关联的值。同样，仅当对象可变（且允许其项被删除）时，才需要实现这个方法。

对于这些方法，还有一些额外的要求。
* 对于序列，如果键为负整数，应从末尾往前数。换而言之，`x[-n]`应与`x[len(x)-n]`等效。
* 如果键的类型不合适（如对序列使用字符串键），可能引发TypeError异常。
* 对于序列，如果索引的类型是正确的，但不在允许的范围内，应引发IndexError异常。

要了解更复杂的接口和使用的抽象基类（Sequence），请参阅有关模块collections的文档。
```Python
# 创建一个无穷序列。
def check_index(key):
    """
    指定的键是否是可接受的索引？

    键必须是非负整数，才是可接受的。如果不是整数，
    将引发TypeError异常；如果是负数，将引发Index
    Error异常（因为这个序列的长度是无穷的）
    """
    if not isinstance(key, int): raise TypeError
    if key < 0: raise IndexError

class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        """
        初始化这个算术序列
        start -序列中的第一个值
        step -两个相邻值的差
        changed -一个字典，包含用户修改后的值
        """
        self.start = start # 存储起始值
        self.step = step # 存储步长值
        self.changed = {} # 没有任何元素被修改

    def __getitem__(self, key):
        """
        从算术序列中获取一个元素
        """
        check_index(key)
        try: return self.changed[key] # 修改过？
        except KeyError: # 如果没有修改过，
            return self.start + key * self.step # 就计算元素的值

    def __setitem__(self, key, value):
        """
        修改算术序列中的元素
        """
        check_index(key)
        self.changed[key] = value # 存储修改后的值
```
这些代码实现的是一个算术序列，其中任何两个相邻数字的差都相同。第一个值是由构造函数的参数start（默认为0）指定的，而相邻值之间的差是由参数step（默认为1）指定的。你允许用户修改某些元素，这是通过将不符合规则的值保存在字典changed中实现的。如果元素未被修改，就使用公式`self.start + key * self.step`来计算它的值。
```Python
>>> s = ArithmeticSequence(1, 2)
>>> s[4]
9
>>> s[4] = 2
>>> s[4]
2
>>> s[5]
11
>>> del s[4]    # 禁止删除元素，因此没有实现__del__
Traceback (most recent call last):
File "<stdin>", line 1, in ?
AttributeError: ArithmeticSequence instance has no attribute '__delitem__'
```
这个类没有方法`__len__`，因为其长度是无穷的。如果所使用索引的类型非法，将引发TypeError异常；如果索引的类型正确，但不在允许的范围内（即为负数），将引发IndexError异常。
```Python
>>> s["four"]
Traceback (most recent call last):
    File "<stdin>", line 1, in ?
    File "arithseq.py", line 31, in __getitem__
        check_index(key)
    File "arithseq.py", line 10, in checkIndex
        if not isinstance(key, int): raise TypeError
TypeError
>>> s[-42]    # 索引检查是由为此编写的辅助函数check_index负责的。
Traceback (most recent call last):
    File "<stdin>", line 1, in ?
    File "arithseq.py", line 31, in __getitem__
        check_index(key)
    File "arithseq.py", line 11, in checkIndex
        if key < 0: raise IndexError
IndexError
```

### 9.3.2 从list、dict 和str 派生

如果只想定制某种操作的行为，就没有理由去重新实现其他所有方法。“咒语”就是继承。。在能够继承的情况下为何去重新实现呢？在标准库中，模块collections提供了抽象和具体的基类，但你也可以继承内置类型。因此，如果要实现一种行为类似于内置列表的序列类型，可直接继承list。
```Python
# 一个带访问计数器的列表。
class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0
    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)
```
CounterList类深深地依赖于其超类（list）的行为。CounterList没有重写的方法（如append、extend、index等）都可直接使用。在两个被重写的方法中，使用super来调用超类的相应方法，并添加了必要的行为：初始化属性counter（在`__init__`中）和更新属性counter（在`__getitem__`中）。
<br>*注意: 重写`__getitem__`并不能保证一定会捕捉用户的访问操作，因为还有其他访问列表内容的方式，如通过方法pop。*
```Python
>>> cl = CounterList(range(10))
>>> cl
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> cl.reverse()
>>> cl
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> del cl[3:6]
>>> cl
[9, 8, 7, 3, 2, 1, 0]
>>> cl.counter    # 之前怎么没有增加counter
0
>>> cl[4] + cl[2]
9
>>> cl.counter
2
```
CounterList的行为在大多数方面都类似于列表，但它有一个counter属性（其初始值为0）。每当你访问列表元素时，这个属性的值都加1。执行加法运算`cl[4] + cl[2]`后，counter的值递增两次，变成了2。

## 9.4 其他魔法方法

## 9.5 特性

如果访问给定属性时必须采取特定的措施，那么像这样封装状态变量（属性）很重要。
```Python
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def set_size(self, size):
        self.width, self.height = size
    def get_size(self):
        return self.width, self.height

>>> r = Rectangle()
>>> r.width = 10
>>> r.height = 5
>>> r.get_size()
(10, 5)
>>> r.set_size((150, 100))
>>> r.width
150
```
如果有一天你想修改实现，**让size成为真正的属性**，而width和height是动态计算出来的，就需要提供用于访问width和height的存取方法，使用这个类的程序也必须重写。
<br>Python能够替你隐藏存取方法，让所有的属性看起来都一样。通过存取方法定义的属性通常称为特性（property）。

### 9.5.1 函数property

函数property使用起来很简单。如果你编写了一个类，只需再添加一行代码。
```Python
class Rectangle:
    def __init__ (self):
        self.width = 0
        self.height = 0
    def set_size(self, size):
        self.width, self.height = size
    def get_size(self):
        return self.width, self.height
    size = property(get_size, set_size)

# 属性size依然受制于get_size和set_size执行的计算，但看起来就像普通属性一样。
>>> r = Rectangle()
>>> r.width = 10
>>> r.height = 5
>>> r.size
(10, 5)
>>> r.size = 150, 100
>>> r.width
150
```
通过调用函数property并将存取方法作为参数（获取方法在前，设置方法在后）创建了一个特性，然后将名称size关联到这个特性。这样，你就能以同样的方式对待width、height和size，而无需关心它们是如何实现的。
<br>这里要说明的是，对于新式类，应使用特性而不是存取方法。

#### 函数property的工作原理
你可能很好奇，想知道特性是如何完成其魔法的，下面就来说一说
<br>property其实并不是函数，而是一个类。它的实例包含一些魔法方法，而所有的魔法都是由这些方法完成的。这些魔法方法为`__get__`、`__set__`和`__delete__`，它们一道定义了所谓的描述符协议。只要对象实现了这些方法中的任何一个，它就是一个描述符。描述符的独特之处在于其访问方式。例如，读取属性（具体来说，是在实例中访问类中定义的属性）时，如果它关联的是一个实现了`__get__`的对象，将不会返回这个对象，而是调用方法`__get__`并将其结果返回。实际上，这是隐藏在特性、关联的方法、静态方法和类方法（详细信息请参阅下一小节）以及`super`后面的机制。
<br>有关描述符的详细信息，请参阅Descriptor HowTo Guid（https://docs.python.org/3/howto/descriptor.html）。

### 9.5.2 静态方法和类方法

静态方法和类方法是这样创建的：将它们分别包装在staticmethod和classmethod类的对象中。静态方法的定义中没有参数self，可直接通过类来调用。类方法的定义中包含类似于self的参数，通常被命名为cls。对于类方法，也可通过对象直接调用，但参数cls将自动关联到类。
```Python
class MyClass:
    def smeth():
        print('This is a static method')
    smeth = staticmethod(smeth)
    def cmeth(cls):
        print('This is a class method of', cls)
    cmeth = classmethod(cmeth)
```
像这样手工包装和替换方法有点繁琐。在Python 2.4中，引入了一种名为装饰器的新语法，可用于像这样包装方法。（实际上，装饰器可用于包装任何可调用的对象，并且可用于方法和函数。）可指定一个或多个装饰器，为此可在方法（或函数）前面使用运算符@列出这些装饰器（**指定了多个装饰器时，应用的顺序与列出的顺序相反**）。
```Python
class MyClass:
    @staticmethod
    def smeth():
        print('This is a static method')
    @classmethod
    def cmeth(cls):
        print('This is a class method of', cls)

# 使用它们（无需实例化类）：
>>> MyClass.smeth()
This is a static method
>>> MyClass.cmeth()
This is a class method of <class '__main__.MyClass'>
```
在Python中，静态方法和类方法以前一直都不太重要，主要是因为从某种程度上说，总是可以使用函数或关联的方法替代它们，而且早期的Python版本并不支持它们。因此，虽然较新的代码没有大量使用它们，但它们确实有用武之地（如工厂函数），因此你或许应该考虑使用它们。

### 9.5.3 `__getattr__`、`__setattr__`等方法

可以拦截对对象属性的所有访问企图，其用途之一是在旧式类中实现特性（在旧式类中，函数property的行为可能不符合预期）。要在属性被访问时执行一段代码，必须使用一些魔法方法。下面的四个魔法方法提供了你需要的所有功能（在旧式类中，只需使用后面三个）。
* `__getattribute__(self, name)`：在属性被访问时自动调用（只适用于新式类）。
* `__getattr__(self, name)`：在属性被访问而对象没有这样的属性时自动调用。
* `__setattr__(self, name, value)`：试图给属性赋值时自动调用。
* `__delattr__(self, name)`：试图删除属性时自动调用。

相比函数property，这些魔法方法使用起来要棘手些（从某种程度上说，效率也更低），但它们很有用，因为你可在这些方法中编写处理多个特性的代码。然而，在可能的情况下，还是使用函数property吧。
```Python
# 再来看前面的Rectangle示例，但这里使用的是魔法方法：
class Rectangle:
    def __init__ (self):
        self.width = 0
        self.height = 0
    def __setattr__(self, name, value):
        if name == 'size': #
            self.width, self.height = value
        else:
            self. __dict__[name] = value
    def __getattr__(self, name):
        if name == 'size': #
            return self.width, self.height
        else:
            raise AttributeError()
```
如你所见，这个版本需要处理额外的管理细节。对于这个代码示例，需要注意如下两点。
* 即便涉及的属性不是size，也将调用方法`__setattr__`。因此这个方法必须考虑如下两种情形：
    * 如果涉及的属性为size，就执行与以前一样的操作；
    * 否则就使用魔法属性`__dict__`。
<br>`__dict__`属性是一个字典，其中包含所有的实例属性。之所以使用它而不是执行常规属性赋值，是因为旨在避免再次调用`__setattr__`，进而导致无限循环。
* 仅当没有找到指定的属性时，才会调用方法`__getattr__`。这意味着如果指定的名称不是
size，这个方法将引发AttributeError异常。这在要让类能够正确地支持hasattr和getattr
等内置函数时很重要。如果指定的名称为size，就使用前一个实现中的表达式。

注意: 前面说过，编写方法`__setattr__`时需要避开无限循环陷阱，编写`__getattribute__`时亦如此。由于它拦截对所有属性的访问（在新式类中），因此将拦截对`__dict__`的访问！在`__getattribute__`中访问当前实例的属性时，唯一安全的方式是使用超类的方法`__getattribute__`（使用super）。

## 9.6 迭代器

### 9.6.1 迭代器协议

迭代（iterate）意味着重复多次，就像循环那样。本书前面只使用for循环迭代过序列和字典，但实际上也可迭代其他对象：实现了方法`__iter__`的对象。
<br>方法`__iter__`返回一个迭代器，它是包含方法`__next__`的对象，而调用这个方法时可不提供任何参数。当你调用方法`__next__`时，迭代器应返回其下一个值。如果迭代器没有可供返回的值，应引发StopIteration异常。你还可使用内置的便利函数next，在这种情况下，`next(it)`与`it.__next__()`等效。
<br>*注意 在Python 3中，迭代器协议有细微的变化。在以前的迭代器协议中，要求迭代器对象包含方法next而不是`__next__`。*

为何不使用列表呢？因为在很多情况下，使用列表都有点像用大炮打蚊子。如果有很多值，列表可能占用太多的内存。但还有其他原因：使用迭代器更通用、更简单、更优雅。
```Python
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
    def __iter__(self):
        return self
```
注意到这个迭代器实现了方法`__iter__`，而这个方法返回迭代器本身。在很多情况下，都在另一个对象中实现返回迭代器的方法`__iter__`，并在for循环中使用这个对象。但推荐在迭代器中也实现方法`__iter__`（并像刚才那样让它返回self），这样迭代器就可直接用于for循环中。
<br>*注意 更正规的定义是，实现了方法`__iter__`的对象是可迭代的，而实现了方法`__next__`的对象是迭代器。*
```Python
# 首先，创建一个Fibs对象。
>>> fibs = Fibs()
# 然后就可在for循环中使用这个对象，如找出第一个大于1000的斐波那契数。
>>> for f in fibs:
...     if f > 1000:
...         print(f)
...         break
...
1597
```
提示: 通过对可迭代对象调用 **内置函数iter**，可获得一个迭代器。
```Python
>>> it = iter([1, 2, 3])
>>> next(it)
1
>>> next(it)
2
```
还可使用它从函数或其他可调用对象创建可迭代对象，详情请参阅库参考手册。

### 9.6.2 从迭代器创建序列

除了对迭代器和可迭代对象进行迭代（通常这样做）之外，还可将它们转换为序列。在可以使用序列的情况下，大多也可使用迭代器或可迭代对象（诸如索引和切片等操作除外）。
```Python
# 一个这样的例子是使用构造函数list显式地将迭代器转换为列表。
>>> class TestIterator:
...     value = 0
...     def __next__(self):
...         self.value += 1
...         if self.value > 10: raise StopIteration
...          return self.value
...     def __iter__(self):
...         return self
...
>>> ti = TestIterator()
>>> list(ti)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
## 9.7 生成器

生成器是一个相对较新的Python概念。由于历史原因，它也被称为简单生成器（simple generator）。生成器和迭代器可能是近年来引入的最强大的功能，但生成器是一个相当复杂的概念，你可能需要花些功夫才能明白其工作原理和用途。虽然生成器让你能够编写出非常优雅的代码，但请放心，无论编写什么程序，都完全可以不使用生成器。
**生成器是一种使用普通函数语法定义的迭代器**。生成器的工作原理到底是什么呢？下面先来看看如何创建和使用生成器，然后再看看幕后的情况。

### 9.7.1 创建生成器

创建一个将嵌套列表展开的函数。这个函数将一个类似于下面的列表作为参数：
<br>`nested = [[1, 2], [3, 4], [5]]``
<br>换而言之，这是一个列表的列表。函数应按顺序提供这些数字:
```Python
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element    # 包含yield语句的函数都被称为生成器

>>> list(flatten(nested))
[1, 2, 3, 4, 5]
```
生成器不是使用return返回一个值，而是可以生成多个值，每次一个。每次使用yield生成一个值后，函数都将冻结，即在此停止执行，等待被重新唤醒。被重新唤醒后，函数将从停止的地方开始继续执行。

#### 简单生成器
在Python 2.4中，引入了一个类似于列表推导（参见第5章）的概念：生成器推导（也叫生成器表达式）。其工作原理与列表推导相同，但不是创建一个列表（即不立即执行循环），而是返回一个生成器，让你能够逐步执行计算。
```Python
>>> g = ((i + 2) ** 2 for i in range(2, 27))
>>> next(g)
16
```
如你所见，不同于列表推导，这里使用的是圆括号。在像这样的简单情形下，还不如使用列表推导；但如果要包装可迭代对象（可能生成大量的值），使用列表推导将立即实例化一个列表，从而丧失迭代的优势。
<br>另一个好处是，**直接在一对既有的圆括号内（如在函数调用中）使用生成器推导时，无需再添加一对圆括号**。换而言之，可编写下面这样非常漂亮的代码：
<br>`sum(i ** 2 for i in range(10))`

### 9.7.2 递归式生成器

如果要处理任意层嵌套的列表，该求助于递归了。
```Python
def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested
```
调用flatten时，有两种可能性（处理递归时都如此）：基线条件和递归条件。在基线条件下，要求这个函数展开单个元素（如一个数）。在这种情况下，for循环将引发TypeError异常（因为你试图迭代一个数），而这个生成器只生成一个元素。
<br>然而，如果要展开的是一个列表（或其他任何可迭代对象），你就需要做些工作：遍历所有的子列表（其中有些可能并不是列表）并对它们调用flatten，然后使用另一个for循环生成展开后的子列表中的所有元素。这可能看起来有点不可思议，但确实可行。
<br>这个解决方案存在一个问题。如果nested是字符串或类似于字符串的对象，它就属于序列，因此不会引发TypeError异常，可你并不想对其进行迭代。
<br>*注意: 在函数flatten中，不应该对类似于字符串的对象进行迭代，主要原因有两个。
* 首先，你想将类似于字符串的对象视为原子值，而不是应该展开的序列。
* 其次，对这样的对象进行迭代会导致无穷递归，因为字符串的第一个元素是一个长度为1的字符串，而长度为1的字符串的第一个元素是字符串本身！*

要处理这种问题，必须在生成器开头进行检查。要检查对象是否类似于字符串，最简单、最快捷的方式是，尝试将对象与一个字符串拼接起来，并检查这是否会引发TypeError异常①。添加这种检查后的生成器如下：
```Python
def flatten(nested):
    try:
        # 不迭代类似于字符串的对象：
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
        yield element
    except TypeError:
        yield nested

# 这个版本也可用于字符串
>>> list(flatten(['foo', ['bar', ['baz']]]))
['foo', 'bar', 'baz']
```
这里没有执行类型检查：**我没有检查nested是否是字符串，而只是检查其行为是否类似于字符串，即能否与字符串拼接**。对于这种检查，一种更自然的替代方案是，使用isinstance以及字符串和类似于字符串的对象的一些抽象超类，但遗憾的是没有这样的标准类。另外，即便是对UserString来说，也无法检查其类型是否为str。

### 9.7.3 通用生成器

生成器是包含关键字yield的函数，但被调用时不会执行函数体内的代码，而是返回一个迭代器。每次请求值时，都将执行生成器的代码，直到遇到yield或return。yield意味着应生成一个值，而return意味着生成器应停止执行（即不再生成值；仅当在生成器调用return时，才能不提供任何参数）。
<br>换而言之，生成器由两个单独的部分组成：**生成器的函数** 和 **生成器的迭代器**。生成器的函数是由def语句定义的，其中包含yield。生成器的迭代器是这个函数返回的结果。用不太准确的话说，这两个实体通常被视为一个，通称为生成器。
<br>对于生成器的函数返回的迭代器``<generator object at 1510b0>``，可以像使用其他迭代器一样使用它。

### 9.7.4 生成器的方法

在生成器开始运行后，可使用生成器和外部之间的通信渠道向它提供值。这个通信渠道包含如下两个端点。
* **外部世界**：外部世界可访问生成器的方法send，这个方法类似于next，但接受一个参数（要发送的“消息”，可以是任何对象）。
* **生成器**：在挂起的生成器内部，yield可能用作表达式而不是语句。换而言之，当生成器重新运行时，yield返回一个值——通过send从外部世界发送的值。如果使用的是next，yield将返回None。

请注意，仅当生成器被挂起（即遇到第一个yield）后，使用send（而不是next）才有意义。要在此之前向生成器提供信息，可使用生成器的函数的参数。
<br>注意: 如果一定要在生成器刚启动时对其调用方法send，可向它传递参数None。
```Python
# 下面的示例很傻，但说明了这种机制：
def repeater(value):
    while True:
        new = (yield value)
        if new is not None: value = new

# 下面使用了这个生成器：
>>> r = repeater(42)
>>> next(r)
42
>>> r.send("Hello, world!")
"Hello, world!"
```
注意到使用圆括号将yield表达式括起来了。在有些情况下，并非必须这样做，但小心驶得万年船。**如果要以某种方式使用返回值，就不管三七二十一，将其用圆括号括起吧。**
<br>生成器还包含另外两个方法。
* **方法throw**：用于在生成器中（yield表达式处）引发异常，调用时可提供一个异常类型、一个可选值和一个traceback对象。
* **方法close**：用于停止生成器，调用时无需提供任何参数。

方法close（由Python垃圾收集器在需要时调用）也是基于异常的：在yield处引发GeneratorExit异常。因此如果要在生成器中提供一些清理代码，可将yield放在一条`try/finally`语句中。如果愿意，也可捕获GeneratorExit异常，但随后必须重新引发它（可能在清理后）、引发其他异常或直接返回。对生成器调用close后，再试图从它那里获取值将导致RuntimeError异常。

### 9.7.5 模拟生成器

较老的Python版本，就无法使用生成器。下面是一个简单的解决方案，让你能够使用普通函数模拟生成器。
<br>首先，在函数体开头插入如下一行代码：
<br>`result = []`
<br>如果代码已使用名称result，应改用其他名称。（在任何情况下，使用更具描述性的名称都是不错的主意。）接下来，将类似于`yield some_expression`的代码行替换为如下代码行：
```python
yield some_expression with this:
result.append(some_expression)
```
<br>最后，在函数末尾添加如下代码行：
<br>`return result`
<br>尽管使用这种方法并不能模拟所有的生成器，但可模拟大部分生成器。例如，这无法模拟无穷生成器，因为显然不能将这种生成器的值都存储到一个列表中。
```Python
def flatten(nested):
    result = []
    try:
    # 不迭代类似于字符串的对象：
    try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return result
```

## 9.8 八皇后问题

## 9.9 小结

本章介绍的内容很多，下面来总结一下。
* **新式类和旧式类**：Python类的工作方式在不断变化。较新的Python 2版本有两种类，其中旧式类正在快速退出舞台。新式类是Python 2.2引入的，提供了一些额外的功能，如支持函数`super`和`property`，而旧式类不支持。要创建新式类，必须直接或间接地继承object或设置`__metaclass__`。
* **魔法方法**：Python中有很多特殊方法，其名称以两个下划线开头和结尾。这些方法的功能各不相同，但大都由Python在特定情况下自动调用。例如`__init__`是在对象创建后调用的。
* **构造函数**：很多面向对象语言中都有构造函数，对于你自己编写的每个类，都可能需要为它实现一个构造函数。构造函数名为`__init__`，在对象创建后被自动调用。
* **重写**：类可重写其超类中定义的方法（以及其他任何属性），为此只需实现这些方法即可。要调用被重写的版本，可直接通过超类调用未关联版本（旧式类），也可使用函数super来调用（新式类）。
* **序列和映射**：要创建自定义的序列或映射，必须实现序列和映射协议指定的所有方法，其中包括`__getitem__`和`__setitem__`等魔法方法。通过从`list`（或UserList）和`dict`（或UserDict）派生，可减少很多工作量。
* **迭代器**：简单地说，迭代器是包含方法`__next__`的对象，可用于迭代一组值。没有更多的值可供迭代时，方法`__next__`应引发StopIteration异常。可迭代对象包含方法`__iter__`，它返回一个像序列一样可用于for循环中的迭代器。通常，迭代器也是可迭代的，即包含返回迭代器本身的方法`__iter__`。
* **生成器**：生成器的函数是包含关键字yield的函数，它在被调用时返回一个生成器，即一种特殊的迭代器。要与活动的生成器交互，可使用方法`send`、`throw`和`close`。
* **八皇后问题**：八皇后问题是个著名的计算机科学问题，使用生成器可轻松地解决它。这个问题要求在棋盘上放置8个皇后，并确保任何两个皇后都不能相互攻击。

### 9.9.1 本章介绍的新函数

|函 数|描 述|
|:|:|
|iter(obj) |从可迭代对象创建一个迭代器|
|next(it) |让迭代器前进一步并返回下一个元素|
|property(fget, fset, fdel, doc) |返回一个特性；所有参数都是可选的|
|super(class, obj) |返回一个超类的关联实例|

调用`iter`和`super`时，还可提供这里没有列出的其他参数，更详细的信息请参阅标准Python文档。
