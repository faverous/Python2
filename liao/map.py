# -- coding: utf-8 --
# map()函数的使用，接收两个参数，第一个参数为函数，第二个为列表，将函数依次应用到列表元素中

def f(str):
	return str.capitalize()

a = []
n = int(raw_input("> "))
for i in range(0,n):
	a.append(raw_input())	
print map(f, a)

