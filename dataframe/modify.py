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

print '--------'
df['new'] = [6,7,8]
print df

print '--------'
df.loc['new_loc',:] = [6,7,8]
print df

#删除行或列——df.drop
#df.drop(labels,axis=0，inplace=False)
#
#labels 行或列的标签名，写在第一个可省略。
#axis= 0 删除行；1 删除列
#inplace= False 生成新dataframe；True 不生成新的dataframe，替换原本dataframe。默认是False。
#该操作默认返回的是另一个新的dataframe，以至于原来的没有变，如在下面第一个例子中删除的列，在第二个例子中还有。要替换原来的请调整inplace参数

print '--------'
print df.drop(['new'], axis=1)

print '--------'
print df.drop(['new_loc'], axis=0)
