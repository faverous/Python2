# -- coding:utf-8 --
# filter是筛选器，参数有两个，第一个是函数，第二个是列表，作用是将列表中每个元素执行函数，根据返回值时True or False决定是否保留,删除返回true的值
# 本程序实现删除1-100中的素数

def is_su(m):
	fin = False
	if(m==1): 
		fin = True
	else:
		for i in range(2,m):
			if(m%i==0):
				fin = True
	return fin 
l = range(1,101)
print l
print filter(is_su, l)
