# --coding: utf-8--
# __slots__方法，用于限制类中添加的动态属性
# 2017/8/5

class Student(object):
	__slots__ = ('name', 'age') #动态添加属性时，只能添加这两类

# test
s = Student()
s.name = 'Tom'
print s.name

s.score = 120
print s.score #报错	