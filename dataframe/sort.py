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

print '------'
# 转置
print '\n#转置'
print df.T

print '------'
print '# 按行名降序排序'
print df.sort_index(axis=0, ascending=False)

print '------'
print '# 按值排序'
print df.sort_values(axis=0, by=['a'], ascending=False)
