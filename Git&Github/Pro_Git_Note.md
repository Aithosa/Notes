# Pro Git Note

## 初次运行 Git 前的配置
Git 自带一个 `git config` 的工具:
* 用户信息
    * $ git config --global user.name "John Doe"
    <br>$ git config --global user.email johndoe@example.com
* 文本编辑器
    * git config --global core.editor emacs
* 检查配置信息
    * git config --list
    * 通过输入`` git config <key>`` 来检查 Git 的某一项配置
    <br>git config user.name

获取帮助:
* ```bash
$ git help <verb>
$ git <verb> --help
$ man git-<verb>
```
* 获得 config 命令的手册:
<br>git help config

## Git 基础
### 获取 Git 仓库
两种取得 Git 项目仓库的方法:
* 在现有项目或目录下导入所有文件到 Git
* 从一个服务器克隆一个现有的 Git 仓库。
#### 在现有目录中初始化仓库
```bash
$ git init
跟踪这些文件并提交：
$ git add *.c
$ git add LICENSE
$ git commit -m 'initial project version'
```
#### 克隆现有的仓库
```bash
git clone [url]
git clone [url] [new name]
```
#### 记录每次更新到仓库
你工作目录下的每一个文件都不外乎这两种状态：
* 已跟踪
    > 已跟踪的文件是指那些被纳入了版本控制的文件，在上一次快照中有它们的记录，在工作一段时间后，它们的状态可能处于未修改，已修改或已放入暂存区。

* 未跟踪
    > 工作目录中除已跟踪文件以外的所有其它文件都属于未跟踪文件，它们既不存在于上次快照的记录中，也没有放入暂存区。

#### 检查当前文件状态
```bash
git status
$ echo 'My Project' > README
$ git status
```
#### 跟踪新文件
```bash
git add README
git status
git add
```
命令使用文件或目录的路径作为参数；如果参数是目录的路径，该命令将递归地跟踪该目录下的所有文件。
#### 暂存已修改文件
要暂存文件更新，需要运行 git add 命令。
> 这是个多功能命令：
* 可以用它开始跟踪新文件，
* 或者把已跟踪的文件放到暂存区，
* 还能用于合并时把有冲突的文件标记为已解决状态等。

<br>将这个命令理解为“**添加内容到下一次提交中**”而不是“将一个文件添加到项目中”要更加合适。
```bash
$ git add CONTRIBUTING.md
$ git status
```
#### 状态简览
`git status` 命令的输出十分详细，但其用语有些繁琐。 如果你使用 `git status -s` 命令或 `git status --short` 命令，你将得到一种更为紧凑的格式输出。
* 新添加的未跟踪文件前面有 ?? 标记，
* 新添加到暂存区中的文件前面有 A 标记，
* 修改过的文件前面有 M 标记。
    * M 有两个可以出现的位置，
        * 出现在右边的 M 表示该文件被修改了但是还没放入暂存区，
        * 出现在靠左边的 M表示该文件被修改了并放入了暂存区。

```bash
M README
MM Rakefile
A lib/git.rb
M lib/simplegit.rb
?? LICENSE.txt
```
#### 忽略文件
一般我们总会有些文件无需纳入 Git 的管理，也不希望它们总出现在未跟踪文件列表。这种情况下，我们可以创建一个名为 ``.gitignore``的文件，列出要忽略的文件模式。
```bash
$ cat .gitignore
*.[oa]  # 告诉 Git 忽略所有以 .o 或 .a 结尾的文件。
*~      # 告诉 Git 忽略所有以波浪符（~）结尾的文
```
文件 .gitignore 的格式规范如下：
* 所有空行或者以 ＃ 开头的行都会被 Git 忽略。
* 可以使用标准的 glob 模式匹配。
* 匹配模式可以以（/）开头防止递归。
* 匹配模式可以以（/）结尾指定目录。
* 要忽略指定模式以外的文件或目录，可以在模式前加上惊叹号（!）取反。

所谓的 glob 模式是指 shell 所使用的简化了的正则表达式。 星号（``*``）匹配零个或多个任意字符；[abc] 匹配任何一个列在方括号中的字符（这个例子要么匹配一个 a，要么匹配一个 b，要么匹配一个 c）；问号（?）只匹配一个任意字符；如果在方括号中使用短划线分隔两个字符，表示所有在这两个字符范围内的都可以匹配（比如 [0-9] 表示匹配所有 0 到 9 的数字）。 使用两个星号（``*``) 表示匹配任意中间目录，比如`a/**/z` 可以匹配 a/z, a/b/z 或 `a/b/c/z`等。
```bash
# no .a files
*.a
# but do track lib.a, even though you're ignoring .a files above
!lib.a
# only ignore the TODO file in the current directory, not subdir/TODO
/TODO
# ignore all files in the build/ directory
build/
# ignore doc/notes.txt, but not doc/server/arch.txt
doc/*.txt
# ignore all .pdf files in the doc/ directory
doc/**/*.pdf
```
> GitHub 有一个十分详细的针对数十种项目及语言的 .gitignore 文件列表，你可以在 https://github.com/github/gitignore 找到它.

#### 查看已暂存和未暂存的修改
你想知道具体修改了什么地方，可以用 `git diff` 命令来回答这两个问题：
* 当前做的哪些更新还没有暂存？
* 有哪些更新已经暂存起来准备好了下次提交？

若要查看已暂存的将要添加到下次提交里的内容，可以用 `git diff --cached` / `git diff --staged` 命令（Git 1.6.1 及更高版本）。
> Git Diff 的插件版本
<br>在本书中，我们使用 git diff 来分析文件差异。 但是，如果你喜欢通过图形化的方式或其它格式输出方式的话，可以使用 git difftool 命令来用 Araxis ，emerge 或 vimdiff 等软件输出 diff 分析结果。 使用 git difftool --tool-help 命令来看你的系统支持哪些 Git Diff 插件。

#### 提交更新
git commit
