# Appendix: A Command Line Crash Course

this is a copy from *Learn Python3 the hard way*

## 简介
**1. 如何使用本附录**

使用本附录的最佳方法是执行以下操作：

* 给自己一个小纸笔记本和一支笔。
* 从附录的开头开始，按照你的说法完成每项练习。
* 当您阅读的内容没有意义或者您不理解时，请将其写在笔记本中。留一点空间，以便你可以写一个答案。
* 完成练习后，请返回您的笔记本并查看您的问题。尝试通过在线搜索并询问可能知道答案的朋友来回答这些问题。请发送电子邮件至help@learncodethehardway.org，我也会帮助您。

继续完成这个练习的过程，写下你有的问题，然后回过头来回答你可以提出的问题。当你完成时，你实际上比你想到的使用命令行知道更多。

**2. 你会记住事物**

我提前警告你，我会立刻让你记住事情。这是让你有能力做某事的最快方法，但对于一些人来说，记忆是痛苦的。无论如何，只要通过它进行战斗。记忆是学习事物的重要技能，所以你应该克服对它的恐惧。

这是你记忆的方式：

* 告诉自己你会做到的。不要试图找到技巧或简单的方法，只需坐下来做它。
* 在一些索引卡上写下你想要记住的内容。把你需要学习的东西的一半放在另一边，然后另一半放在另一边。
* 每天大约15-30分钟，在索引卡上钻自己，试图回忆每一个。把你没有得到的任何卡片放到另一堆，只需钻那些卡片直到你感到无聊，然后尝试整个套牌，看看你是否有所改进。
* 在你上床睡觉之前，钻掉你错误的牌约5分钟，然后再去睡觉。

还有其他技术，比如你可以在一张纸上写下你需要学习的东西，将它层压，然后将它粘在你的淋浴墙上。当你在洗澡的时候，不用看就可以钻取知识，当你被困住时，可以瞥一眼它来刷新你的记忆。

如果你每天都这样做，你应该能够记住我告诉你在大约一周到一个月内记住的大部分内容。一旦你这样做，几乎所有其他东西变得更容易和直观，这是记忆的目的。它不是教你抽象的概念，而是为了使基础知识变得更加直观，你不必考虑它们。一旦你记住了这些基础知识，他们就会停止减速，阻止你学习更高级的抽象概念。

## 练习1：设置
在本附录中，您将被指示做三件事：

* 在shell中做一些事情（命令行，终端，PowerShell）。
* 了解你刚刚做了什么。
* 自己做更多。

对于第一次练习，您需要让您的终端打开并正常工作，以便您可以完成附录的其余部分。

**做这个**
<br>让您的终端，shell或PowerShell正常工作，以便您可以快速访问它并知道它的工作原理。

**1. 苹果系统**

对于macOS，您需要这样做：
* 按住命令键并按空格键。
* 将弹出“搜索栏”。
* 类型：终端
* 单击看起来像黑盒子的终端应用程序。
* 这将打开终端。
* 您现在可以转到停靠栏并按住CTRL键单击以拉出菜单，然后选择选项 - >保持停靠。

现在你打开了你的终端，它在你的码头，所以你可以到达它。

**2. Linux**

我假设如果你有Linux，那么你已经知道如何到达你的终端。查看窗口管理器的菜单，查找名为“Shell”或“Terminal”的任何内容。

**3. Windows**

在Windows上，我们将使用PowerShell。人们过去常常使用一个名为cmd.exe的程序，但它并不像PowerShell那样可用。如果您使用的是Windows 7或更高版本，请执行：

* 单击开始。
* 在“搜索程序和文件”中键入：powershell
* 按Enter键。

如果您没有Windows 7，则应认真考虑升级。如果您仍然坚持不升级，那么您可以尝试从Microsoft的下载中心安装Powershell。在线搜索以查找适用于您的Windows版本的“powershell downloads”。但是，你是独立的，因为我没有Windows XP，但希望PowerShell的体验是一样的。

**你了解到这一点**

您学习了如何打开终端，以便完成本附录的其余部分。

*注意
<br>如果你有一个非常聪明的朋友谁已经知道Linux，当他告诉你使用Bash以外的东西时忽略他。我教你Bash。而已。他会声称zsh会给你30多个智商点，并在股市中赢得数百万美元。忽略他。你的目标是获得足够的能力，在这个级别，你使用哪个shell并不重要。下一个警告是留在IRC或“黑客”闲逛的其他地方。他们认为把你的命令摧毁你的计算机很有趣。命令rm -rf /是一个你不能输入的经典。只是避免他们。如果您需要帮助，请确保您从您信任的人那里获得帮助，而不是从互联网上的随机白痴获得。*

**多做**
<br>这个练习有一个很大的“做多”部分。其他的练习并不像这个练习那么复杂，但是我通过做一些记忆让你为大脑的其余部分做好准备。请相信我：这将使以后的事情变得如丝般顺畅。

**Linux / MacOS**
<br>获取此命令列表并创建索引卡，其一侧为左侧名称，另一侧为定义。每天钻孔，同时继续本附录中的课程。

|names |definitions |
|:|:|
|pwd |print working directory|
|hostname |my computer's network name|
|mkdir |make directory|
|cd |change directory|
|ls |list directory|
|rmdir |remove directory|
|pushd |push directory|
|popd |pop directory|
|cp |copy a file or directory|
|mv |move a file or directory|
|less |page through a file|
|cat |print the whole file|
|xargs |execute arguments|
|find |find files|
|grep |find things inside files|
|man |read a manual page|
|apropos |find which man page is appropriate|
|env |look at your environment|
|echo |print some arguments|
|export |export/set a new environment variable|
|exit |exit the shell|
|sudo |DANGER! become super user root DANGER!|

**Windows**
<br>如果您使用的是Windows，那么这里是您的命令列表：

|names |definitions |
|:|:|
|pwd |print working directory|
|hostname |my computer's network name|
|mkdir |make directory|
|cd |change directory|
|ls |list directory|
|rmdir |remove directory|
|pushd |push directory|
|popd |pop directory|
|cp |copy a file or directory|
|robocopy |robust copy|
|mv |move a file or directory|
|more |page through a file|
|type |print the whole file|
|forfiles |run a command on lots of files|
|dir |-r find files|
|select-string |find things inside files|
|help |read a manual page|
|helpctr |find what man page is appropriate|
|echo |print some arguments|
|set |export/set a new environment variable|
|exit |exit the shell|
|runas |DANGER! become super user root DANGER!|

## 练习2：路径，文件夹，目录（pwd）

在本练习中，您将学习如何使用pwd命令打印工作目录。

我将教你如何阅读我向你展示的这些“会话”。您不必键入我在此处列出的所有内容，只需输入部分内容：

* You do not type in the $ (Unix) or > (Windows). That's just me showing you my session so you can see what I got.
* You type in the stuff after $ or >, then hit Enter. So if I have $ pwd, you type just pwd and hit Enter.
* You can then see what I have for output followed by another $ or > prompt. That content is the output, and you should see the same output.

**Linux/macOS**

```bash
$ pwd
/Users/zedshaw
$
```

**Windows**
```bash
PS C:\Users\zed> pwd

Path
----
C:\Users\zed

PS C:\Users\zed>
```

*注意
<br>在本附录中，我需要节省空间，以便您可以专注于命令的重要细节。要做到这一点，我将剥离出提示的第一部分（PS C：\用户\捷思以上），并只留下小>部分。这意味着您的提示看起来不完全相同，但不要担心。
<br>请记住，从现在开始，我只拥有>告诉你是这样的提示。
<br>我正在为UNIX提示做同样的事情，但UNIX提示是如此多样化，以至于大多数人习惯于$意味着“只是提示”。*

**你了解到这一点**
<br>你的提示与我的提示有所不同。您可以在$和计算机名称之前使用您的用户名。在Windows上，它可能看起来也不同。关键是你看到的模式：

* 有一个提示。
* 你在那里输入一个命令。在这种情况下，它是pwd。
* 它印了一些东西。
* 重复。

你刚刚学到了pwd的功能，这意味着“打印工作目录”。什么是目录？这是一个文件夹。文件夹和目录是相同的，它们可以互换使用。当您在计算机上打开文件浏览器以图形方式查找文件时，您正在浏览文件夹。这些文件夹与我们将要使用的这些“目录”完全相同。

## 练习3：如果你迷路了
当您完成这些说明时，您可能会迷路。您可能不知道您的位置或文件的位置，也不知道如何继续。为了解决这个问题，我将教你输入要停止丢失的命令。

每当你迷路时，最有可能的原因是你输入了命令并且不知道你到底在哪里。你应该做的是输入pwd来打印你当前的目录。这告诉你你在哪里。

接下来的事情是你需要有一种方法回到你安全的地方，你的家。要做到这一点，请输入cd~，然后你回到家中。

这意味着如果您在任何时候迷路型：

```bash
PWD
cd~
```
第一个命令pwd告诉你你在哪里。第二个命令cd~带你回家，你可以再试一次。

**做这个**
<br>现在弄清楚你在哪里，然后用pwd和cd~回家。这将确保您始终在正确的位置。

**你了解到这一点**
<br>如果你迷路了怎么回到家里。

## 练习4：制作目录（mkdir）
在本练习中，您将学习如何使用mkdir命令创建新目录（文件夹）。

**做这个**
<br>记得！你需要先回家！在做这个练习之前，你的pwd然后cd~ 在您完成本附录中的所有练习之前，请先回家！

**Linux的/ MacOS的**
```bash
$  pwd
$  cd ~
$ mkdir temp
$ mkdir temp / stuff
$ mkdir temp / stuff / things
$ mkdir -p temp / stuff / things / orange / apple / pear / grape
$
```
Windows
```bash
> pwd
> cd ~
> mkdir temp


    Directory: C:\Users\zed


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/17/2011   9:02 AM            temp


> mkdir temp/stuff


    Directory: C:\Users\zed\temp


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/17/2011   9:02 AM            stuff


> mkdir temp/stuff/things


    Directory: C:\Users\zed\temp\stuff

Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/17/2011   9:03 AM            things


> mkdir temp/stuff/things/orange/apple/pear/grape


    Directory: C:\Users\zed\temp\stuff\things\orange\apple\pear


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/17/2011   9:03 AM            grape


>
```
这是我唯一一次列出pwd和cd~命令。他们每次都会参加练习。一直这样做。

**你了解到这一点**
<br>现在我们开始输入多个命令。这些是你运行mkdir的不同方法。是什么MKDIR吗？它制作目录。你为什么问这个？你应该做你的索引卡并记住你的命令。如果您不知道“ mkdir创建目录”，那么继续使用索引卡。

制作目录意味着什么？您可以将目录称为“文件夹”。他们是一回事。您在上面所做的就是在更多目录中的目录内创建目录。这被称为“路径”，它是一种说“第一温度，然后是东西，然后事情，这就是我想要它”的方式。这是一组指向计算机的方向，您希望将某些内容放在组成计算机硬盘的文件夹（目录）树中。

*注意
<br>在本附录中，我对所有路径使用/（斜杠）字符，因为它们现在在所有计算机上的工作方式相同。但是，Windows用户需要知道您也可以使用\（反斜杠）字符，而其他Windows用户通常会期望这种情况。*

**多做**
* 在这一点上，“路径”的概念可能会使您感到困惑。别担心。我们会用它们做更多的事情，然后你会得到它。
* 在临时目录中以不同级别创建20个其他目录。使用图形文件浏览器查看它们。
* 通过在其周围加上引号来创建名称中包含空格的目录：mkdir“I Have Fun”
* 如果临时目录已经存在，那么您将收到错误。使用cd更改为可以控制的工作目录并在那里进行尝试。在Windows桌面上是个好地方。

## 练习5：更改目录（cd）
在本练习中，您将学习如何使用cd命令从一个目录更改为另一个目录。

**做这个**
<br>我将再次给你这些会议的指示：

* 您不输入$（Unix）或>（Windows）。
* 在此之后输入内容，然后按Enter键。如果我有$ cd temp，你只需输入cd temp并按Enter键。
* 按Enter键后输出，然后是另一个$或>提示符。
* 总是先回家！做PWD然后CD〜 ，让你回到你的出发点。

**Linux的/ MacOS的**
```bash
$ cd temp
$ pwd
~/temp
$ cd stuff
$ pwd
~/temp/stuff
$ cd things
$ pwd
~/temp/stuff/things
$ cd orange/
$ pwd
~/temp/stuff/things/orange
$ cd apple/
$ pwd
~/temp/stuff/things/orange/apple
$ cd pear/
$ pwd
~/temp/stuff/things/orange/apple/pear
$ cd grape/
$ pwd
~/temp/stuff/things/orange/apple/pear/grape
$ cd ..
$ cd ..
$ pwd
~/temp/stuff/things/orange/apple
$ cd ..
$ cd ..
$ pwd
~/temp/stuff/things
$ cd ../../..
$ pwd
~/
$ cd temp/stuff/things/orange/apple/pear/grape
$ pwd
~/temp/stuff/things/orange/apple/pear/grape
$ cd ../../../../../../../
$ pwd
~/
$
```
**Windows**
```bash
> cd temp
> pwd

Path
----
C:\Users\zed\temp


> cd stuff
> pwd

Path
----
C:\Users\zed\temp\stuff


> cd things
> pwd

Path
----
C:\Users\zed\temp\stuff\things


> cd orange
> pwd

Path
----
C:\Users\zed\temp\stuff\things\orange


> cd apple
> pwd

Path
----
C:\Users\zed\temp\stuff\things\orange\apple


> cd pear
> pwd

Path
----
C:\Users\zed\temp\stuff\things\orange\apple\pear


> cd grape
> pwd

Path
----
C:\Users\zed\temp\stuff\things\orange\apple\pear\grape


> cd ..
> cd ..
> cd ..
> pwd

Path
----
C:\Users\zed\temp\stuff\things\orange


> cd ../..
> pwd

Path
----
C:\Users\zed\temp\stuff


> cd ..
> cd ..
> cd temp/stuff/things/orange/apple/pear/grape
> cd ../../../../../../../
> pwd

Path
----
C:\Users\zed


>
```
**你了解到这一点**
<br>你在最后一个练习中创建了所有这些目录，现在你只需要使用cd命令在它们内部移动。在我上面的会话中，我也使用pwd来检查我的位置，所以切记不要输入pwd打印的输出。例如，在第3行，您会看到〜/ temp，但这是pwd从其上方的提示输出。 不要输入。

您还应该看到我如何使用..在树和路径中“向上”移动。

**多做**
<br>学习在具有图形用户界面（GUI）的计算机上使用命令行界面（CLI）的一个非常重要的部分是弄清楚它们如何协同工作。当我开始使用计算机时没有“GUI”，你用DOS提示符（CLI）完成了所有工作。后来，当计算机变得足够强大以至于每个人都可以拥有图形时，我很容易将CLI目录与GUI窗口和文件夹相匹配。

然而，今天的大多数人都不了解CLI，路径和目录。事实上，向他们教授它是非常困难的，了解连接的唯一方法是让您不断使用CLI，直到有一天它点击您在GUI中执行的操作将显示在CLI中。

这样做的方法是花一些时间用GUI文件浏览器查找目录，然后用CLI进行访问。这就是你接下来要做的。

* 使用一个命令cd到apple目录。
* 使用一个命令cd回temp，但不要超过它。
* 了解如何使用一个命令cd到“主目录”。
* cd到您的Documents目录，然后使用您的GUI文件浏览器（Finder，Windows资源管理器等）找到它。
* cd到您的下载目录，然后使用您的文件浏览器找到它。
* 用文件浏览器找到另一个目录，然后cd到它。
* 还记得当你在一个带有空格的目录中放置引号时吗？您可以使用任何命令执行此操作。例如，如果你有一个`I Have Fun`的目录，你可以这样做： `cd "I Have Fun"`

## 练习6：列出目录（ls）
在本练习中，您将学习如何使用ls命令列出目录的内容。

**做这个**
<br>在开始之前，请确保您的CD回到上述临时目录。如果您不知道自己身在何处，请使用pwd计算出来然后移动到那里。

**Linux的/ MacOS的**
```bash
$ cd temp
$ ls
stuff
$ cd stuff
$ ls
things
$ cd things
$ ls
orange
$ cd orange
$ ls
apple
$ cd apple
$ ls
pear
$ cd pear
$ ls
$ cd grape
$ ls
$ cd ..
$ ls
grape
$ cd ../../../
$ ls
orange
$ cd ../../
$ ls
stuff
$
```

**Windows**
```bash
> cd temp
> ls


    Directory: C:\Users\zed\temp


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/17/2011   9:03 AM            stuff


> cd stuff
> ls


    Directory: C:\Users\zed\temp\stuff


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/17/2011   9:03 AM            things


> cd things
> ls


    Directory: C:\Users\zed\temp\stuff\things


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/17/2011   9:03 AM            orange


> cd orange
> ls


    Directory: C:\Users\zed\temp\stuff\things\orange


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/17/2011   9:03 AM            apple


> cd apple
> ls


    Directory: C:\Users\zed\temp\stuff\things\orange\apple


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/17/2011   9:03 AM            pear


> cd pear
> ls


    Directory: C:\Users\zed\temp\stuff\things\orange\apple\pear


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/17/2011   9:03 AM            grape


> cd grape
> ls
> cd ..
> ls


    Directory: C:\Users\zed\temp\stuff\things\orange\apple\pear


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/17/2011   9:03 AM            grape


> cd ..
> ls


    Directory: C:\Users\zed\temp\stuff\things\orange\apple


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/17/2011   9:03 AM            pear


> cd ../../..
> ls


    Directory: C:\Users\zed\temp\stuff


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/17/2011   9:03 AM            things


> cd ..
> ls


    Directory: C:\Users\zed\temp


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/17/2011   9:03 AM            stuff


>
```
**你了解到这一点**
<br>该LS命令列出了你当前目录的内容。你可以看到我用CD换穿不同的目录，然后列出什么在他们，所以我知道要到下一次的目录。

ls命令有很多选项，但是当我们介绍help命令时，你将学习如何获得帮助。

**多做**
* 输入这些命令中的每一个！你必须实际输入这些来学习它们。只是阅读它们还不够好。我现在不再大喊大叫了。
* 在Unix上，在你处于`temp`时尝试使用`ls -lR`命令。
* 在Windows上使用`dir -R`执行相同的操作。
* 使用`cd`进入计算机上的其他目录，然后使用`ls`查看其中的内容。
* 用新问题更新您的笔记本。我知道你可能有一些，因为我没有涉及这个命令的所有内容。
* 请记住，如果你迷路了，请使用`ls`和`pwd`找出你的位置，然后去你需要的地方用`cd`。

## 练习7：删除目录（rmdir）
在本练习中，您将学习如何删除空目录。

**做这个**

**Linux的/ MacOS的**
```bash
$ cd temp
$ ls
stuff
$ cd stuff/things/orange/apple/pear/grape/
$ cd ..
$ rmdir grape
$ cd ..
$ rmdir pear
$ cd ..
$ ls
apple
$ rmdir apple
$ cd ..
$ ls
orange
$ rmdir orange
$ cd ..
$ ls
things
$ rmdir things
$ cd ..
$ ls
stuff
$ rmdir stuff
$ pwd
~/temp
$
```
**警告**

如果你试图在macOS上做`rmdir`并且它拒绝删除目录，即使你是肯定的它是空的，那么实际上有一个名为``.DS_Store`的文件。在这种情况下，请键入`rm -rf <dir>``（将``<dir>``替换为目录名称）。

**Windows**
```bash
> cd temp
> ls


    Directory: C:\Users\zed\temp


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/17/2011   9:03 AM            stuff


> cd stuff/things/orange/apple/pear/grape/
> cd ..
> rmdir grape
> cd ..
> rmdir pear
> cd ..
> rmdir apple
> cd ..
> rmdir orange
> cd ..
> ls


    Directory: C:\Users\zed\temp\stuff


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/17/2011   9:14 AM            things


> rmdir things
> cd ..
> ls


    Directory: C:\Users\zed\temp


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/17/2011   9:14 AM            stuff


> rmdir stuff
> pwd

Path
----
C:\Users\zed\temp


> cd ..
>
```
**你了解到这一点**
<br>我现在正在混合命令，因此请确保您完全键入它们并注意。每次你犯错误，都是因为你没有注意。如果你发现自己犯了很多错误，那么休息一下或者放弃一天。你明天总是要再试一次。

在本例中，您将学习如何删除目录。这很容易。您只需转到它上面的目录，然后键入`rmdir <dir>`，将``<dir>``替换为要删除的目录的名称。

**多做**
* 再制作20个目录并将其全部删除。
* 创建一个10深的目录路径，并像以前一样一次删除它们。
* 如果您尝试删除包含内容的目录，则会出现错误。我将告诉你如何在以后的练习中删除它们。

## 练习8：四处移动（pushd, popd）
在本练习中，您将学习如何保存当前位置并使用pushd转到新位置。然后，您将学习如何使用popd返回保存的位置。

**做这个**

**Linux的/ MacOS的**
```bash
$ cd temp
$ mkdir -p i/like/icecream
$ pushd i/like/icecream
~/temp/i/like/icecream ~/temp
$ popd
~/temp
$ pwd
~/temp
$ pushd i/like
~/temp/i/like ~/temp
$ pwd
~/temp/i/like
$ pushd icecream
~/temp/i/like/icecream ~/temp/i/like ~/temp
$ pwd
~/temp/i/like/icecream
$ popd
~/temp/i/like ~/temp
$ pwd
~/temp/i/like
$ popd
~/temp
$ pushd i/like/icecream
~/temp/i/like/icecream ~/temp
$ pushd
~/temp ~/temp/i/like/icecream
$ pwd
~/temp
$ pushd
~/temp/i/like/icecream ~/temp
$ pwd
~/temp/i/like/icecream
$
```
**Windows**
```bash
> cd temp
> mkdir i/like/icecream


    Directory: C:\Users\zed\temp\i\like


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/20/2011  11:05 AM            icecream


> pushd i/like/icecream
> popd
> pwd

Path
----
C:\Users\zed\temp


> pushd i/like
> pwd

Path
----
C:\Users\zed\temp\i\like


> pushd icecream
> pwd

Path
----
C:\Users\zed\temp\i\like\icecream


> popd
> pwd

Path
----
C:\Users\zed\temp\i\like


> popd
>
```
*注意
<br>在WINDOWS中，您通常不需要像在LINUX中那样使用-P选项。但是，我认为这是一个更新的开发，因此您可能会遇到需要-P的旧WINDOWS POWERSHELL 。如果您有关于此的更多信息，请发送电子邮件至HELP@LEARNCODETHEHARDWAY.ORG，以便我可以解决是否提及-P FOR WINDOWS。*

**你了解到这一点**
<br>你正在使用这些命令进入程序员领域，但它们非常方便我必须教给你。这些命令允许您临时转到不同的目录，然后返回，轻松切换两者。

在`PUSHD`命令将当前目录和“pushes”入列表供以后，然后将其更改到另一个目录。这就像说：“保存我的位置，然后去这里。”

该`POPD`命令把你推过去的目录和“pops”而过，带你回到那里。

最后，在Unix `pushd`上，如果你自己运行它没有参数，它将在你当前的目录和你推送的最后一个目录之间切换。这是在两个目录之间切换的简单方法。 这在PowerShell中不起作用。

**多做**
* 使用这些命令可以在整个计算机上移动目录。
* 删除i / like / icecream目录并制作自己的目录，然后在其中移动。
* 向你自己解释pushd和popd将为你输出的输出。请注意它是如何工作的堆栈？
* 您已经知道这一点，但请记住，即使所有目录都不存在，mkdir -p（在Linux / macOS上）也会生成一个完整的路径。这就是我本次练习的第一步。
* 请记住，Windows将构成完整路径，不需要-p。

## 练习9：制作空文件（Touch，New-Item）
在本练习中，您将学习如何使用touch（Windows上的new-item）命令创建一个空文件。

**做这个**

**Linux的/ MacOS的**
```bash
$ cd temp
$ touch iamcool.txt
$ ls
iamcool.txt
$
```
**Windows**
```bash
> cd temp
> New-Item iamcool.txt -type file
> ls


    Directory: C:\Users\zed\temp


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
-a---        12/17/2011   9:03 AM            iamcool.txt


>
````
**你了解到这一点**
<br>您学会了如何制作一个空文件。在Unix上触摸这样做，它也会改变文件的时间。除了制作空文件之外，我很少使用它。在Windows上，您没有此命令，因此您学习了如何使用New-Item命令，该命令执行相同的操作，但也可以创建新目录。

**多做**
* Unix：创建一个目录，更改它，然后在其中创建一个文件。然后更改一级并在此目录中运行`rmdir`命令。你应该得到一个错误。试着理解为什么会出现这个错误。
* Windows：做同样的事情，但你不会得到错误。您将收到一个提示，询问您是否确实要删除该目录。

## 练习10：复制文件（cp）
在本练习中，您将学习如何使用cp命令将文件从一个位置复制到另一个位置。

**做这个**

**Linux的/ MacOS的**
```bash
$ cd temp
$ cp iamcool.txt neat.txt
$ ls
iamcool.txt neat.txt
$ cp neat.txt awesome.txt
$ ls
awesome.txt iamcool.txt neat.txt
$ cp awesome.txt thefourthfile.txt
$ ls
awesome.txt  iamcool.txt  neat.txt  thefourthfile.txt
$ mkdir something
$ cp awesome.txt something/
$ ls
awesome.txt iamcool.txt  neat.txt  something  thefourthfile.txt
$ ls something/
awesome.txt
$ cp -r something newplace
$ ls newplace/
awesome.txt
$
```

**Windows**
```bash
> cd temp
> cp iamcool.txt neat.txt
> ls


    Directory: C:\Users\zed\temp


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
-a---        12/22/2011   4:49 PM          0 iamcool.txt
-a---        12/22/2011   4:49 PM          0 neat.txt


> cp neat.txt awesome.txt
> ls


    Directory: C:\Users\zed\temp


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
-a---        12/22/2011   4:49 PM          0 awesome.txt
-a---        12/22/2011   4:49 PM          0 iamcool.txt
-a---        12/22/2011   4:49 PM          0 neat.txt


> cp awesome.txt thefourthfile.txt
> ls


    Directory: C:\Users\zed\temp


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
-a---        12/22/2011   4:49 PM          0 awesome.txt
-a---        12/22/2011   4:49 PM          0 iamcool.txt
-a---        12/22/2011   4:49 PM          0 neat.txt
-a---        12/22/2011   4:49 PM          0 thefourthfile.txt


> mkdir something


    Directory: C:\Users\zed\temp


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/22/2011   4:52 PM            something


> cp awesome.txt something/
> ls


    Directory: C:\Users\zed\temp


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/22/2011   4:52 PM            something
-a---        12/22/2011   4:49 PM          0 awesome.txt
-a---        12/22/2011   4:49 PM          0 iamcool.txt
-a---        12/22/2011   4:49 PM          0 neat.txt
-a---        12/22/2011   4:49 PM          0 thefourthfile.txt


> ls something


    Directory: C:\Users\zed\temp\something


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
-a---        12/22/2011   4:49 PM          0 awesome.txt


> cp -recurse something newplace
> ls newplace


    Directory: C:\Users\zed\temp\newplace


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
-a---        12/22/2011   4:49 PM          0 awesome.txt

>
```
**你了解到这一点**
<br>现在您可以复制文件了。只需取一个文件并将其复制到新文件即可。在本练习中，我还创建了一个新目录并将文件复制到该目录中。

我现在要告诉你关于程序员和系统管理员的秘密。他们很懒。我很懒。我的朋友很懒。这就是我们使用电脑的原因。我们喜欢让电脑为我们做无聊的事情。到目前为止，在练习中你一直在键入重复的无聊命令，以便你可以学习它们，但通常它不是这样的。通常情况下，如果你发现自己做了一些无聊和重复的事情，可能有一个程序员已经想出如何让它变得更容易。你只是不知道它。

关于程序员的另一件事是他们并不像你想象的那么聪明。如果你想要输入什么，那么你可能会弄错。相反，试着想象一下命令的名称对你来说并尝试它。有可能是它的名字或缩写类似于你的想法。如果你仍然无法直观地弄明白，那就四处询问并在线搜索。希望它不像ROBOCOPY那样真正愚蠢。

**多做**
* 使用`cp -r`命令复制包含文件的更多目录。
* 将文件复制到主目录或桌面。
* 在图形用户界面中查找这些文件，然后在文本编辑器中打开它们。
* 请注意我有时会在目录末尾添加``/``（斜杠）？这确保文件确实是一个目录，所以如果目录不存在，我将收到错误。

## 练习11：移动文件（mv）
在本练习中，您将学习如何使用mv命令将文件从一个位置移动到另一个位置。

**做这个**

**Linux的/ MacOS的**
```bash
$  cd temp
$ mv awesome.txt uncool.txt
$ ls
newplace uncool.txt
$ mv newplace oldplace
$ ls
oldplace uncool.txt
$ mv oldplace newplace
$ ls
newplace uncool.txt
$
```

**Windows**

```bash
> cd temp
> mv awesome.txt uncool.txt
> ls


    Directory: C:\Users\zed\temp


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/22/2011   4:52 PM            newplace
d----        12/22/2011   4:52 PM            something
-a---        12/22/2011   4:49 PM          0 iamcool.txt
-a---        12/22/2011   4:49 PM          0 neat.txt
-a---        12/22/2011   4:49 PM          0 thefourthfile.txt
-a---        12/22/2011   4:49 PM          0 uncool.txt


> mv newplace oldplace
> ls


    Directory: C:\Users\zed\temp


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/22/2011   4:52 PM            oldplace
d----        12/22/2011   4:52 PM            something
-a---        12/22/2011   4:49 PM          0 iamcool.txt
-a---        12/22/2011   4:49 PM          0 neat.txt
-a---        12/22/2011   4:49 PM          0 thefourthfile.txt
-a---        12/22/2011   4:49 PM          0 uncool.txt


> mv oldplace newplace
> ls newplace


    Directory: C:\Users\zed\temp\newplace


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
-a---        12/22/2011   4:49 PM          0 awesome.txt


> ls


    Directory: C:\Users\zed\temp


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/22/2011   4:52 PM            newplace
d----        12/22/2011   4:52 PM            something
-a---        12/22/2011   4:49 PM          0 iamcool.txt
-a---        12/22/2011   4:49 PM          0 neat.txt
-a---        12/22/2011   4:49 PM          0 thefourthfile.txt
-a---        12/22/2011   4:49 PM          0 uncool.txt


>
```
**你了解到这一点**
<br>移动文件，或者更改它们。这很容易：给出旧名称和新名称。

**多做**
* 将newplace目录中的文件移动到另一个目录，然后将其移回。

## 练习12：查看文件（更少，更多）
要做这个练习，你将使用你目前为止所知的命令做一些工作。您还需要一个可以生成纯文本（.txt）文件的文本编辑器。这是你做的：

打开文本编辑器并在新文件中键入一些内容。
* 在macOS上，这可能是TextWrangler。
* 在Windows上，这可能是Notepad ++。
* 在Linux上，这可能是gedit。任何编辑都会工作。

将该文件保存到桌面并将其命名为test.txt。
在shell中使用您知道的命令将此文件复制到您一直使用的临时目录中。
完成后，完成此练习。

**做这个**

**Linux的/ MacOS的**
```bash
$ less test.txt
[displays file here]
$
```

**Windows**
```bash
> more test.txt
[displays file here]
>
```

*注意
<br>在前面的输出中，我显示[在此处显示文件]以“缩写”该程序显示的内容。当我的意思是说“向你展示这个程序的输出过于复杂时，我会这样做，所以只需在这里插入你在计算机上看到的内容，并假装我确实向你展示了它。” 您的屏幕实际上不会显示此信息。*

**你了解到这一点**
<br>这是查看文件内容的一种方法。它很有用，因为如果文件有很多行，它将“分页”，这样一次只能看到一个屏幕。在“更多”部分中，您将更多地使用它。

**多做**
* 再次打开文本文件并反复复制粘贴文本，使其长度约为50-100行。
* 再次将其复制到``temp``目录，以便查看它。
* 现在再做一次练习，但是这一次通过它。在Unix上，你使用空格键和w（字母w）向下和向上。箭头键也有效。在Windows上，只需点击空格键即可浏览。
* 看看你创建的一些空文件。
* 在`CP`命令将覆盖已经存在的文件，所以要小心复制文件左右。

## 练习13：流式传输文件（cat）
您将为此进行更多设置，以便您习惯在一个程序中创建文件，然后从命令行访问它们。使用上一个练习中的相同文本编辑器，创建另一个名为test2.txt的文件，但这次将其直接保存到临时目录中。

**做这个**

**Linux的/ MacOS的**
```bash
$ less test2.txt
[displays file here]
$ cat test2.txt
I am a fun guy.
Don't you know why?
Because I make poems,
that make babies cry.
$ cat test.txt
Hi there this is cool.
$
```
**Windows**
```bash
> more test2.txt
[displays file here]
> cat test2.txt
I am a fun guy.
Don't you know why?
Because I make poems,
that make babies cry.
> cat test.txt
Hi there this is cool.
>
```
请记住，当我说``[displays file here]``时，我缩写了该命令的输出，因此我不必向您展示所有内容。

**你了解到这一点**
<br>你喜欢我的诗吗？完全赢得诺贝尔奖。无论如何，你已经知道了第一个命令，我只是让你检查你的文件是否存在。然后你把文件抓到屏幕上。此命令只是将整个文件喷射到屏幕上，没有分页或停止。为了证明这一点，我让你对`test.txt`做这个，它应该从这个练习中吐出一堆线。

**多做**
* 再制作一些文本文件并使用cat。
* Unix：尝试`cat test.txt test2.txt`，看看它做了什么。
* Windows：尝试`cat test.txt，test2.txt`，看看它的作用。

## 练习14：删除文件（rm）
在本练习中，您将学习如何使用rm命令删除（删除）文件。

**做这个**

**Linux的**
```bash
$ cd temp
$ ls
uncool.txt  iamcool.txt  neat.txt  something  thefourthfile.txt
$ rm uncool.txt
$ ls
iamcool.txt  neat.txt  something  thefourthfile.txt
$ rm iamcool.txt neat.txt thefourthfile.txt
$ ls
something
$ cp -r something newplace
$
$ rm something/awesome.txt
$ rmdir something
$ rm -rf newplace
$ ls
$
```
**Windows**
```bash
> cd temp
> ls


    Directory: C:\Users\zed\temp


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/22/2011   4:52 PM            newplace
d----        12/22/2011   4:52 PM            something
-a---        12/22/2011   4:49 PM          0 iamcool.txt
-a---        12/22/2011   4:49 PM          0 neat.txt
-a---        12/22/2011   4:49 PM          0 thefourthfile.txt
-a---        12/22/2011   4:49 PM          0 uncool.txt


> rm uncool.txt
> ls


    Directory: C:\Users\zed\temp


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/22/2011   4:52 PM            newplace
d----        12/22/2011   4:52 PM            something
-a---        12/22/2011   4:49 PM          0 iamcool.txt
-a---        12/22/2011   4:49 PM          0 neat.txt
-a---        12/22/2011   4:49 PM          0 thefourthfile.txt


> rm iamcool.txt
> rm neat.txt
> rm thefourthfile.txt
> ls


    Directory: C:\Users\zed\temp


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        12/22/2011   4:52 PM            newplace
d----        12/22/2011   4:52 PM            something


> cp -r something newplace
> rm something/awesome.txt
> rmdir something
> rm -r newplace
> ls
>
```
**你了解到这一点**
<br>在这里，我们清理上一个练习中的文件。还记得当我尝试使用其中包含某些内容的`rmdir`时吗？好吧，失败了，因为你无法删除包含文件的目录。为此，您必须删除该文件或递归删除其所有内容。这就是你在这结束时所做的。

**多做**
* 到目前为止，从所有练习中清除所有温度。
* 写入笔记本时要小心运行递归删除文件。

## 练习15：退出终端（退出）
**做这个**

**Linux的/ MacOS的**
```bash
$ exit
```

**Windows**
```bash
> exit
```
**你了解到这一点**
<br>您最后的练习是如何退出终端。这又很容易，但我会让你做得更多。

**多做**
<br>对于你的最后一组练习，我将让你使用帮助系统来查找你应该研究的一组命令，并学习如何自己使用。

这是Unix的列表：
* xargs
* sudo
* chmod
* chown

对于Windows，请查看以下内容：
* forfiles
* runas
* attrib
* icacls

找出它们是什么，与它们一起玩，然后将它们添加到索引卡中。

## 命令行后续步骤
您已完成速成课程。此时你应该是一个几乎没有能力的shell用户。有一大堆你不知道的技巧和关键序列，我会给你一些最后的研究方向。

**Unix Bash参考**
<br>你一直在使用的shell叫做Bash。它不是最好的外壳，但它无处不在，并且具有很多功能，所以这是一个好的开始。以下是关于Bash的简短列表，您应该阅读：

Bash备忘单
<br>https://learncodethehardway.org/unix/bash_cheat_sheet.pdf由Raphael和CC授权创建。

参考手册
<br>http://www.gnu.org/software/bash/manual/bashref.html

**PowerShell参考**
<br>在Windows上，实际上只有PowerShell。以下是与PowerShell相关的有用链接列表：

用户手册
<br>http://technet.microsoft.com/en-us/library/ee221100.aspx

备忘单
<br>https://download.microsoft.com/download/2/1/2/2122F0B9-0EE6-4E6D-BFD6-F9DCD27C07F9/WS12_QuickRef_Download_Files/PowerShell_LangRef_v3.pdf

掌握PowerShell
<br>http://powershell.com/cs/blogs/ebook/default.aspx
