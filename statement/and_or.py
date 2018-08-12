# -*- coding: utf-8 -*-
print 2 < 3, 3 < 2
print 2 or 3, 3 or 2
print [] or 3
print [] or {} 
print 2 and 3, 3 and 2
print [] and {} #空 list 本身等同于 False

A = False
B = []
C = 0
X = A or B or C or None #会把X设为A、B以及C中第一个非空（为真）的对象，或者所有对象都为空就设为None
print X
