# -*- coding: utf-8 -*-

# range
print '#range'
X = 'spam'
for i in range(len(X)):
    print (X[i])

print '--------'

S = 'abcdefghijk'
for i in range(0,len(S),2):
    print S[i]

print '--------'

# 下面方法更容易理解，但是会复制一个字符串，如果字符串很大，占用内存较大
S = 'abcdefghijk'
for c in S[::2]:
    print c 

# zip
print '\n#zip'
L1 = [1,2,3,4]
L2 = [5,6,7,8]
for (x,y) in zip(L1,L2):
    print (x,y,x+y)

keys = ['a','b','c']
vals = [1,3,5]
D2 = {}
for (k,v) in zip(keys,vals): D2[k]=v
print D2

# enumerate 可以获得元素和元素的偏移值
print '\n#enumerate'
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print enumerate(seasons, start=3)
print list(enumerate(seasons, start=3))
print dict(enumerate(seasons, start=3))
print tuple(enumerate(seasons, start=3))

# map 
print '\n#map'
S1 = 'abc'
S2 = 'xyz123'
print map(None,S1,S2)
print map(pow, [1,2,3], [2,3,4])
print map((lambda x: x+3),[1,2,3,4])
def inc(x):
    return x+10
print map(inc,[1,2,3])

import math
print list(map(math.sqrt,(x ** 2 for x in range(4))))

# filter 
print '\n#filter'
print list(filter((lambda x:x>0),range(-5,5)))

# reduce
print '\n#reduce'
print reduce((lambda x,y:x+y),[1,2,3,4])

import operator,functools
print functools.reduce(operator.add,[2,4,6])

# squares 列表推导公式
print '\n#列表推导公式'
squares = []
for x in range(10):
     squares.append(x**2)
print squares

squares = [x**2 for x in range(10)]
print squares

print [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
         if x != y:
            combs.append((x, y))
print combs

vec = [-4, -2, 0, 2, 4]
print [x*2 for x in vec]

print [x for x in vec if x >= 0]

print [abs(x) for x in vec]

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print [weapon.strip() for weapon in freshfruit]

print [(x, x**2) for x in range(6)]

vec = [[1,2,3], [4,5,6], [7,8,9]]
print [num for elem in vec for num in elem]

from math import pi
print [str(round(pi, i)) for i in range(1, 6)]


# 嵌套的列表推导式
print '\n#嵌套的列表推导式'
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]

print [[row[i] for row in matrix] for i in range(4)]

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print transposed

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print transposed

print list(zip(*matrix))
