# -*- coding: utf-8 -*-
import pandas as pd

# 建立一个简单的dataframe
# 一个三行两列的数据
d= [[1,2],
    [3,4],
    [5,6]]
# 列名
v=['a','b']
#行名
h=['c','d','e']

print d
# 将数据d，列名v，行名h组合成一个dataframe
df = pd.DataFrame(data=d,index=h,columns=v)
print df

# 建立一个简单的字典型数据
dic={'a':[1,3,5],'b':[2,4,6]}
print dic
df = pd.DataFrame(data=dic,index=['c','d','e'])
print df
