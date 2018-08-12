# -*- coding: utf-8 -*-
L = [1,2,3,'a','b','c',4,5,6,7,8,9]
print L
print len(L)
print L[0]
print L[-1]
print L[1:5]
print L + [2,3,4]

a = [1, 2, 3, 3, 1234.5]
print 'a中 1 出现的次数：',a.count(1)
print 'a中 3 出现的次数：',a.count(3) 
print 'a中 x 出现的次数：',a.count('x')


# 在a的尾部添加元素# 在a的尾部 
a.append(555)
print a

# 返回2在a中的位置
print a.index(2)

a.reverse()
print a

# 对a进行排序，默认为升序！
a.sort()
print a

a.sort(reverse=True)
print a

# 删除列表a中值为 3 的第一个元素
a.remove(3)
print a

del a[0]
print a

del a[2:4]
print a

# 删除整个变量，回收
del a
print a

