# -*- coding: utf-8 -*-
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1

for letter in 'Python':     # 第一个实例
   print '当前字母 :', letter

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print '当前字母 :', fruit

T = [(1,2), (3,4), (5,6)]
for (a,b) in T:
    print (a,b)

D = {'a':1,'b':2,'c':3}
for key in D:
    print (key, '=>', D[key])

print D.items()

for (key,value) in D.items():
    print (key,'=>',value)

for ((a,b),c) in [((1,2),3),((4,5),6)]: print (a,b,c)

print '---------'
for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print 'Current Letter :', letter

print '---------'
for letter in 'Python':     # 第一个实例
   if letter == 'h':
      continue
   print '当前字母 :', letter

print '---------'
for letter in 'Python':
   if letter == 'h':
      pass
      print '这是 pass 块'
   print '当前字母 :', letter
