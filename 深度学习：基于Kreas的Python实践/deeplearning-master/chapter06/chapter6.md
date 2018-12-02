## Chapter 6 在Keras中使用Scikit-Learn

Python中的Scikit-Learn是非常受欢迎的机器学习库，基于Scipy，用于高效的数值计算。Scikit-Learn中提供了很多用于选择模型和对模型调优的方法，这些方法同样适用于深度学习。

Keras类库为深度学习模型提供了一个包装类(Wrapper),将Keras的深度学习模型包装为Scikit-Learn中的分类模型或回归模型，以便于方便的使用Scikit-Learn中的方法和函数。对深度学习模型的包装是通过KerasClassifier(用于分类模型)和KerasRegressor(用于回归模型)来实现的。

### 6.1 使用交叉验证评估模型
KerasClassifier和KerasRegressor类使用参数build_fn，指定用来创建模型的函数的名称。因此，必须定义一个函数，通过函数来定义深度学习的模型，编译并返回它。

### 6.2 深度学习模型调参
通过Keras的包装类，借助Scikit-Learn的网格搜索，算法评估神经网络模型的不同配置，并找到最佳评估性能的参数组合。create_model()函数被定义为具有两个默认值的参数(optimizer和init)的函数，这便于对神经网络使用不同的优化器和权重初始化方案进行评估。创建模型后，定义要搜索的参数的值数组，包括优化器(optimizer)、权重初始化方案(init)、epoch和batch_size。

在Scikit-Learn中的GridSearchCV需要一个字典类型的字段作为需要调参的参数，默认采用3折交叉验证来评估算法，由于有4个参数需要进行调参，因此会产生4x3个模型。如果参数比较多，会生成比较多的模型，因此需要进行大量的计算，不适合大数据量的情况下使用。