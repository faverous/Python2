# --coding: utf-8 --
# reduce()函数的使用，接收两个参数，第一个参数为函数，第二个参数为列表，从列表前两个元素开始，应用函数，并将结果与下一个参数循环应用函数

l = []
def multi(x,y):
	return x * y
n = int(raw_input("输入个数> "))
for i in range(0,n):
	l.append(int(raw_input()))
print l	
print reduce(multi, l)
