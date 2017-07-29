# -- coding: utf-8 --
# 匿名函数lambda，只能有一个表达式，不需要return，表达式结果就是返回值
def build(x,y):
	return lambda: x * x + y * y

a = build(1,2)()
print a


# lambda的使用：在常规函数中使用匿名函数时，在调用时要引用双括号，注意参数的使用
