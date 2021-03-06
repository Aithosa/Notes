# C++ 基础知识

1. extern关键字的作用

    extern置于变量或函数前，用于标示变量或函数的定义在别的文件中，提示编译器遇到此变量和函数时在其他模块中寻找其定义。
    <br>当extern不与“C”在一起修饰变量或函数时，如：`extern int g_Int；`它的作用就是声明函数或全局变量的作用范围的关键字，其声明的函数和变量可以在本模块或其他模块中使用。记住它是一个声明不是定义!也就是说B模块(编译单元)要是引用模块(编译单元)A中定义的全局变量或函数时，它只要包含A模块的头文件即可,在编译阶段，模块B虽然找不到该函数或变量，但它不会报错，它会在连接时从模块A生成的目标代码中找到此函数。

2. `sizeof` 和 `strlen` 的区别

    ① `sizeof` 是一个操作符，`strlen` 是库函数。

    ② `sizeof` 的参数可以是数据的类型，也可以是变量，而 `strlen` 只能以结尾为`\ 0`的字符串作参数。

    ③ 编译器在**编译**时就计算出了sizeof 的结果。而strlen 函数必须在**运行**时才能计算出来。并且 sizeof计算的是**数据类型**占内存的大小，而 strlen 计算的是字符串实际的长度。

    ④ 数组做 sizeof 的参数不退化，传递给 strlen 就退化为指针了。

3. C中的 malloc 和C++中的 new 有什么区别?

    ① new、delete 是**操作符**，可以重载，只能在 C++中使用。
    <br>malloc、free 是**函数**，可以覆盖，C、C++中都可以使用。

    ② new  可以调用对象的构造函数，对应的 delete 调用相应的析构函数。
    <br>malloc 仅仅分配内存，free 仅仅回收内存，并不执行构造和析构函数

    ③ new、delete 返回的是某种**数据类型指针**，malloc、free 返回的是 **void 指针**。

    > 注意：malloc 申请的内存空间要用 free 释放，而 new 申请的内存空间要用 delete 释放，不要混用。因为两者实现的机理不同。

4. c/c++中static

    要理解static，就必须要先理解另一个与之相对的关键字auto，其实我们通常声明的不用static修饰的变量，都是auto的，因为它是默认的。auto的含义是由程序自动控制变量的生存周期，通常指的就是变量在进入其作用域的时候被分配，离开其作用域的时候被释放；而static就是不auto，变量在程序初始化时被分配，直到程序退出前才被释放；也就是static是按照程序的生命周期来分配释放变量的，而不是变量自己的生命周期。

5. 简述C\C++程序编译的内存情况分配

    C、C++中内存分配方式可以分为三种：

    ① 从静态存储区域分配：内存在程序编译时就已经分配好，这块内存在程序的整个运行期间都存在。速度快、不容易出错，因为有系统会善后。例如全局变量，static变量等。

    ② 在栈上分配：在执行函数时，函数内局部变量的存储单元都在栈上创建，函数执行结束时这些存储单元自动被释放。栈内存分配运算内置于处理器的指令集中，效率很高，但是分配的内存容量有限。

    ③ 从堆上分配：即动态内存分配。程序在运行的时候用 malloc 或 new 申请任意大小的内存，程序员自己负责在何时用 free 或 delete 释放内存。动态内存的生存期由程序员决定，使用非常灵活。如果在堆上分配了空间，就有责任回收它，否则运行的程序会出现内存泄漏，另外频繁地分配和释放不同大小的堆空间将会产生堆内碎块。

    一个 C、C++程序编译时内存分为 5 大存储区：堆区、栈区、全局区、文字常量区、程序代码区。

6. 面向对象的三大特征

    ① **封装**，也就是把客观事物封装成抽象的类，并且类可以把自己的数据和方法只让可信的类或者对象操作，对不可信的进行信息隐藏。

    ② **继承**，是指这样一种能力：它可以使用现有类的所有功能，并在无需重新编写原来的类的情况下对这些功能进行扩展。通过继承创建的新类称为“子类”或“派生类”。继承的过程，就是从一般到特殊的过程。要实现继承，可以通过“继承”和“组合”来实现。

    ③ **多态**，简单的说，就是一句话：允许将指向子类类型的指针赋值给父类类型的指针。
    <br>实现多态，有二种方式，覆盖，重载。

    * **覆盖**，是指子类重新定义父类的虚函数的做法。

    * **重载**，是指允许存在多个同名函数，而这些函数的参数表不同（或许参数个数不同，或许参数类型不同，或许两者都不同）。

    总结：作用

    ① 封装可以隐藏实现细节，使得代码模块化

    ② 继承可以扩展已存在的代码模块（类）；它们的目的都是为了——**代码重用**

    ③ 多态则是为了实现另一个目的——**接口重用**！多态的作用，就是为了类在继承和派生的时候，保证使用“家谱”中任一类的实例的某一属性时的正确调用。

7. 简述多态的实现原理

    编译器发现一个类中有**虚函数**，便会立即为此类生成**虚函数表vtable**。虚函数表的各表项为指向对应虚函数的指针。编译器还会在此类中隐含插入一个指针 vptr指向虚函数表。调用此类的构造函数时，在类的构造函数中，编译器会隐含执行 vptr 与 vtable 的关联代码，将 vptr 指向对应的 vtable，将类与此类的 vtable 联系了起来。
    <br>另外在调用类的构造函数时，指向基础类的指针此时已经变成指向具体的类的 this 指针，这样依靠此 this 指针即可得到正确的 vtable。

    如此才能真正与函数体进行连接，这就是动态联编，实现多态的基本原理。

    > 注意：一定要区分虚函数，纯虚函数、虚拟继承的关系和区别。牢记虚函数实现原理，因为多态C++面试的重要考点之一，而虚函数是实现多态的基础。

8. c++空类的成员函数

    * 缺省的**构造函数**
    * 缺省的拷贝构造函数
    * 缺省的**赋值运算符**
    * 缺省的**析构函数**
    * 缺省的取址运算符
    * 缺省的取址运算符const

    > 注意：只有当实际使用这些函数的时候，编译器才会去定义它们。

9. 谈谈你对拷贝构造函数和赋值运算符的认识

    两个不同之处：

    ① 拷贝构造函数生成**新的类对象**，而赋值运算符不能。

    ② 由于拷贝构造函数是直接构造一个新的类对象，所以在初始化这个对象之前**不用检验源对象是否和新建对象相同**。而赋值运算符则需要这个操作，另外赋值运算中如果原来的对象中有内存分配要**先把内存释放掉**。

    > 注意：当有类中有**指针类型的成员变量**时，一定要重写拷贝构造函数和赋值运算符，不要使用默认的。

10. 用 C++设计一个不能被继承的类

    ```C++
    class Base

    {

        private:

           Base() {}

           ~Base() {}

    };

    class Derived : public Base

    {

        public:

           Derived() : Base() {}

           ~Derived() {}

    };
    ```
    C++ 中的流对象就是采用这样的原理。防止被赋值、复制。

11. 类成员的重写、重载和隐藏的区别

    重写和重载主要有以下几点不同：

    ① **范围** 的区别：被重写的和重写的函数在两个类中，而重载和被重载的函数在同一个类中。

    ② **参数** 的区别：被重写函数和重写函数的参数列表一定相同，而被重载函数和重载函数的参数列表一定不同。

    ③ virtual 的区别：重写的基类中被重写的函数必须要有 virtual 修饰，而重载函数和被重载函数可以被virtual 修饰，也可以没有。

    隐藏和重写、重载有以下几点不同：

    ① 与重载的范围不同：和重写一样，隐藏函数和被隐藏函数不在同一个类中

    ② 参数的区别：隐藏函数和被隐藏的函数的参数列表可以相同，也可不同，但是函数名肯定要相同。当参数不相同时，无论基类中的参数是否被 virtual 修饰，基类的函数都是被隐藏，而不是被重写

    说明：虽然重载和覆盖都是实现多态的基础，但是两者实现的技术完全不相同，达到的目的也是完全不同的，覆盖是动态绑定的多态，而重载是静态绑定的多态。

12. extern 有什么作用

    extern 标识的变量或者函数声明其定义在别的文件中，提示编译器遇到此变量和函数时在其它模块中寻找其定义。

13. 引用和指针区别

    ① 引用必须被初始化，但是不分配存储空间。指针不必在声明时初始化，在初始化的时候需要分配存储空间

    ② 引用初始化以后不能被改变，指针可以改变所指的对象

    ③ 不存在指向空值的引用，但是存在指向空值的指针

14. 数组指针

    ```C++
    #include<iostream>

    using namespace std;

    int main()

    {

        int a[5] = {1, 2, 3, 4, 5};

        int *ptr = (int*)(&a+1);

        cout << *(ptr-1) << "\t" << *(ptr-2) << endl; // 5 4
        cout << "----------------" << endl;

        int *p = (int *)(a+1);            //2

        cout << *p << endl;

    }
    ```

    15. const int *a  和 int * const a 区别

    ```C++
    #include<iostream>

    using namespace std;

    int main()

    {

      int b = 3;
      int c = 4;

      const int *p = &b;  //等价于 int const *p = &b;

      p = &c;        //修饰值，指针可变

                  //*p = 5;//error 修饰值，值不可变

      cout << *p << endl;

      int a = 5;
      int * const q = &a;   //修饰指针

                  //p = &c;//error修饰指针，指针不可变

      *p = 5;        //修饰指针，值可变

    }
    ```

16. C++友元函数和友元类（C++ friend）

    私有成员只能在类的成员函数内部访问，如果想在别处访问对象的私有成员，只能通过类提供的接口（成员函数）间接地进行。这固然能够带来数据隐藏的好处，利于将来程序的扩充，但也会增加程序书写的麻烦。

    C++ 设计者认为， 如果有的程序员真的非常怕麻烦，就是想在类的成员函数外部直接访问对象的私有成员，那还是做一点妥协以满足他们的愿望为好，这也算是眼前利益和长远利益的折中。因此，C++ 就有了友元（friend）的概念。打个比方，这相当于是说：朋友是值得信任的，所以可以对他们公开一些自己的隐私。

    友元分为两种：友元函数和友元类。

    1. 友元函数

        在定义一个类的时候，可以把一些函数（包括全局函数和其他类的成员函数）声明为“友元”，这样那些函数就成为该类的友元函数，在友元函数内部就可以访问该类对象的私有成员了。

        将全局函数声明为友元的写法如下：
        `friend  返回值类型  函数名(参数表);`

        将其他类的成员函数声明为友元的写法如下：
        `friend  返回值类型  其他类的类名::成员函数名(参数表);`

        > 注：不能把其他类的私有成员函数声明为友元。

        ```C++
        #include<iostream>

        using namespace std;

        class CCar;  //提前声明CCar类，以便后面的CDriver类使用

        class CDriver
        {
            public:
                void ModifyCar(CCar* pCar);  //改装汽车
        };

        class CCar
        {
            private:
                int price;
                friend int MostExpensiveCar(CCar cars[], int total);  //声明友元
                friend void CDriver::ModifyCar(CCar* pCar);  //声明友元
        };

        void CDriver::ModifyCar(CCar* pCar)
        {
            pCar->price += 1000;  //汽车改装后价值增加
        }

        int MostExpensiveCar(CCar cars[], int total)  //求最贵气车的价格
        {
            int tmpMax = -1;
            for (int i = 0; i<total; ++i)
                if (cars[i].price > tmpMax)
                    tmpMax = cars[i].price;
            return tmpMax;
        }

        int main()
        {
            return 0;
        }
        ```

        第 13 行将全局函数 `MostExpensiveCar` 声明为 `CCar` 类的友元，因此在第 24 行可以访问 cars[i] 的私有成员 price。同理，第 14 行将 CDriver 类的 ModifyCar 成员函数声明为友元，因此在第 18 行可以访问 pCar 指针所指向的对象的私有成员变量 price。

    2. 友元类

        一个类 A 可以将另一个类 B 声明为自己的友元，类 B 的所有成员函数就都可以访问类 A 对象的私有成员。在类定义中声明友元类的写法如下：`friend  class  类名;`

        ```C++
        class CCar
        {
        private:
            int price;
            friend class CDriver;  //声明 CDriver 为友元类
        };

        class CDriver
        {
        public:
            CCar myCar;
            void ModifyCar()  //改装汽车
            {
                myCar.price += 1000;  //因CDriver是CCar的友元类，故此处可以访问其私有成员
            }
        };

        int main()
        {
            return 0;
        }
        ```

        第 5 行将 CDriver 声明为 CCar 的友元类。这条语句本来就是在声明 CDriver 是一个类，所以 CCar 类定义前面就不用声明 CDriver 类了。第 5 行使得 CDriver 类的所有成员函数都能访问 CCar 对象的私有成员。如果没有第 5 行，第 13 行对 myCar 私有成员 price 的访问就会导致编译错误。

        一般来说，类 A 将类 B 声明为友元类，则类 B 最好从逻辑上和类 A 有比较接近的关系。例如上面的例子，CDriver 代表司机，CCar 代表车，司机拥有车，所以 CDriver 类和 CCar 类从逻辑上来讲关系比较密切，把 CDriver 类声明为 CCar 类的友元比较合理。

        **友元关系在类之间不能传递**，即类 A 是类 B 的友元，类 B 是类 C 的友元，并不能导出类 A 是类 C 的友元。“咱俩是朋友，所以你的朋友就是我的朋友”这句话在 C++ 的友元关系上 不成立。

16. 多态

    [资料1](https://blog.csdn.net/qq_39412582/article/details/81628254)
    <br>[资料2](http://c.biancheng.net/view/264.html)

17. 泛型编程

    [资料1](https://blog.csdn.net/sevenjoin/article/details/88538692)

18.

    [资料](https://blog.csdn.net/weixin_43819197/article/details/94407751)


https://www.cnblogs.com/LUO77/p/5771237.html

