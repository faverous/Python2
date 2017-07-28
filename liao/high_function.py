# --coding: utf-8--
# 高阶函数：把函数作为参数传入新的函数中所构成的函数

f = abs #将绝对值函数赋给变量f
a = 12
b = -23
print a+b
def add(a,b,f):
	return f(a) + f(b)

print add(a,b,f)

