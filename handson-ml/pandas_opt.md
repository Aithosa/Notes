使用 DataFrame 的 head() 方法查看该数据集的前5行
housing.head(10)

info()方法可以快速查看数据的描述，特别是总行数、每个属性的类型和非空值的数量
housing.info()

用 value_counts() 方法查看该项中都有哪些类别，每个类别中都包含有多少个街区
housing["ocean_proximity"].value_counts()

describe()方法展示了数值属性的概
housing.describe()

使用 corr() 方法计算出每对属性间的标准相关系数（standard correlation coefficient，也称作皮尔逊相关系数）：
housing.corr()
