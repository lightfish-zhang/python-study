# -*- coding: utf-8 -*-
print abs(-100)

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print my_abs(-100)

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print power(5,2)

def power2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print power2(3)


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc([1,2,3])

# 不定参数
def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc2(1,2,3)

nums = [1,2,3]
print calc2(*nums)

# 关键字参数
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

person('Michael', 30)
person('Adam', 45, gender='M', job='Engineer')

#　在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

func(1,2,3,'a','b',x=99)

# *args是可变参数，args接收的是一个tuple；

# **kw是关键字参数，kw接收的是一个dict。
