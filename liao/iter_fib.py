# --coding:utf-8--
# 让类可以使用for...in循环
# 2017/8/4

#斐波那契函数为例
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1   #初始化

	def __iter__(self):
		return self             #实例本身为迭代对象

	def next(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 100000:
			raise StopIteration();
		return self.a           #返回下一个值

for n in Fib():
	print n