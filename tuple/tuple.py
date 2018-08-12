# -*- coding: utf-8 -*-
tup1 = ('physic' , 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );

print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]

tup3 = tup1 + tup2;
print tup3;

# 任意无符号的对象，以逗号隔开，默认为元组，如下实例：
print 'abc', -4.24e93, 18+6.6j, 'xyz';
x, y = 1, 2;
print "Value of x , y : ", x,y;

T = ('c','a','d','e')
tmp = list(T)
tmp.sort()
print tmp
print tuple(tmp)

T = ('c','a','d','e')
print sorted(T)

T = (1,2,3,4,5)
L = [x+20 for x in T]
print L

T = (1,2,3,2,3,5,2)
print T.index(2)
print T.index(5,2,7)
print T.count(2)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)
print fruit
print 'orange' in fruit
print 'crabgrass' in fruit

a = set('abracadabra')
b = set('alacazam')
print 'a:\t',a                                  # 唯一值
print 'a - b:\t',a - b                              # 在a不在b里面
print 'a | b:\t',a | b                              # 在a或b里
print 'a & b:\t',a & b                              # a、b里面都有
print 'a ^ b:\t',a ^ b                              # 在a或b里但是不同时在两个里面
print 'a>b,a<b:\t',a>b,a<b

a = {x for x in 'abracadabra' if x not in 'abc'}#'abc'默认是集合
print a

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)
print fruit

S = set()
S.add((1,2,3))
print S

# S.add([4,5,6]) # error, ubhashable type: 'list'

print type(S)
