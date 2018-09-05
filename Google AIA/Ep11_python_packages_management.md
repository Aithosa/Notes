# Ep11 python packages management
1. pip安装配置环境
`pip install -r requirements.txt`

2. 两种python包管理工具：Virtualenv和Anaconda
3. Anaconda
``` python
conda create --name aiadeventures
python=3.5
conda activate aiadventures
conda install tensorflow
pip install tensorflow=1.4
```
4. 两个包管理工具在一个机器里偶尔会不协调，可以用pyenv
> pyenv 是凌驾于virtualenv和Anaconda之上的，可以控制两者的环境，并且可以帮助选择python2还是python3。

```bash
pyenv

github.com/pyenv/pyenv

pyenv local 2.7.10
pyenv activate py27_tf11

pyenv local 3.5.2
pyenv activate py35_tf12
```
pyenv可以在指定文件夹里设置一个默认开发环境，于是一进入某个文件夹，对应的开发环境就自动启动
```
pyenv

~/code $ cd mypoject
(py35_tf11) ~/code/myproject $
```
