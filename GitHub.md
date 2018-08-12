# Github

----------

### 1. 基本概念

1. 仓库（Repository）：用来存放项目代码，每个项目对应一个仓库，多个开源项目对应多个仓库。	
2. 收藏（Star）：方便下次查看。	
3. 复制克隆项目（Fork）：Fork后的项目是独立存在的。		
4. 发起请求（Pull Request）：把自己修改的代码请求更新到原创建者，原创建者同意后可以合并到自己的仓库中。	
5. 关注（Watch）：关注动态。	
6. 事物卡片（Issue）：发现代码BUG，但是目前没有成型代码，需要讨论使用。

### 2. 主页
	
1. Github主页
2. 仓库主页
3. 个人主页
	
###3. 操作

1. 创建文件	
2. 编辑文件：commits可以查看文件每次的变动信息。	
3. 删除文件	
4. 上传文件
5. 查找文件

### 4. Issue

提交bug讨论，已解决可以点击close issue关闭issue（双方都可以关闭）。

### 5. 开源项目贡献流程

1. 新建Issue：提交问题、建议或者想法。
2. Pull Issue直接修正代码
	1. fork项目
	2. 修改自己仓库的项目代码
	3. 新建pull request
	4. 等待原作者合并

# Git

----------

- keep track of changes to code.
- Synchronizes code between different people.
- Test changes to code between different people.
- Revert back to old versions of code. 

### 1. Git工作区域

1. 工作区：添加、编辑、修改文件。

		'git status'
		'git add hello.py'

2. 暂存区：暂存已经修改的文件，等待统一提交到git仓库中。

		'git status'
		'git commit -m "message"'

	或者两布合作一步

		'git commit -am "message"

3. Git Repository：最终确定的文件保存到仓库，成为一个新版本，并且对他人可见。

		'git status'

### 2. Git基础设置

1. 设置用户名
 
		'git config --global user.name 'itcast''

2. 设置用户名邮箱
 
		'git config --global user.email 'itcast@itcast.com''

3. 查看设置
 
		'git config --list'

### 3. 初始化一个新的Git仓库
	
1. 创建新的文件夹：

		'mkdir name'

2. 在文件内初始化git（创建git仓库）：
 
		'cd newfolder'
		'git init'

	*注: 'pwd'显示当前位置，同一个文件夹只用初始化一次？*

### 4. 创建项目

1. 创建文件：

		'touch test.py'

2. 提交到暂存区：
 
		'git status'
		'git add test.py'

3. 将文件提交到仓库：
 
		'git status'
		'git commit -m 'add test.py''

4. 查看状态：

		'git status'

5. 修改仓库文件：

		'vi test.py'

	随时用
 
		'git status'

	查询状态，并按步骤提交。
 
6. 删除仓库文件：

	'rm -rf test.py'

### 5. Git管理远程仓库

在以上几步之后使用

	'git push'

将本地仓库提交到远程

### 6. Pull

retrives changes from remote repository

	'git pull'

### 7. Merge conflicts

- when different commits can't be automatically merged
- need to be resolved

after `git pull`：

	<<<<<<< HEAD
	'your changes'
	=======	
	'remote changes'
	>>>>>>> <conflicting commit>
	
### 8. Log

shows a history of commits and messages

	'git log'

### 9. Reset

reverts code back to a previous commit

	git reset --hard <commit>
	e.g. git reset --hard 4761626(see log)

reverts code back to remote repository version

	git reset --hard origin/master

### 10. Branch

- show all branched of code

		git branch

- creat a branch with 

		git branch <branch_name>

- switch to ('cheakout') a new branch with

		git cheakout <branch_name>	（切换到另一个分支）

		e.g. master > `git branch test` > test 

### 11. Merge

merges the branch *branch_name* with current branch

	git mergr <branch_name> 
	
	e.g. `git merge tests` tests的所有版本都会合并到master分支中

### 12. Clone

- makes a copy of a repository.
- stores it on your computer.
- a "fork" creates your own copy of someone else's repository.

		'git clone <url>'

		url是github主页上的项目地址。

### 13. 无法同步或没有权限的问题

私有项目，没有权限，输入用户名和密码，或者远程地址采用这种类型：

	`vi .git/config`

		[remote "origin"]
			url = https://github.com/name/repository_name.git
		修改为
		[remote "origin"]
			url = https://name:password@github.com/name/repository_name.git

*注：防止别人修改远端仓库：*

2018/4/6 0:23:21 