# -*- coding: utf-8 -*-
x = 88
def func():
    global x
    x = 99
func()
print x

y,z = 1,2
def all_global():
    global x
    x = y + z
all_global()
print x

# 匿名函数 lambda
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
# lambda函数拥有自己的名字空间，且不能访问自有参数列表之外或全局名字空间里的参数。
# 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
import time
start = time.clock()
fib=lambda n,x=0,y=1:x if not n else fib(n-1,y,x+y)
print fib(20)
end = time.clock()
print "read: %f s" % (end - start)

start = time.clock()
fib=lambda n:1 if n<=2 else fib(n-1)+fib(n-2)
print fib(20)
end = time.clock()
print "read: %f s" % (end - start)
