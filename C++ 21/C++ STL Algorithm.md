# 使用STL 算法

## 1. 根据值或条件查找元素
```C++
auto element = find (numsInVec.cbegin(), // Start of range
					 numsInVec.cend(), // End of range
					 numToFind); // Element to find

// find_if( )的用法与此类似，但需要通过第三个参数提供一个一元谓词（返回true 或false 的一元函数）
auto evenNum = find_if (numsInVec.cbegin(), // Start of range
						numsInVec.cend(), // End of range
						[](int element) { return (element % 2) == 0; } );

// Check if find() succeeded
if (element != numsInVec.cend ())
	cout << "Result: Value found!" << endl;
```

这两个函数都返回一个迭代器，您需要将其同容器的`end( )`或`cend( )`进行比较，检查查找操作是否
成功。如果成功，便可进一步使用该迭代器。

## 2. 计算包含给定值或满足给定条件的元素数

算法`std::count( )`和`count_if( )`计算给定范围内的元素数。


1. `std::count( )`计算包含给定值（使用相等运算符==进行测试）的元素数：
```C++
size_t numZeroes = count (numsInVec.cbegin (), numsInVec.cend (), 0);
cout << "Number of instances of '0': " << numZeroes << endl;
```

2. `std::count_if( )`计算这样的元素数，即满足通过参数传递的一元谓词（可以是函数对象，也可以是lambda 表达式）：
```C++
// Unary predicate:
template <typename elementType>
bool IsEven (const elementType& number)
{
return ((number % 2) == 0); // true, if even
}
...
// Use the count_if algorithm with the unary predicate IsEven:
size_t numEvenNums = count_if (numsInVec.cbegin (),
							   numsInVec.cend (), 
							   IsEven <int> );
cout << "Number of even elements: " << numEvenNums << endl;
```

> 注: 使用lambda 表达式可节省多行代码，但别忘了，如果将这两个示例合并成一个，则可将`IsEven( )`用于`find_if( )`和`count_if( )`中，从而提高了代码的可重用性。

## 3. 在集合中搜索元素或序列

有时需要查找**序列**或**模式**。在这种情况下，应使用`search( )`或`search_n( )`。`search( )`用于在一个序列中查找另一个序列：
```C++
auto range = search (numsInVec.cbegin(), // Start range to search in
					 numsInVec.cend(), // End range to search in
					 numsInList.cbegin(), // start range to search
					 numsInList.cend() ); // End range to search for
```

`search_n( )`用于在容器中查找n 个相邻的指定值：
```C++
auto partialRange = search_n (numsInVec.cbegin(), // Start range
							  numsInVec.cend(), // End range
							  3, // num items to be searched for
							  9); // value to search for
```
这两个函数都返回一个迭代器，它指向找到的第一个模式；使用该迭代器之前，务必将其与`end( )`进行比较。

## 4. 将容器中的元素初始化为指定值

STL算法`fill( )`和`fill_n( )`用于将指定范围的内容设置为指定值。

1. `fill( )`将指定范围内的元素设置为指定值
```C++
vector <int> numsInVec (3);
// fill all elements in the container with value 9
fill (numsInVec.begin (), numsInVec.end (), 9);
```

2. `fill_n( )`将n个元素设置为指定的值，接受的参数包括起始位置、元素数以及要设置的值
```C++
fill_n (numsInVec.begin () + 3, /*count*/ 3, /*fill value*/ -9);
```
> 注: fill( )算法对整个vector 进行操作，而fill_n( )可对vector的一部分进行操作。

## 5. 使用`std::generate( )`将元素设置为运行阶段生成的值

函数`fill( )`和`fill_n( )`将集合的元素设置为指定的值，而`generate( )`和`generate_n( )`等STL算法用于将集合的内容设置为一元函数返回的值。

可使用`generate( )`将指定范围内的元素设置为生成器函数返回的值
```C++
generate (numsInVec.begin (), numsInVec.end (), // range
		  rand); // generator function
```

`generate_n( )`与`generate( )`类似，但您指定的是要设置的元素数，而不是闭区间

```C++
generate_n (numsInList.begin (), 5, rand);
```

因此，可使用这两种算法将容器设置为文件的内容或随机值。

```C++
#include <ctime>
srand(time(NULL)); // seed random generator using time
```

## 6. 使用`for_each( )`处理指定范围内的元素

算法`for_each( )`对指定范围内的每个元素执行指定的一元函数对象，其用法如下

```C++
fnObjType retValue = for_each (start_of_range,
							   end_of_range,
							   unaryFunctionObject);
```
也可使用接受一个参数的lambda表达式代替一元函数对象。
<br>返回值表明，`for_each( )`返回用于对指定范围内的每个元素进行处理的函数对象（functor）。这意味着使用结构或类作为函数对象可存储状态信息，并在for_each( )执行完毕后查询这些信息。

```C++
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

template <typename elementType>
struct DisplayElementKeepcount
{
	int count;
	DisplayElementKeepcount (): count (0) {}

	void operator () (const elementType& element)
	{
		++ count;
		cout << element << ' ';
	}
};

int main ()
{
	vector <int> numsInVec{ 2017, 0, -1, 42, 10101, 25 };

	cout << "Elements in vector are: " << endl;
	DisplayElementKeepcount<int> functor = for_each (numsInVec.cbegin(), // Start of range
													 numsInVec.cend (), // End of range
			  										 DisplayElementKeepcount<int> ());// functor
	cout << endl;

	// Use the state stored in the return value of for_each!
	cout << "'" << functor.count << "' elements displayed" << endl;

	string str ("for_each and strings!");
	cout << "Sample string: " << str << endl;

	cout << "Characters displayed using lambda:" << endl;
	int numChars = 0;
	for_each (str.cbegin(),
			  str.cend (),
			  [&numChars](char c) { cout << c << ' '; ++numChars; } );

	cout << endl;
	cout << "'" << numChars << "' characters displayed" << endl;

	return 0;
}
```

```
Elements in vector are:
2017 0 -1 42 10101 25
'6' elements displayed
Sample string: for_each and strings!
Characters displayed using lambda:
f o r _ e a c h a n d s t r i n g s !
'21' characters displayed
```

## 7. 使用`std::transform( )`对范围进行变换

`std::for_each( )`和`std::transform( )`很像，都对源范围内的每个元素调用指定的函数对象。然而，`std::transform( )`有两个版本。

1. 第一个版本一个接受一元函数，常用于将字符串转换为大写或小写（使用的一元函数分别是`toupper( )`和`tolower( )`）

```C++
string str ("THIS is a TEst string!");
transform (str.cbegin(), // start source range
		   str.cend(), // end source range
		   strLowerCaseCopy.begin(), // start destination range
		   ::tolower); // unary function
```

2. 第二个版本接受一个二元函数，让`transform( )`能够处理一对来自两个不同范围的元素

```C++
// sum elements from two vectors and store result in a deque
transform (numsInVec1.cbegin(), // start of source range 1
		   numsInVec1.cend(), // end of source range 1
		   numsInVec2.cbegin(), // start of source range 2
		   sumInDeque.begin(), // store result in a deque
		   plus<int>()); // binary function plus
```

不像`for_each( )`那样只处理一个范围，这两个版本的`transform( )`都将指定变换函数的结果赋给指定的目标范围。

> 注: 通过使用迭代器，可将容器及其实现同STL算法分离：`transform( )`是一种处理范围的算法，它无需知道实现这些范围的容器的细节。因此，虽然这里的输入范围为vector，而输出范围为deque，但该算法仍管用—只要指定范围的边界（提供给transform的输入参数）有效。

## 8. 复制和删除操作

STL 提供了三个重要的复制函数：`copy( )`、`copy_if( )`和`copy_backward( )`。

1. copy 沿向前的方向将源范围的内容赋给目标范围：
```C++
auto lastElement = copy (numsInList.cbegin(), // start source range
						 numsInList.cend(), // end source range
						 numsInVec.begin()); // start dest range
```

2. `copy_if( )`是C++11 新增的，仅在指定的一元谓词返回true时才复制元素：
```C++
// copy odd numbers from list into vector
copy_if (numsInList.cbegin(), numsInList.cend(),
		 lastElement, // copy position in dest range??? 开始的的位置，这里是接上一句结束的地方继续
		 [](int element){return ((element % 2) == 1);});
```

3. `copy_backward( )`沿向后的方向将源范围的内容赋给目标范围：
```C++
copy_backward (numsInList.cbegin (),
			   numsInList.cend (),
			   numsInVec.end ());
```

4. `remove( )`将容器中与指定值匹配的元素删除：
```C++
// Remove all instances of '0', resize vector using erase()
auto newEnd = remove (numsInVec.begin (), numsInVec.end (), 0);
numsInVec.erase (newEnd, numsInVec.end ());
```

5. `remove_if( )`使用一个一元谓词，并将容器中满足该谓词的元素删除：
```C++
// Remove all odd numbers from the vector using remove_if
auto newEnd = remove_if (numsInVec.begin (), numsInVec.end (),
						 [](int num) {return ((num % 2) == 1);} ); //predicate
numsInVec.erase (newEnd, numsInVec.end ()); // resizing
```

> 注: `remove( )`和`remove_if( )`都返回一个指向容器末尾的迭代器，但容器numsInVec 一直未调整大小。删除算法删除元素时，其他元素将向前移，但`size( )`返回的值没变，这意味着vector 末尾还有其他值。要调整容器的大小（这很重要，否则末尾将包含不需要的值），需要调用`erase( )`，并将`remove( )`或`remove_if( )`返回的迭代器传递给它。

## 9. 替换值以及替换满足给定条件的元素

STL算法`replace( )`与`replace_if( )`分别用于替换集合中等于指定值和满足给定条件的元素。

1. `replace( )`根据比较运算符==的返回值来替换元素：
```C++
cout << "Using 'std::replace' to replace value 5 by 8" << endl;
replace (numsInVec.begin (), numsInVec.end (), 5, 8);
```

2. `replace_if( )`需要一个用户指定的一元谓词，对于要替换的每个值，该谓词都返回true：
```C++
cout << "Using 'std::replace_if' to replace even values by -1" << endl;
replace_if (numsInVec.begin (), numsInVec.end (),
			[](int element) {return ((element % 2) == 0); }, -1);
```

```C++
#include <algorithm>
// shuffle the container
random_shuffle (numsInVec.begin (), numsInVec.end ());
```

## 10. 排序、在有序集合中搜索以及删除重复元素

1. 在实际的应用程序中，经常需要排序以及在有序范围内（出于性能考虑）进行搜索。

经常需要对一组信息进行排序，为此可使用STL算法`sort( )`：
```C++
sort (numsInVec.begin (), numsInVec.end ()); // ascending order
```

这个版本的`sort( )`将`std::less<>`用作二元谓词，而该谓词使用vector存储的数据类型实现的运算符<。

您可使用另一个重载版本，以指定谓词，从而修改排列顺序：
```C++
sort (numsInVec.begin (), numsInVec.end (),
	  [](int lhs, int rhs) {return (lhs > rhs);} ); // descending order
```

`stable_sort( )`确保排序后元素的相对顺序保持不变。 为了确保相对顺序保持不变，将降低性能，这是一个需要考虑的因素，尤其在元素的相对顺序不重要时。

2. 在显示集合的内容前，需要删除重复的元素。

要删除相邻的重复值，可使用`unique( )`：
```C++
auto newEnd = unique (numsInVec.begin (), numsInVec.end ());
numsInVec.erase (newEnd, numsInVec.end ()); // to resize
```

3. 要进行快速查找，可使用STL算法`binary_search( )`，这种算法只能用于有序容器：
```C++
bool elementFound = binary_search (numsInVec.begin (), numsInVec.end (), 2011);
if (elementFound)
	cout << "Element found in the vector!" << endl;
```

程序清单23.10 使用STL 算法`std::sort( )`将一个范围排序，使用`std::binary_search( )`在有序的范围内进行搜索，然后使用`std::unique( )`删除相邻的重复元素（执行`sort( )`后，重复的元素将彼此相邻）。

> 注: 为避免容器末尾包含不想要或未知的值，务必在调用`unique( )`后调用`vector::erase( )`，并将`unique( )`返回的迭代器传递给它。

## 11. 将范围分区

`std::partition( )`将输入范围分为两部分：一部分满足一元谓词；另一部分不满足：
```C++
bool IsEven (const int& num) // unary predicate
{
	return ((num % 2) == 0);
}
...
partition (numsInVec.begin(), numsInVec.end(), IsEven);
```

然而，`std::partition( )`不保证每个分区中元素的相对顺序不变。在相对顺序很重要，需要保持不变时，应使用`std::stable_partition( )`：
```C++
stable_partition (numsInVec.begin(), numsInVec.end(), IsEven);
```

> 注: 保持相对顺序不变是有代价的，这种代价可能很小，也可能很大，这取决于包含在范围中的对象类型。

## 12. 在有序集合中插入元素

将元素插入到有序集合中时，将其插入到正确位置很重要。为了满足这种需求，STL提供了`lower_bound( )`和`upper_bound( )`等函数：
```C++
auto minInsertPos = lower_bound (names.begin(), names.end(), "Brad Pitt");

cout << distance (names.begin (), minInsertPos) << endl;

// alternatively:
auto maxInsertPos = upper_bound (names.begin(), names.end(), "Brad Pitt");

cout << distance (names.begin (), maxInsertPos) << endl;
```

`lower_bound( )`和`upper_bound( )`都返回一个迭代器，分别指向在不破坏现有顺序的情况下，元素可插入到有序范围内的最前位置和最后位置。

注: 

* 使用算法`remove( )`、`remove_if( )`或`unique( )`后，务必使用容器的成员方法`erase( )`调整容器的大小。
* 使用`find( )`、`find_if( )`、`search( )`或`search_n( )`返回的迭代器之前，务必将其与容器的`end( )`进行比较，以确定它有效。
* 仅当元素的相对顺序很重要时，才应使用`stable_partition( )`（而不是`partition( )`）和`stable_sort( )`（而不是`sort( )`），因为`stable_*`可能降低应用程序的性能。
* 调用`unique( )`删除重复的相邻值之前，别忘了使用`sort( )`对容器进行排序。`sort( )`确保包含相同值的元素彼此相邻，这样`unique( )`才能发挥作用。
* 对于已排序的容器，不要在随机选择的位置插入元素， 而应将其插入到`lower_bound()`或`upper_bound()`返回的位置，以确保插入元素后容器依然是有序的。