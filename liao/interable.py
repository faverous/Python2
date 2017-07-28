# -- coding: utf-8 --
# 20170728
# 迭代问题
from collections import Iterable # 判断是否可迭代
print "判断abc是否可迭代"
print isinstance('abc',Iterable)
print "判断整形123是否可迭代"
print isinstance(123,Iterable)

#迭代的作用
d = {'a':1,'b':2,'c':3} #dict类型,默认以key为迭代值
for key in d:
	print key

for ch in 'ABC':
	print ch

# enumerate方法，可以将下标转化为数字
for i,value in enumerate(['A','B','C']):
	print i, value

