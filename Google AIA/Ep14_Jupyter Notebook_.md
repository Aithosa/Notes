# Ep14 Jupyter Notebook

1. 安装方法：pip install jupyter

2. 只有没有被赋值的变量才会出现在输出单元中
``` python
import tensorflow as tf
version = str(tf.__version__)
'This TF is version ' + version
```
3. 显示你正在调用函数的docstring(简版)：Shift + Tab
4. 缩小输出区大小：
	1. 点击输出内容左侧的空白区域即可
	2. 双击可以完全隐藏
5. 创建新格子：Shift + Enter，当前单元执行，跳到下一个单元/创建下一个空白单元
6. 在任意单元格后添加新单元格：Alt + Enter(当前单元格会被执行)
7. 代码块前加上`%%time`，可以在输出后显示花了多少时间
8. 执行命令行指令：在代码前加上一个英文感叹号(只能运行一条指令)
<br>`!gsutil ls gs://cloudml-public/census/data`
9. 执行批处理命令：
```bash
%%bash
ls
pwd
whoami
```
10. 这个功能可以用于启动TensorBoard
<br>`!tensorboard --logdir=/tmp/MNIST_data`
<br>其打开期间单元格会一直处于运行状态，停止可以点击方形的停止按钮
